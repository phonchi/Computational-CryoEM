# Computational CryoEM Methods 
[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

This repository is a curated list for computational cryo-EM methods mainly target for single particle analysis!

You will find the paper and associated software for the popular algorithms used in the cryo-EM field.

The format for the item is [software link] - [Paper link] (Available in which package) and the headings may contain a ink to a review paper.



- [**Computational CryoEM Methods**](#computational-cryoEM-methods)
- [**Resources**](#resources)
- [**Workflow**](#workflow)
    - [Motion correction](#motion-correction)
    - [CTF estimation](#ctf-estimation)
    - [Particle picking](#particle-picking)
    - [2D classification](#2D-classification)
    - [Ab-initial Model](#ab-initial-model)
    - [3D refinement](#3d-refinement)
    - [Postprocessing](#postprocessing)
- [**Conventions**](#conventions)
- [**Tips**](#tips)
    - [Format Conversion](#format-conversion)
- [**Contributing**](#contributing)

---


# Resources
## Introduction
* [A quick introduction video for cryo-EM](https://www.youtube.com/watch?v=Qq8DO-4BnIY)
* [Cryo-EM workflow by Nvidia](https://resources.nvidia.com/en-us-drug-discovery/) - Describe the blueprint of cryo-EM using GPU processing.
* [A Primer to Single-Particle Cryo-Electron Microscopy](https://www.sciencedirect.com/science/article/pii/S0092867415003700?via%3Dihub) - A great review to start with.
* [Principles of cryo-EM single-particle image processing](https://pubmed.ncbi.nlm.nih.gov/26705325/) - Highlight the principles when dealing with a cryo-EM dataset.
* [Single-particle cryo-electron microscopy: Mathematical theory, computational challenges, and opportunities](https://web.math.princeton.edu/~amits/publications/IEEE_Signal_Processing_Magazine.pdf) - Review that covers recent updates.
* [Computational Methods for Single-Particle Electron Cryomicroscopy](https://www.annualreviews.org/doi/abs/10.1146/annurev-biodatasci-021020-093826) - A comprehensive review for the mathematical background behind single-particle cryo-EM methods.

## Courses
* [Getting Started in Cryo-EM](http://cryo-em-course.caltech.edu/outline)
* [Electron Microscopy Training by MRC LAB](https://www2.mrc-lmb.cam.ac.uk/research/scientific-training/electron-microscopy/)
* [nysbc training course](http://semc.nysbc.org/the-winter-spring-2018-em-course/)


## Resources
* [3DEM Methods](http://3demmethods.i2pc.es/index.php/Main_Page) - A great wiki that collects papers or books for computational methods.
* [A collective resource](https://github.com/barrykui/awesome-cryoem) - A great repository that covers single particle analysis, model building and tomography.
* [Math behind CryoEM](https://github.com/geoffwoollard/learn_cryoem_math) - A great repository that collects the materials which elaborate the math behind single-particle analysis.
* [Chimera Tutorial](http://embo2015.cryst.bbk.ac.uk/embo2015/course/practicals/prac-7/Practical-7-Maya-Topf-9-Sept-15.pdf)

## Events
* [3DEM Events](http://www.emdatabank.org/3dem_events.html)
* [NRAMM Events](http://nramm.nysbc.org/workshops-and-courses/?lcp_page0=1#lcp_instance_0)

## [Software](http://3dem.ucsd.edu/software.shtm)
* [Scipion](http://scipion.i2pc.es/) - An integrated platform that allows users to use a variety of methods in the same framework.
* [Relion](https://www3.mrc-lmb.cam.ac.uk/relion/index.php?title=Main_Page) - A comprehensive package that utilizes Bayesian approach for 2D classification and 3D refinement.
* [CryoSparc 2](https://cryosparc.com/) - A general package that employs stochastic gradient descent, branch and bound as well as GPU acceleration for rapid reconstructions.
* [Sphire](http://sphire.mpg.de/) - A general package that contains neural network methods for particle picking, denoising and classification.
* [CisTEM](https://cistem.org/) - An easy-to-use framework that implements a complete pipeline for single-particle analysis.
* [EMAN2](https://blake.bcm.edu/emanwiki/EMAN2) - A comprehensive package that contains a python interface and handy scripts for common tasks.
* [SPIDER](https://spider.wadsworth.org/spider_doc/spider/docs/spider.html) - A well-known package that implements image processing methods for electron microscopy.



# Workflow
## Import Data
1. From [EMPIAR](https://www.ebi.ac.uk/pdbe/emdb/empiar/) or [EMDB](https://www.ebi.ac.uk/pdbe/emdb/index.html/).
2. From tutorial data set.


 DataSet (Molecule) | File Size | Movie (#frame) | Micrograph Size (Pixel Size) | Picked Particles (Size) | Final Resolution(A)(Symmetry)
 :--------: | :--------: | :--------: | :--------: | :--------: | :--------: 
 [Scipion](https://github.com/I2PC/scipion/wiki/tutorials/scipion_tutorial_betagal.pdf) <br>  ([Beta-gal](https://drive.google.com/file/d/17e7MCk6-FP3X9Jn9-U-WvWw-L1oY178V/view?usp=sharing]))    | 4.0GB     | 15(16)     |  1950x1950 (3.54)    |  (100x100)    | 7.3 (D2) 
 [Relion 3](ftp://ftp.mrc-lmb.cam.ac.uk/pub/scheres/relion31_tutorial.pdf) <br>  ([Beta-gal](https://www.ebi.ac.uk/pdbe/emdb/empiar/entry/10204/))    | 3.1GB     | 24(24)     |  3710x3838 (0.885)    | (256x256)     |2.9 (D2) 
 [CryoSparc 2](https://cryosparc.com/docs/tutorials/t20s) ([T20S](https://www.ebi.ac.uk/pdbe/emdb/empiar/entry/10025/))    | 8.1GB     | 20(38)     |  7420x7676 (0.6575)    | (440x440)     | 2.93 (D7)
 [CisTEM](https://cistem.org/documentation#tab-1-1) ([ApoFerritin](https://www.ebi.ac.uk/pdbe/emdb/empiar/entry/10146/))    | 5.6GB     | 20(50)     |  1240x1200 (1.5)    |      | 3.0 (O)

3. Generate simulation data
    * [Discrete](Simulation_data.ipynb) 
    * [Continuous](https://github.com/evanseitz/cryoEM_synthetic_continua)


## [Motion correction](https://www.sciencedirect.com/science/article/pii/S0076687916300271?via%3Dihub)

* ### Whole frame alignment
1. [`Unblur`](https://grigoriefflab.umassmed.edu/unblur_summovie) - [**Measuring the optimal exposure for single particle cryo-EM using a 2.6 Å reconstruction of rotavirus VP6**](https://elifesciences.org/articles/06980) ( Use in [`CisTEM`](https://cistem.org/documentation#tab-1-6))
2. `Full-frame motion correction` - (Use in `CryoSparc`)
3. `Optical Flow` - [**Alignment of direct detection device micrographs using a robust Optical Flow approach**](https://www.sciencedirect.com/science/article/pii/S1047847715000313) (Use in [`Xmipp`](http://xmipp.i2pc.es/))


* ### Patch-based/Per-particle based alignment
1. [`MotionCorr2`](https://emcore.ucsf.edu/ucsf-motioncor2) - [**MotionCor2: anisotropic correction of beam-induced motion for improved cryo-electron microscopy**](https://www.nature.com/articles/nmeth.4193?proof=t) (Use in `Relion` and `CryoSparc`)
2. [`Alignparts`](https://sites.google.com/site/rubinsteingroup/direct-detector-align_lmbfgs) - [**Alignment of cryo-EM Movies of Individual Particles by Optimization of Image Translations**](https://pubmed.ncbi.nlm.nih.gov/26296328/) (Use in [`CryoSparc`(local, patch)](https://cryosparc.com/docs/tutorials/patch-motion-ctf))
3. [`Warp`](http://www.warpem.com/warp/?page_id=185) - Contains [Patch-based motion correction](http://www.warpem.com/warp/).
4. `FlexAlign` - [**FlexAlign: An Accurate and Fast Algorithm for Movie Alignment in Cryo-Electron Microscopy**](https://www.mdpi.com/2079-9292/9/6/1040/htm) - (Use in `Scipion`)

* ### [Damage compensation](https://www.sciencedirect.com/science/article/pii/S0076687910810158?via%3Dihub)
    * This functionality is available in most of the motion correction tool
    * The [**dark/gain corrected**](https://pubmed.ncbi.nlm.nih.gov/27572724/) is also conducted in this stage

## [CTF estimation](https://www.sciencedirect.com/science/article/pii/S0076687910820026?via%3Dihub)
* ### Whole frame
1. [`CTFFIND4`](https://grigoriefflab.umassmed.edu/ctffind4) - [**CTFFIND4: Fast and accurate defocus estimation from electron micrographs**](https://www.sciencedirect.com/science/article/pii/S1047847715300460) ( Use in [`CisTEM`](http://grigoriefflab.janelia.org/ctffind4))
2. [`gCTF`](https://www2.mrc-lmb.cam.ac.uk/research/locally-developed-software/zhang-software/#gctf) - [**Gctf: Real-time CTF determination and correction**](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4711343/)
* ### Patch-based/tilt data
1. `Patch-Based CTF Estimation` - [**Real-time cryo-electron microscopy data preprocessing with Warp**](https://www.nature.com/articles/s41592-019-0580-y) ( Use in [`CryoSparc`](https://cryosparc.com/docs/tutorials/patch-motion-ctf), `Warp`)
2. [`goCTF`](https://www.lsi.umich.edu/science/centers-technologies/cryo-electron-microscopy/research/goctf) - [**goCTF: Geometrically optimized CTF determination for single-particle cryo-EM**](https://www.lsi.umich.edu/science/centers-technologies/cryo-electron-microscopy/research/goctf)
3. [`Warp`](http://www.warpem.com/warp/?page_id=185) - Contains Patch-based CTF estimation.

* ### Denoising micrograph
1. [`Restore`](https://github.com/eugenepalovcak/restore) - [**Enhancing SNR and generating contrast for cryo-EM images with convolutional neural networks**](https://www.biorxiv.org/content/10.1101/2020.08.16.253070v1)
2. `Topaz` - [**Topaz-Denoise: general deep denoising models for cryoEM**](https://www.biorxiv.org/content/10.1101/838920v1.full)
3.  [`JANNI`](https://sphire.mpg.de/wiki/doku.php?id=janni) - Just Another Noise 2 Noise Implementation 
4.  `Warp` - Contains methods base on noise2noise and deconvolution filter 


## Particle picking
* ### Semi-supervised picking
1. [`Topaz`](https://github.com/tbepler/topaz) - [**Positive-unlabeled convolutional neural networks for particle picking in cryo-electron micrographs**](https://www.nature.com/articles/s41592-019-0575-8). [[Video]](https://www.youtube.com/watch?v=FnCnsT3GIC4&list=PLFEB3YHuxu11Jp_pOCIEtXxSqozFHve0O&index=10)
2. [`Cryolo`](https://sphire.mpg.de/wiki/doku.php?id=pipeline:window:cryolo) - [**SPHIRE-crYOLO is a fast and accurate fully automated particle picker for cryo-EM**](https://www.nature.com/articles/s42003-019-0437-z). [[Video](https://www.youtube.com/watch?v=JTgldM4wAAk&list=UUbo1TnKiXGtkE_R5b526JmQ&index=6&t=1s&app=desktop)]
4. `Xmipp` - [**A pattern matching approach to the automatic selection of particles from low-contrast electron micrographs**](https://academic.oup.com/bioinformatics/article/29/19/2460/189951)
* ### Template-based picking
1. [`Relion`](https://www.sciencedirect.com/science/article/pii/S1047847714002615), `CryoSparc` - Use 2D class averages or 3D projection for more accurate particle picking
* ### Automatic picking
1. [`DoG`](https://emg.nysbc.org/redmine/projects/software/wiki/DoGpicker) - [**DoG Picker and TiltPicker: software tools to facilitate particle selection in single particle electron microscopy**](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2768396/)
2. `LoG` - [**The Laplacian of Gaussian and Arbitrary Z-Crossings Approach Applied to Automated Single Particle Reconstruction**](https://pubmed.ncbi.nlm.nih.gov/17490891/) (Use in `Relion` auto-picking) 
3. [`APPLE`](https://github.com/PrincetonUniversity/APPLEpicker) - [**APPLE picker: Automatic particle picking, a low-effort cryo-EM framework**](https://www.sciencedirect.com/science/article/pii/S1047847718302326)

* ### Denoising particle and dimenison reduction
1. [`2SDR`](http://sabid.stat.sinica.edu.tw/start) - [**Two-stage dimension reduction for noisy high-dimensional images and application to Cryogenic Electron Microscopy**](https://www.intlpress.com/site/pub/pages/journals/items/amsa/content/vols/0005/0002/a004/index.php)
2. [`CWF`](https://github.com/PrincetonUniversity/cwf_denoise) - [**Denoising and covariance estimation of single particle cryo-EM images**](https://www.sciencedirect.com/science/article/pii/S104784771630082X)
3. [`GAN`](https://github.com/cianfrocco-lab/GAN-for-Cryo-EM-image-denoising) - [**Generative adversarial networks as a tool to recover structural information from cryo-electron microscopy data**](https://www.biorxiv.org/content/10.1101/256792v1.article-info)

## 2D classification

* ### Multirefence alignment based classification
1. `ISAC` - [**Iterative Stable Alignment and Clustering of 2D Transmission Electron Microscope Images**](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3426367/). [[GPU version]](https://sphire.mpg.de/wiki/doku.php?id=gpu_isac)
2. `CL2D` - [**A clustering approach to multireference alignment of single-particle projections in electron microscopy**](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2893300/)

* ### [Maximum-likelihood based classification](https://www.sciencedirect.com/science/article/pii/S0076687910820117?via%3Dihub)
1. `Relion` - Bayesian (Empirical Bayes) approach
2. `CryoSparc` - Bayesian with Branch and bound method
3. `CisTEM` - Maximum likelihood method
* ### Mixed approach classification
1. [`ROME`](http://ipccsb.dfci.harvard.edu/rome/) - [**Massively parallel unsupervised single-particle cryo-EM data clustering via statistical manifold learning**](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0182130)

* ### Automatic selection of 2D classes
1. [`Cryoassess`](https://github.com/cianfrocco-lab/Automatic-cryoEM-preprocessing) -[**High-Throughput Cryo-EM Enabled by User-Free Preprocessing Routines**](https://www.sciencedirect.com/science/article/pii/S0969212620300800?via%3Dihub)
2. [`Cinderella`](https://sphire.mpg.de/wiki/doku.php?id=auto_2d_class_selection) - Cinderella: Deep learning based binary classification tool
* ### New clustering methods
1. [`γ-SUP`](http://sabid.stat.sinica.edu.tw/start) - [γ-SUP: A clustering algorithm for cryo-electron microscopy images of asymmetric particles](https://projecteuclid.org/euclid.aoas/1396966286)
## Ab-initial model 
* ### Class-averages based method
1. [`Simple`](https://simplecryoem.com/)-[**Single-particle cryo-EM-Improved Ab Initio 3D Reconstruction With SIMPLE/PRIME**](https://pubmed.ncbi.nlm.nih.gov/28795512/)
* ### Particles based method
1. `CryoSparc` - [**cryoSPARC: algorithms for rapid unsupervised cryo-EM structure determination**](https://www.nature.com/articles/nmeth.4169). [[Slides]](https://nramm.nysbc.org/wp-content/seminars/2017/slides/nysbc-nov2017-Brubaker.pdf)

## 3D refinement
* ### 3D Homogeneous Refinemnet
1. `Relion` - [**RELION: Implementation of a Bayesian approach to cryo-EM structure determination**](https://www.sciencedirect.com/science/article/pii/S1047847712002481). [[Video]](https://www.youtube.com/watch?time_continue=2&v=TfLFCeehfjM&feature=emb_title)
2. [`CryoSparc`](https://www.nature.com/articles/nmeth.4169) - Use Expectation-Maximization with branch and bound method for higher resolution

* ### 3D classification
1. [`Relion`](http://franklab.cpmc.columbia.edu/franklab/Learning_Materials/Meeting_7_Maximum_Likelihood/Papers/Scheres_2016_MIE_v579.pdf), `CryoSparc`  - Perturb the initial model and use projection matching with weighted assignment

* ### 3D non-uniform Refinemnet
1. `CryoSparc` - [**Non-uniform refinement: Adaptive regularization improves single particle cryo-EM reconstruction**](https://www.nature.com/articles/s41592-020-00990-8)
2. [`SideSplitter`](https://github.com/StructuralBiology-ICLMedicine/SIDESPLITTER) - [**Mitigating Local Over-fitting During Single Particle Reconstruction with SIDESPLITTER**](https://www.sciencedirect.com/science/article/pii/S1047847720301180). [[Video]](https://www.youtube.com/watch?v=jTNH6Z0n254&list=PLFEB3YHuxu11Jp_pOCIEtXxSqozFHve0O&index=12)


* ### [3D variability](http://scripts.iucr.org/cgi-bin/paper?S2053230X18015108)
1. `3DVA` - [**3D Variability Analysis: Directly resolving continuous flexibility and discrete heterogeneity from single particle cryo-EM images**](https://www.biorxiv.org/content/10.1101/2020.04.08.032466v1) ( Use in `CryoSparc`)
2. [`CryoDRGN`](https://github.com/zhonge/cryodrgn) - [**CryoDRGN: Reconstruction of heterogeneous structures from cryo-electron micrographs using neural networks**](https://www.biorxiv.org/content/10.1101/2020.03.27.003871v1)
3. [`ManifoldEM`](https://github.com/GMashayekhi/ManifoldEM_Matlab) - [**Retrieving functional pathways of biomolecules from single-particle snapshots**](https://www.nature.com/articles/s41467-020-18403-x)
4. [`AlphaCryo4D`](https://github.com/AlphaCryo4D/AlphaCryo4D) - [**Deep manifold learning reveals hidden dynamics of proteasome autoregulation**](https://arxiv.org/abs/2012.12854)

* ### [Focus classifcation](https://www.frontiersin.org/articles/10.3389/fmolb.2019.00033/full)
1. [`localrec`](https://github.com/OPIC-Oxford/localrec) - [**Localized reconstruction of subunits from electron cryomicroscopy images of macromolecular complexes**](https://www.nature.com/articles/ncomms9843) (Use in `Scipion`)
2. `Multi-body refinement` - [**Characterisation of molecular motions in cryo-EM single-particle data by multi-body refinement in RELION**](https://elifesciences.org/articles/36861) (Use in `Relion`)


## [Postprocessing](https://www.sciencedirect.com/science/article/pii/S0079610720300699)
* ### Per-particle based motion and ctf refinement
1. `CTF refinement` - [`Relion3`](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6250425/)/[`CisTEM`](https://cistem.org/documentation#tab-1-12)/[`CryoSparc`](https://cryosparc.com/docs/tutorials/ctf-refinement), 3D Reference required
2. `Ewald sphere correction` - [`Relion3`](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6250425/) (Use ` relion_reconstruct --reverse_curvature`)
3.  `High-order aberrations` - [**Estimation of high-order aberrations and anisotropic magnification from cryo-EM data sets in RELION-3.1**](https://journals.iucr.org/m/issues/2020/02/00/fq5009/index.html)
4. `Bayesian Polishing` - [**A Bayesian approach to beam-induced motion correction in cryo-EM single-particle analysis**](https://journals.iucr.org/m/issues/2019/01/00/fq5003/)  (Use in Relion, 3D Reference required)
5. [`M`](http://www.warpem.com/warp/?page_id=827) - [**Multi-particle cryo-EM refinement with M visualizes ribosome-antibiotic complex at 3.7 Å inside cells**](https://www.biorxiv.org/content/10.1101/2020.06.05.136341v1)  (For both movie data and tilted data). [[Video]](https://www.youtube.com/watch?v=kiS-ELvQ1gc&list=PLFEB3YHuxu11Jp_pOCIEtXxSqozFHve0O&index=18)

* ### [Local resolution](https://www.sciencedirect.com/science/article/pii/S0959440X20301044) and directional resolution
1. [`blocres`](https://lsbr.niams.nih.gov/bsoft/programs/blocres.html) - [**One number does not fit all: Mapping local variations in resolution in cryo-EM reconstructions**](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3837392/)
1. [`ResMap`](https://sourceforge.net/projects/resmap-latest/) - [**Quantifying the Local Resolution of Cryo-EM Density Maps**](https://www.nature.com/articles/nmeth.2727)
2. `MonoRes` - [**MonoRes: Automatic and Accurate Estimation of Local Resolution for Electron Microscopy Maps**](https://pubmed.ncbi.nlm.nih.gov/29395788/) (Use in `Scipion`)
3. [`3DFSC`](https://github.com/nysbc/Anisotropy) - [**Addressing preferred specimen orientation in single-particle cryo-EM through tilting**](https://www.nature.com/articles/nmeth.4347)
4. `MonoDir` - [**Measuring local-directional resolution and local anisotropy in cryo-EM maps**](https://www.nature.com/articles/s41467-019-13742-w) (Use in `Scipion`)

* ### [Sharpening](https://www.sciencedirect.com/science/article/pii/S0022283603010222) and local filtering to enhance [interpretability](https://www.sciencedirect.com/science/article/pii/S0079610720300699)
1. [`Confidence Maps`](https://git.embl.de/mbeckers/FDRthresholding/-/tree/master) - [**Thresholding of cryo-EM density maps by false discovery rate control**](https://journals.iucr.org/m/issues/2019/01/00/pw5002/index.html) (Use in [`ccpem`](https://www.ccpem.ac.uk/download.php))
2. [`DeepEnhancer`](https://github.com/rsanchezgarc/deepEMhancer)-[**DeepEMhancer: a deep learning solution for cryo-EM volume post-processing**](https://www.biorxiv.org/content/10.1101/2020.06.12.148296v3)
3. [`LocScale`](https://git.embl.de/jakobi/LocScale)[**Model-based local density sharpening of cryo-EM maps**](https://elifesciences.org/articles/27131) (Use in [`ccpem`](https://www.ccpem.ac.uk/download.php))
4. [`LocalDeblur`](https://github.com/I2PC/scipion-em-xmipp/wiki/XmippProtLocSharp) - [**Automatic local resolution-based sharpening of cryo-EM maps**](https://academic.oup.com/bioinformatics/article/36/3/765/5554698)

* ### Denoising 3D volume
1. [`Warp`](http://www.warpem.com/warp/?page_id=389) - Based on Noise2Noise
2. `Topaz` - Contains 3D denoise functionality
3. [`Relion`](https://github.com/3dem/externprior) - [**Exploiting prior knowledge about biological macromolecules in cryo-EM structure determination**](https://www.biorxiv.org/content/10.1101/2020.03.25.007914v1)

## Visualization
1. [`Chimera`](https://www.cgl.ucsf.edu/chimera/) - [**UCSF Chimera--a Visualization System for Exploratory Research and Analysis**](https://pubmed.ncbi.nlm.nih.gov/15264254/)
2. [`ChimeraX`](http://www.rbvi.ucsf.edu/chimerax/) - [**UCSF ChimeraX: Meeting modern challenges in visualization and analysis**](https://onlinelibrary.wiley.com/doi/full/10.1002/pro.3235)

# Conventions
## 3DEM Convention
* [3DEM Conventions](https://github.com/azazellochg/3DEM-conventions)
* [Resolution Measure](https://www.sciencedirect.com/science/article/pii/S0079610716300037)

## Image contrast
`White on Black` - Relion, Xmipp, EMAN2, CryoSparc (Cryo-EM data is typically recorded as Black on White but will invert during processing)

`Black on White` - Frealign (CisTEM)

## Pixel size
For the format defined in RELION, the actual pixel size is calculated as `rlnDetectorPixelSize * 10000 / rlnMagnification`


## FSC calculation
Using [e2proc3d](http://sphire.mpg.de/wiki/doku.php?id=pipeline:utilities:e2proc3d)

## Mask generation in [CryoSparc](https://discuss.cryosparc.com/t/tight-corrected-and-loose-gsfsc-curves/201/5)

### No Mask:
This is the raw FSC calculated between two independent half-maps reconstructed from the data. There is no masking applied, so both the structure and solvent are included in this FSC.

### Spherical:
This is the FSC calculated after applying a soft spherical mask to both half maps. The outer radius of the soft sphere is equal to half the volume box-size (i.e. the sphere extends to the faces of the box in all directions). The inner radius is 85 percent of the outer radius. Between inner and outer radii, a soft cosine edge transitions from a mask value of one to a value of zero.

### Loose:
This is the FSC calculated after applying a soft solvent mask to both half maps. The loose mask is calculated as follows. First, the density map is thresholded at 50% of the maximum density value. The resulting volume is dilated to create a soft mask. Voxels in the mask that are within 25 angstroms of the thresholded region receive a mask value of 1.0. Voxels between 25 and 40 angstroms fall off with a soft cosine edge, and voxels outside 40 angstroms receive a value of 0.0.

### Tight:
This is the same as the loose mask, except the dilation distances are 6 angstroms for the value 1.0 distance and 12 angstroms for the value 0.0 distance.

### Corrected:
This is the FSC curve calculated using the tight mask with correction by noise substitution [1]. The two half maps have their phases randomized beyond a certain resolution, then the tight mask is applied to both, and an FSC is calculated. This FSC is used along with the original FSC before phase randomization to compute the corrected FSC as in [1]. This accounts for correlation effects induced by masking. The resolution at which phase randomization begins is the resolution at which the no-mask FSC drops below the FSC = 0.143 criteria.

> Chen, S. et al. High-resolution noise substitution to measure overfitting and validate resolution in 3D structure determination by single particle electron cryomicroscopy. Ultramicroscopy 135, 24–35 (2013).

## Sharpen and filtering in [CryoSparc](https://discuss.cryosparc.com/t/how-is-the-non-uniform-refinement-map-filtered-map-created/4388)
The `map_filtered` output in non-uniform refinement is generated as follows, after refinement has converged:

1. both raw, unfiltered halfmaps are averaged together
2. the raw map is filtered using the Gold-Standard FSC curve
3. the filtered map is sharpened using the Guinier-plot estimated b-factor
4. the sharpened map is outputted as `_map_sharp_local.mrc` (confusing filename… sorry)
5. the sharpened map is locally filtered using a local resolution estimate computed from the half-maps and the locally filtered map is outputted as `_map_filtered.mrc`


# Tips
## Format Conversion
1. Using [PyRelion](https://github.com/OPIC-Oxford/localrec/wiki/Tips-and-tricks)
Operate Star files

2. Using [PyEM](https://github.com/asarnow/pyem)
Convert metadata

3. Using [EMAN2](https://blake.bcm.edu/emanwiki/EMAN2)
Convert binary data

4. Using [SPHIRE](http://sphire.mpg.de/)
Convert binary data

## Parse `Star file`
1. Using [`StarTool`](https://github.com/cdienem/StarTool)
2. Using Custom function like [here](Parse_Star.ipynb)

## Parse `CryoSparc file`
1. Using [`PyEM`](https://github.com/asarnow/pyem)
2. Using Custom function like [here](Parse_CryoSparc.ipynb). See full tutorial [here](https://guide.cryosparc.com/processing-data/manipulating-.cs-files-created-by-cryosparc) 

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

### [Local classification in CryoSparc](https://cryosparc.com/blog/local-refinement-snRNP-case-study/)

## Display images
### Micrographs
In Matlab use `grayImage = uint8(255 * mat2gray(originalImage)); imshow(grayImage);`

## Chimera
### [Dispaly local resolution](https://discuss.cryosparc.com/t/view-coloured-3d-map-in-chimera-using-output-from-local-resolution/1003)
### [Flip handedness of model and map](https://github.com/asarnow/pyem/wiki/Z-Flip-for-Models-and-Maps)
### Slice view
`volume #0 planes z,220 step 1 level -1 style surface`

# Contributing
Your contributions are highly appreciated! Please take a look at the [contribution guidelines](https://github.com/phonchi/Computational-CryoEM/blob/master/CONTRIBUTING.md) first.
