# Computational CryoEM Methods

This is a curated list for computational cryo-EM method mainly target for single particle analysis!

- [Computational CryoEM Methods](#computational-cryoEM-methods)
- [Resources](#resources)
- [Conventions](#conventions)
- [Tips](#tips)

---


# Resources
## Courses
* [Getting Started in Cryo-EM](http://cryo-em-course.caltech.edu/outline)
* [Electron Microscopy Training by MRC LAB](https://www2.mrc-lmb.cam.ac.uk/research/scientific-training/electron-microscopy/)
* [nysbc training course](http://semc.nysbc.org/the-winter-spring-2018-em-course/)

## Resources
* [3DEM Methods](http://3demmethods.i2pc.es/index.php/Main_Page)
* [A collective resource](https://github.com/barrykui/awesome-cryoem)
* [3DEM Conventions](https://github.com/azazellochg/3DEM-conventions)
* [Chimera Tutorial](http://embo2015.cryst.bbk.ac.uk/embo2015/course/practicals/prac-7/Practical-7-Maya-Topf-9-Sept-15.pdf)

## Events
* [3DEM Events](http://www.emdatabank.org/3dem_events.html)
* [NRAMM Events](http://nramm.nysbc.org/workshops-and-courses/?lcp_page0=1#lcp_instance_0)

## Software
* [Scipion](http://scipion.i2pc.es/)
* [Relion](https://www3.mrc-lmb.cam.ac.uk/relion/index.php?title=Main_Page)
* [CryoSparc 2](https://cryosparc.com/)
* [Sphire](http://sphire.mpg.de/)
* [CisTEM](https://cistem.org/)
* [EMAN2](https://blake.bcm.edu/emanwiki/EMAN2)
* [SPIDER](https://spider.wadsworth.org/spider_doc/spider/docs/spider.html)



# Workflow
## Import Data
1. From EMPIAR (https://www.ebi.ac.uk/pdbe/emdb/empiar/)
2. From tutorial data set


 DataSet (Molecule) | File Size | Movie (#frame) | Micrograph Size (Pixel Size) | Picked Particles (Size) | Final Resolution(A)(Symmetry)
 :--------: | :--------: | :--------: | :--------: | :--------: | :--------: 
 [Scipion](https://github.com/I2PC/scipion/wiki/tutorials/scipion_tutorial_betagal.pdf) <br>  ([Beta-gal](https://drive.google.com/file/d/17e7MCk6-FP3X9Jn9-U-WvWw-L1oY178V/view?usp=sharing]))    | 4.0GB     | 15(16)     |  1950x1950 (3.54)    |  (100x100)    | 7.3 (D2) 
 [Relion 3](ftp://ftp.mrc-lmb.cam.ac.uk/pub/scheres/relion31_tutorial.pdf) <br>  ([Beta-gal](https://www.ebi.ac.uk/pdbe/emdb/empiar/entry/10204/))    | 3.1GB     | 24(24)     |  3710x3838 (0.885)    | (256x256)     |2.9 (D2) 
 [CryoSparc 2](https://cryosparc.com/docs/tutorials/t20s) ([T20S](https://www.ebi.ac.uk/pdbe/emdb/empiar/entry/10025/))    | 8.1GB     | 20(38)     |  7420x7676 (0.6575)    | (440x440)     | 2.93 (D7)
 [CisTEM](https://cistem.org/documentation#tab-1-1) ([ApoFerritin](https://www.ebi.ac.uk/pdbe/emdb/empiar/entry/10146/))    | 5.6GB     | 20(50)     |  1240x1200 (1.5)    |      | 3.0 (O)

3. Simulate Data
    * [Continuous](https://github.com/evanseitz/cryoEM_synthetic_continua)


## Motion correction
### Whole Frame Alignment
1. [`MotionCorr2`](https://emcore.ucsf.edu/ucsf-motioncor2) - [**MotionCor2: anisotropic correction of beam-induced motion for improved cryo-electron microscopy**](https://www.nature.com/articles/nmeth.4193?proof=t) (Use in `Relion`, `CryoSparc` and [`Warp`](http://www.warpem.com/warp/))
2. [`Unblur`](https://grigoriefflab.umassmed.edu/unblur_summovie) - [**Measuring the optimal exposure for single particle cryo-EM using a 2.6 Å reconstruction of rotavirus VP6**](https://elifesciences.org/articles/06980) ( Use in [`CisTEM`](https://cistem.org/documentation#tab-1-6))
3. `Full-frame motion correction` - (Use in `CryoSparc`)
4. `Optical Flow` - [**Alignment of direct detection device micrographs using a robust Optical Flow approach**](https://www.sciencedirect.com/science/article/pii/S1047847715000313) (Use in [`Xmipp`](http://xmipp.i2pc.es/))
### Per-particle based alignment
1. [`Alignparts`](https://sites.google.com/site/rubinsteingroup/direct-detector-align_lmbfgs) - [**Alignment of cryo-EM Movies of Individual Particles by Optimization of Image Translations**](https://pubmed.ncbi.nlm.nih.gov/26296328/) (Use in [`CryoSparc`(local, patch)](https://cryosparc.com/docs/tutorials/patch-motion-ctf))


## CTF estimation
### Whole frame
1. [`CTFFIND4`](https://grigoriefflab.umassmed.edu/ctffind4) - [**CTFFIND4: Fast and accurate defocus estimation from electron micrographs**](https://www.sciencedirect.com/science/article/pii/S1047847715300460) ( Use in [`CisTEM`](http://grigoriefflab.janelia.org/ctffind4))
2. [`gCTF`](https://www2.mrc-lmb.cam.ac.uk/research/locally-developed-software/zhang-software/#gctf) - [**Gctf: Real-time CTF determination and correction**](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4711343/)
### Patch-based/tilt data
1. `Patch-Based CTF Estimation` - [**Real-time cryo-electron microscopy data preprocessing with Warp**](https://www.nature.com/articles/s41592-019-0580-y) ( Use in [`CryoSparc`](https://cryosparc.com/docs/tutorials/patch-motion-ctf), `Warp`)
2. [`goCTF`](https://www.lsi.umich.edu/science/centers-technologies/cryo-electron-microscopy/research/goctf) - [**goCTF: Geometrically optimized CTF determination for single-particle cryo-EM**](https://www.lsi.umich.edu/science/centers-technologies/cryo-electron-microscopy/research/goctf)

### Denoising micrograph
1. `Topaz` - [**Topaz-Denoise: general deep denoising models for cryoEM**](https://www.biorxiv.org/content/10.1101/838920v1.full)
2.  [`JANNI`](https://sphire.mpg.de/wiki/doku.php?id=janni) - Just Another Noise 2 Noise Implementation 
3.  `Warp`

## Particle-picking
### Semi-superviesd
1. [`Topaz`](https://github.com/tbepler/topaz) - [**Positive-unlabeled convolutional neural networks for particle picking in cryo-electron micrographs**](https://www.nature.com/articles/s41592-019-0575-8)
2. [`Cryolo`](https://sphire.mpg.de/wiki/doku.php?id=pipeline:window:cryolo) - [**SPHIRE-crYOLO is a fast and accurate fully automated particle picker for cryo-EM**](https://www.nature.com/articles/s42003-019-0437-z)
### Template-based
1. `Relion`, `CryoSparc`
### Automatic
1. [`DoG`](https://emg.nysbc.org/redmine/projects/software/wiki/DoGpicker) - [**DoG Picker and TiltPicker: software tools to facilitate particle selection in single particle electron microscopy**](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2768396/)
2. [`APPLE`](https://github.com/PrincetonUniversity/APPLEpicker) - [**APPLE picker: Automatic particle picking, a low-effort cryo-EM framework**](https://www.sciencedirect.com/science/article/pii/S1047847718302326)

## Denoising patricle and dimenison reduction
1. `2SDR` - [**Two-stage dimension reduction for noisy high-dimensional images and application to Cryogenic Electron Microscopy**](https://arxiv.org/abs/1911.09816)
2. [`CWF`](https://github.com/PrincetonUniversity/cwf_denoise) - [**Denoising and covariance estimation of single particle cryo-EM images**](https://www.sciencedirect.com/science/article/pii/S104784771630082X)
3. [`GAN`](https://github.com/cianfrocco-lab/GAN-for-Cryo-EM-image-denoising) - [**Generative adversarial networks as a tool to recover structural information from cryo-electron microscopy data**](https://www.biorxiv.org/content/10.1101/256792v1.article-info)

## 2D classification

### MRA-based
1. `ISAC` - [**Iterative Stable Alignment and Clustering of 2D Transmission Electron Microscope Images**](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3426367/)
2. `CL2D` - [**A clustering approach to multireference alignment of single-particle projections in electron microscopy**](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2893300/)

### Maximum-likelihood
1. `Relion` - Bayesian
2. `CryoSparc` - Bayesian with Branch and bound
3. `CisTEM` - Maximum likelihood
### Mixed
1. [`ROME`](http://ipccsb.dfci.harvard.edu/rome/) - [**Massively parallel unsupervised single-particle cryo-EM data clustering via statistical manifold learning**](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0182130)

### Automatic select 2D class
1. [`Cinderella`](https://sphire.mpg.de/wiki/doku.php?id=auto_2d_class_selection) - Cinderella: Deep learning based binary classification tool

## Ab-initial Model 
### Using class-averages
1. [`Simple`](https://simplecryoem.com/)-[**Single-particle cryo-EM-Improved Ab Initio 3D Reconstruction With SIMPLE/PRIME**](https://pubmed.ncbi.nlm.nih.gov/28795512/)
### Using particles
1. `CryoSparc` - [**cryoSPARC: algorithms for rapid unsupervised cryo-EM structure determination**](https://www.nature.com/articles/nmeth.4169)

## 3D Refinement
### 3D Homogeneous Refinemnet
1. `Relion` - [**RELION: Implementation of a Bayesian approach to cryo-EM structure determination**](https://www.sciencedirect.com/science/article/pii/S1047847712002481)
2. [`CryoSparc`](https://www.nature.com/articles/nmeth.4169)

### 3D non-uniform Refinemnet
1. `CryoSparc` - [**Non-uniform refinement: Adaptive regularization improves single particle cryo-EM reconstruction**](https://www.biorxiv.org/content/10.1101/2019.12.15.877092v1)
2. [`SideSplitter`](https://github.com/StructuralBiology-ICLMedicine/SIDESPLITTER) - [**Mitigating Local Over-fitting During Single Particle Reconstruction with SIDESPLITTER**](https://www.biorxiv.org/content/10.1101/2019.12.12.874081v2)


### 3D classification
1. [`Relion`](http://franklab.cpmc.columbia.edu/franklab/Learning_Materials/Meeting_7_Maximum_Likelihood/Papers/Scheres_2016_MIE_v579.pdf)
2. `CryoSparc`

### 3D variability
1. `3DVA` - [**3D Variability Analysis: Directly resolving continuous flexibility and discrete heterogeneity from single particle cryo-EM images**](https://www.biorxiv.org/content/10.1101/2020.04.08.032466v1) ( Use in `CryoSparc`)
2. [`CryoDRGN`](https://github.com/zhonge/cryodrgn) - [**CryoDRGN: Reconstruction of heterogeneous structures from cryo-electron micrographs using neural networks**](https://www.biorxiv.org/content/10.1101/2020.03.27.003871v1)

## Postprocessing
1. `CTF refinement` - ([`Relion3`](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6250425/)/[`CisTEM`](https://cistem.org/documentation#tab-1-12), 3D Reference required)
2. `Bayesian Polishing` - [**A Bayesian approach to beam-induced motion correction in cryo-EM single-particle analysis**](https://journals.iucr.org/m/issues/2019/01/00/fq5003/)  ( Use in Relion, 3D Reference required)
3. [`M`](http://www.warpem.com/warp/?page_id=827) - [**Multi-particle cryo-EM refinement with M visualizes ribosome-antibiotic complex at 3.7 Å inside cells**](https://www.biorxiv.org/content/10.1101/2020.06.05.136341v1)  (For both movie data and tilted data)

### Denoising 3D volume
1. [`Warp`](http://www.warpem.com/warp/?page_id=389) - Based on Noise2Noise
2. `Topaz`
3. [`Relion`](https://github.com/3dem/externprior) - [**Exploiting prior knowledge about biological macromolecules in cryo-EM structure determination**](https://www.biorxiv.org/content/10.1101/2020.03.25.007914v1)

# Conventions
## Contrast
`White on Black` - Relion, Xmipp, EMAN2, CryoSparc (Cryo-EM data is typically recorded as Black on White but will invert during processing)

`Black on White` - Frealign (CisTEM)

## Pixel size
For the format define in RELION the actual pixel size is `rlnDetectorPixelSize * 10000 / rlnMagnification`

## 3DEM Convention
* [3DEM Conventions](https://github.com/azazellochg/3DEM-conventions)

## Calculate FSC manually
Using [e2proc3d](http://sphire.mpg.de/wiki/doku.php?id=pipeline:utilities:e2proc3d)

## Mask takes [CryoSparc](https://discuss.cryosparc.com/t/tight-corrected-and-loose-gsfsc-curves/201/5) for example

### No Mask:
This is the raw FSC calculated between two independent half-maps reconstructed from the data. There is no masking applied, so both the structure and solvent are included in this FSC.

### Spherical:
This is the FSC calculated after applying a soft spherical mask to both half maps. The outer radius of the soft sphere is equal to half the volume box-size (i.e. the sphere extends to the faces of the box in all directions). The inner radius is 85 percent of the outer radius. Between inner and outer radii, a soft cosine edge transitions from a mask value of one to a value of zero.

### Loose:
This is the FSC calculated after applying a soft solvent mask to both half maps. The loose mask is calculated as follows. First, the density map is thresholded at 50% of the maximum density value. The resulting volume is dilated to create a soft mask. Voxels in the mask that are within 25 angstroms of the thresholded region receive a mask value of 1.0. Voxels between 25 and 40 angstroms fall off with a soft cosine edge, and voxels outside 40 angstroms receive a value of 0.0.

### Tight:
This is the same as the loose mask, except the dilation distances are 6 angstroms for the value 1.0 distance and 12 angstroms for the value 0.0 distance.

### Corrected:
This is the FSC curve calculated using the tight mask with correction by noise substitution [1]. The two half maps have their phases randomized beyond a certain resolution, then the tight mask is applied to both, and an FSC is calculated. This FSC is used along with the original FSC before phase randomization to compute the corrected FSC as in [1]. This accounts for correlation effects induced by masking. The resolution at which phase randomization begins is the resolution at which the no-mask FSC drops below the FSC = 0.143 criterion.

> Chen, S. et al. High-resolution noise substitution to measure overfitting and validate resolution in 3D structure determination by single particle electron cryomicroscopy. Ultramicroscopy 135, 24–35 (2013).

# Tips
## Format Conversion
### Using [PyRelion](https://github.com/OPIC-Oxford/localrec/wiki/Tips-and-tricks)
Operate Star files

### Using [PyEM](https://github.com/asarnow/pyem)
Convert metadata

### Using [EMAN2](https://blake.bcm.edu/emanwiki/EMAN2)
Convert binary data

### Using [SPHIRE](http://sphire.mpg.de/)
Convert binary data

## Performing Focus Classification
### Using Chimera
### [CisTEM](https://cistem.org/frequently-asked-questions#tab-1-4)
A focus mask is defined as a sphere specified by radius and x,y,z coordinates of the sphere center, all given in Å. In order to find x,y,z, in CisTEM
1. Open the 3D map in Chimera. The map should be assigned model #0.
1. Display the command line by selecting Tools > General Controls > Command Line.
1. Execute vop threshold #0 maximum -1000 setMaximum 1.0 (this assumes that the minimum voxel value in the 3D map is larger than 1000). This will create a new model #1.
1. Execute shape sphere radius 30 color red mesh true on the Command Line. This will generate a sphere with a 30 Å radius, numbered model #2 (change the radius as needed).
1. Open Tools > General Controls > Model Panel and deactivate models #0 and #1. Then move the sphere (model #2) into model #1 until it is fully contained in that volume.
1. Execute mask #1 #2 on the Command Line. This will generate a new model #3 of a solid sphere with a 30 Å radius.
1. Close models #1 and #2 in Model Panel and make sure model #0 is visible but deactive.
1. Select model #3 (the solid sphere) in Volume Viewer and change its color to red (or something easily distiguishable from the original 3D map) and make it transparent.
1. Move model #3 to the desired location of the focus mask in the 3D map.
1. Execute vop resample #3 onGrid #0 on the Command Line. This will generate a copy of the solid sphere as a new model #1, now resampled in the same coordinate system as the original 3D map.
1. Execute measure center #1 on the Command Line. This will display the x,y,z coordinates of the mask in pixel coordinates below the command line. These coordinates have to be converted to Å by multiplying them with the pixel size of the 3D map before they can be used in cisTEM's Manual Refine panel.

### [CryoSparc](https://cryosparc.com/blog/local-refinement-snRNP-case-study/)

## Display images
### Micrographs
In Matlab use `grayImage = uint8(255 * mat2gray(originalImage)); imshow(grayImage);`
