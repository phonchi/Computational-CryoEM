import numpy as np
import matplotlib.pyplot as plt
import numpy.linalg as LA
from scipy.sparse.linalg import svds, eigs
from numpy.linalg import svd
from sklearn import metrics
from datetime import datetime as dt
import os
import pandas as pd
import sys
import seaborn as sns

import mrc
from mrc import LazyImage
import mrcfile 

### Some of code are from https://github.com/PrincetonUniversity/ASPIRE-Python and https://github.com/zhonge/cryodrgn

########### io #################
class Starfile():
    
    def __init__(self, headers, df):
        self.headers = headers
        self.df = df

    @classmethod
    def load(self, starfile):
        f = open(starfile,'r')
        # get to data block
        while 1:
            for line in f:
                if line.startswith('data_'):
                    break
            break
        # get to header loop
        while 1:
            for line in f:
                if line.startswith('loop_'):
                    break
            break
        # get list of column headers
        while 1:
            headers = []
            for line in f:
                if line.startswith('_'):
                    headers.append(line)
                else:
                    break
            break 
        # assume the rest is the body
        headers = [h.strip().split()[0] for h in headers]
        body = [line]
        for lines in f:
            body.append(lines)
        # remove last line of body if empty
        if body[-1].strip() == '':
            body = body[:-1]
        # put data into an array and instantiate as dataframe
        words = [l.strip().split() for l in body]
        words = np.array(words)
        data = {h:words[:,i] for i,h in enumerate(headers)}
        df = pd.DataFrame(data=data)
        return self(headers, df)

    def write(self, outstar):
        f = open(outstar,'w')
        f.write('# Created {}\n'.format(dt.now()))
        f.write('\n')
        f.write('data_\n\n')
        f.write('loop_\n')
        self.headers = list(self.df)
        for idx, h in enumerate(self.headers):
            f.write(h+' #%s'%(idx+1))
            f.write('\n')
        for i in self.df.index:
            f.write(' '.join(self.df.loc[i]))
            f.write('\n')
        #f.write('\n'.join([' '.join(self.df.loc[i]) for i in range(len(self.df))]))

    def get_particles(self, datadir=None, lazy=False):
        '''
        Return particles of the starfile

        Input:
            datadir (str): Overwrite base directories of particle .mrcs
                Tries both substituting the base path and prepending to the path
            If lazy=True, returns list of LazyImage instances, else np.array
        '''
        particles = self.df['_rlnImageName']

        # format is index@path_to_mrc
        particles = [x.split('@') for x in particles]
        ind = [int(x[0])-1 for x in particles] # convert to 0-based indexing
        mrcs = [x[1] for x in particles]
        if datadir is not None:
            mrcs = prefix_paths(mrcs, datadir)
        for path in set(mrcs):
            assert os.path.exists(path), "%s not found"%path
        D = mrc.parse_header(mrcs[0]).D # image size along one dimension in pixels
        dtype = np.float32
        stride = np.float32().itemsize*D*D
        dataset = [LazyImage(f, (D,D), dtype, 1024+ii*stride) for ii,f in zip(ind, mrcs)]
        if not lazy:
            dataset = np.array([x.get() for x in dataset])
        return dataset

def prefix_paths(mrcs, datadir):
    mrcs1 = ['{}/{}'.format(datadir, os.path.basename(x)) for x in mrcs]
    mrcs2 = ['{}/{}'.format(datadir, x) for x in mrcs]
    try:
        for path in set(mrcs1):
            assert os.path.exists(path)
        mrcs = mrcs1
    except:
        for path in set(mrcs2):
            assert os.path.exists(path), "%s not found"%path
        mrcs = mrcs2
    return mrcs

def csparc_get_particles(csfile, datadir=None, lazy=True):
    metadata = np.load(csfile)
    ind = metadata['blob/idx'] # 0-based indexing
    mrcs = metadata['blob/path'].astype(str).tolist()
    if datadir is not None:
        mrcs = prefix_paths(mrcs, datadir)
    for path in set(mrcs):
        assert os.path.exists(path), "%s not found"%path
    D = metadata[0]['blob/shape'][0]
    dtype = np.float32
    stride = np.float32().itemsize*D*D
    dataset = [LazyImage(f, (D,D), dtype, 1024+ii*stride) for ii,f in zip(ind, mrcs)]
    if not lazy:
        dataset = np.array([x.get() for x in dataset])
    return dataset

########### util #################
def log(msg):
    print('{}     {}'.format(dt.now().strftime('%Y-%m-%d %H:%M:%S'), msg))
    sys.stdout.flush()


    
def print_ctf_params(params):
    assert len(params) == 9
    log('Image size (pix)  : {}'.format(int(params[0])))
    log('A/pix             : {}'.format(params[1]))
    log('DefocusU (A)      : {}'.format(params[2]))
    log('DefocusV (A)      : {}'.format(params[3]))
    log('Dfang (deg)       : {}'.format(params[4]))
    log('voltage (kV)      : {}'.format(params[5]))
    log('cs (mm)           : {}'.format(params[6]))
    log('w                 : {}'.format(params[7]))
    log('Phase shift (deg) : {}'.format(params[8]))
    
def parse_ctf_star(df, D, angpix=None): 
    N = len(df)
    if angpix == None:
        if set(['_rlnDetectorPixelSize','_rlnMagnification']).issubset(df.columns):
            Apix = float(df['_rlnDetectorPixelSize'][0])*10000/float(df['_rlnMagnification'][0]);
        else:
            Apix = 1
    else:
        Apix = angpix
    ctf_params = np.zeros((N, 9))
    ctf_params[:,0] = D
    ctf_params[:,1] = Apix
    
    for i,header in enumerate(['_rlnDefocusU', '_rlnDefocusV', '_rlnDefocusAngle', '_rlnVoltage', '_rlnSphericalAberration', '_rlnAmplitudeContrast', '_rlnPhaseShift']):
        ctf_params[:,i+2] = df[header]
    log('CTF parameters for first particle:')
    print_ctf_params(ctf_params[0])
    return ctf_params
    
def parse_pose_star(df):
    # parse rotations
    N = len(df)
    keys = ('_rlnAngleRot','_rlnAngleTilt','_rlnAnglePsi')
    euler = np.empty((N,3))
    euler[:,0] = df['_rlnAngleRot']
    euler[:,1] = df['_rlnAngleTilt']
    euler[:,2] = df['_rlnAnglePsi']
    log('Euler angles (Rot, Tilt, Psi):')
    log(euler[0])
    log('Converting to rotation matrix:')
    rot = np.asarray([R_from_relion(*x) for x in euler])
    log(rot[0])

    # parse translations
    trans = np.empty((N,2))
    trans[:,0] = df['_rlnOriginX']
    trans[:,1] = df['_rlnOriginY']
    log('Translations:')
    log(trans[0])
    return (euler, trans, rot)

def R_from_relion(a,b,y):
    a *= np.pi/180.
    b *= np.pi/180.
    y *= np.pi/180.
    ca, sa = np.cos(a), np.sin(a)
    cb, sb = np.cos(b), np.sin(b)
    cy, sy = np.cos(y), np.sin(y)
    Ra = np.array([[ca,-sa,0],[sa,ca,0],[0,0,1]])
    Rb = np.array([[cb,0,-sb],[0,1,0],[sb,0,cb]])
    Ry = np.array(([cy,-sy,0],[sy,cy,0],[0,0,1]))
    R = np.dot(np.dot(Ry,Rb),Ra)
    R[0,1] *= -1
    R[1,0] *= -1
    R[1,2] *= -1
    R[2,1] *= -1
    return R
    
def visualise_images(X, n_images, n_columns, randomise=True):
    indices = np.arange(X.shape[0])
    if randomise:
        np.random.shuffle(indices)
    indices = indices[:n_images]
    cmap = plt.cm.Greys_r
    n_rows = np.ceil(n_images / n_columns)
    fig = plt.figure(figsize=(2*n_columns, 2*n_rows))
    fig.subplots_adjust(left=0, right=1, bottom=0, top=1, hspace=0.05, wspace=0.05)

    # plot the digits: each image is 8x8 pixels
    for i, e in enumerate(indices):
        ax = fig.add_subplot(n_rows, n_columns, i + 1, xticks=[], yticks=[])
        ax.imshow(X[e], cmap=cmap, interpolation='nearest')
        
        
def matlab2py(i_matrix):
    tmp = np.swapaxes(i_matrix,0,2)
    return np.swapaxes(tmp,1,2).copy()


def save_mrc(images, filename):
    """Shortcut for writing out MRC files."""
    o = mrcfile.new(filename, overwrite=True)
    o.set_data(images.astype(np.float32))
    o.close()

def cart2pol(x, y):
    """
    Convert Cartesian to Polar Coordinates. All input arguments must be the same shape.
    :param x: x-coordinate in Cartesian space
    :param y: y-coordinate in Cartesian space
    :return: A 2-tuple of values:
        theta: angular coordinate/azimuth
        r: radial distance from origin
    """
    return np.arctan2(y, x), np.hypot(x, y)

def grid_2d(n, shifted=False, normalized=True):
    """
    Generate two dimensional grid.

    :param n: the number of grid points in each dimension.
    :param shifted: shifted by half of grid or not when n is even.
    :param normalized: normalize the grid in the range of (-1, 1) or not.
    :return: the rectangular and polar coordinates of all grid points.
    """
    grid = np.ceil(np.arange(-n/2, n/2))

    if shifted and n % 2 == 0:
        grid = np.arange(-n/2+1/2, n/2+1/2)

    if normalized:
        if shifted and n % 2 == 0:
            grid = grid / (n/2-1/2)
        else:
            grid = grid / (n/2)

    x, y = np.meshgrid(grid, grid, indexing='ij')
    phi, r = cart2pol(x, y)

    return {
        'x': x,
        'y': y,
        'phi': phi,
        'r': r
    }

def estimate_noise(in_matrix):
    ### in_matrix in matlab format
    arr4 = np.swapaxes(in_matrix,0,2)
    arr4 = np.swapaxes(arr4,0,1)
    g2d = grid_2d(in_matrix.shape[1])
    mask = g2d['r'] >= 1

    first_moment = 0
    second_moment = 0

    images_masked = arr4 * np.expand_dims(mask, 2)

    _denominator = in_matrix.shape[0] * np.sum(mask)
    first_moment += np.sum(images_masked) / _denominator
    second_moment += np.sum(np.abs(images_masked**2)) / _denominator
    return second_moment - first_moment**2
    
############ analysis #################
def plot_euler(euler,trans,plot_psi=True,plot_trans=True):
    theta = euler[:,0]
    phi = euler[:,1]
    psi = euler[:,2]
    hexplot = sns.jointplot(theta,phi,kind='hex',
              xlim=(-180,180),
              ylim=(0,180)).set_axis_labels("theta", "phi")
    plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)
    cbar = hexplot.fig.add_axes([.9,.1,.04, .7])
    plt.colorbar(cax=cbar)
    plt.show()
    if plot_psi:
        plt.figure()
        plt.hist(psi)
        plt.xlabel('psi')
    if plot_trans:
        sns.jointplot(trans[:,0],trans[:,1],
              kind='hex').set_axis_labels('tx','ty')

def plot_defocus(ctfs):
    plt.hist(ctfs[:,2])
    plt.xlabel('DefocusU (um)')
    plt.figure()
    plt.hist(ctfs[:,3])
    plt.xlabel('DefocusV (um)')
    
        
def compute_ctf_np(freqs, dfu, dfv, dfang, volt, cs, w, phase_shift=0, bfactor=None):
    '''
    Compute the 2D CTF
   
    Input: 
        freqs (np.ndarray) Nx2 array of 2D spatial frequencies
        dfu (float): DefocusU (Angstrom)
        dfv (float): DefocusV (Angstrom)
        dfang (float): DefocusAngle (degrees)
        volt (float): accelerating voltage (kV)
        cs (float): spherical aberration (mm)
        w (float): amplitude contrast ratio
        phase_shift (float): degrees 
        bfactor (float): envelope fcn B-factor (Angstrom^2)
    '''
    # convert units
    volt = volt * 1000
    cs = cs * 10**7
    dfang = dfang * np.pi / 180
    phase_shift = phase_shift * np.pi / 180
    
    # lam = sqrt(h^2/(2*m*e*Vr)); Vr = V + (e/(2*m*c^2))*V^2
    lam = 12.2639 / np.sqrt(volt + 0.97845e-6 * volt**2)
    x = freqs[:,0]
    y = freqs[:,1]
    ang = np.arctan2(y,x)
    s2 = x**2 + y**2
    df = .5*(dfu + dfv + (dfu-dfv)*np.cos(2*(ang-dfang)))
    gamma = 2*np.pi*(-.5*df*lam*s2 + .25*cs*lam**3*s2**2) - phase_shift
    ctf = np.sqrt(1-w**2)*np.sin(gamma) - w*np.cos(gamma) 
    if bfactor is not None:
        ctf *= np.exp(-bfactor/4*s2)
    return np.require(ctf,dtype=freqs.dtype)

def plot_ctf(ctf_params):
    assert len(ctf_params) == 9
    import matplotlib.pyplot as plt
    import seaborn as sns
    D = int(ctf_params[0])
    Apix = ctf_params[1]
    freqs = np.stack(np.meshgrid(np.linspace(-.5,.5,D,endpoint=False),np.linspace(-.5,.5,D,endpoint=False)),-1)/Apix
    freqs = freqs.reshape(-1,2)
    c = compute_ctf_np(freqs, *ctf_params[2:])
    sns.heatmap(c.reshape(D, D))
    
############ metrics#################

def purity_score(y_true, y_pred):
    # compute contingency matrix (also called confusion matrix)
    contingency_matrix = metrics.cluster.contingency_matrix(y_true, y_pred)
    # return purity
    return np.sum(np.amax(contingency_matrix, axis=0)) / np.sum(contingency_matrix) 

def c_purity_score(y_true, y_pred):
    # compute contingency matrix (also called confusion matrix)
    contingency_matrix = metrics.cluster.contingency_matrix(y_true, y_pred)
    # return purity
    return np.sum(np.amax(contingency_matrix, axis=1)) / np.sum(contingency_matrix) 

