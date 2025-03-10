# Computational CryoEM Methods 
[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

<div align="center">
    <img src="https://github.com/phonchi/Computational-CryoEM/assets/11373055/e55eab92-2dfb-4c80-b49c-400951aa5124" width="300">
</div>


This repository is a curated list of computational cryo-EM methods mainly targeted for single particle analysis! If you are looking for computational methods for cryo-ET, see [here](https://github.com/phonchi/Computational-CryoET).

You will find the paper and associated software for the popular algorithms used in the cryo-EM field.

The format for the item is [software link] - [Paper link] (Available in which package) and the headings may contain a link to a review paper.



- [**Computational CryoEM Methods**](#computational-cryoEM-methods)
- [**Resources**](#resources)
- [**Workflow**](#workflow)
    - [Motion correction](#motion-correction)
    - [CTF estimation](#ctf-estimation)
    - [Particle picking](#particle-picking)
    - [2D classification](#2D-classification)
    - [Ab-initial Model](#ab-initial-model)
    - [3D refinement](#3d-refinement)
    - [3D variability analysis](#3D-variability-analysis)
    - [Postprocessing](#postprocessing)
    - [Model Building](#model-building)
- [**Conventions**](#conventions)
- [**Tips**](#tips)
    - [Format Conversion](#format-conversion)
    - [Performing Focus Classification](#performing-focus-classification)
    - [Display images](#display-images)
    - [Using Chimera](#using-chimera)
- [**Contributing**](#contributing)

---


# Resources
## Preface
* [Protein Folding Problem](https://www.youtube.com/watch?v=KpedmJdrTpY&t=2s&ab_channel=DeepMind) - Great video describes the importance of understanding protein structure.
* [What is cryoEM](https://www.youtube.com/watch?v=Qq8DO-4BnIY&ab_channel=UCSanFrancisco%28UCSF%29) - Great video that describes how cryoEM can help us understand the protein structure.

## Introduction
* [A quick introduction video for cryo-EM](https://www.youtube.com/watch?v=Qq8DO-4BnIY)
* [Cryo-EM 101](https://cryoem101.org/) - Deomnstrate the principles of cryo-EM using a media-rich approach with videos, animations, interactive simulation.
* [cryoEDU](https://cryoedu.org/) - A hands-on cryo-EM education tool
* [Cryo-EM workflow by Nvidia](https://resources.nvidia.com/en-us-drug-discovery/) - Describe the blueprint of cryo-EM using GPU processing.
* [A Primer to Single-Particle Cryo-Electron Microscopy](https://www.sciencedirect.com/science/article/pii/S0092867415003700?via%3Dihub) - A great review to start with.
* [Principles of cryo-EM single-particle image processing](https://pubmed.ncbi.nlm.nih.gov/26705325/) - Highlight the principles when dealing with a cryo-EM dataset.
* [Single-particle cryo-electron microscopy: Mathematical theory, computational challenges, and opportunities](https://web.math.princeton.edu/~amits/publications/IEEE_Signal_Processing_Magazine.pdf) - Review that covers recent updates.
* [Computational Methods for Single-Particle Electron Cryomicroscopy](https://www.annualreviews.org/doi/abs/10.1146/annurev-biodatasci-021020-093826) - A comprehensive review for the mathematical background behind single-particle cryo-EM methods.
* [Cryo-EM: Breakthroughs in Chemistry, Structural Biology, and Statistical Underpinnings](https://statistics.stanford.edu/technical-reports/cryo-em-breakthroughs-chemistry-structural-biology-and-statistical-underpinnings) - Review that covers statistical problems behind cryo-EM.

## Courses
* [Cryo-EM Principles](https://cryoemprinciples.yale.edu/)
* [Getting Started in Cryo-EM](http://cryo-em-course.caltech.edu/overview)
* [Electron Microscopy Training by MRC LAB](https://www2.mrc-lmb.cam.ac.uk/research/scientific-training/electron-microscopy/)
* [nysbc training course](https://semc.nysbc.org/workshops/past-courses/2023-em-course/)


## Resources
* [3DEM Methods](http://3demmethods.i2pc.es/index.php/Main_Page) - A great wiki that collects papers or books for computational methods.
* [A collective resource](https://github.com/barrykui/awesome-cryoem) - A great repository that covers single particle analysis, model building and tomography.
* [Math behind CryoEM](https://github.com/geoffwoollard/learn_cryoem_math) - A great repository that collects the materials which elaborate the math behind single-particle analysis.
* [Chimera Tutorial](http://embo2015.cryst.bbk.ac.uk/embo2015/course/practicals/prac-7/Practical-7-Maya-Topf-9-Sept-15.pdf)

## Events and News
* [CryoEM and AI reveal a structure of SARS-CoV-2 Nsp2, a multifunctional protein involved in key host processes](https://www.biorxiv.org/content/10.1101/2021.05.10.443524v1)
* [3DEM Events](http://www.emdatabank.org/3dem_events.html)
* [NRAMM Events](http://nramm.nysbc.org/workshops-and-courses/?lcp_page0=1#lcp_instance_0)

## [Software](http://3dem.ucsd.edu/software.shtm)
* [Scipion](http://scipion.i2pc.es/) - An integrated platform that allows users to use a variety of methods in the same framework. [[Documentation](https://scipion-em.github.io/docs/)]
* [Relion](https://www3.mrc-lmb.cam.ac.uk/relion/index.php?title=Main_Page) - A comprehensive package that utilizes Bayesian approach for 2D classification and 3D refinement. [[Documentation](https://relion.readthedocs.io/en/latest/)]
* [CryoSPARC 2](https://cryosparc.com/) - A general package that employs stochastic gradient descent, branch and bound as well as GPU acceleration for rapid reconstructions. [[CryoSPARC Tools](https://tools.cryosparc.com/intro.html)]
* [Sphire](http://sphire.mpg.de/) - A general package that contains neural network methods for particle picking, denoising and classification.
* [CisTEM](https://github.com/timothygrant80/cisTEM) - An easy-to-use framework that implements a complete pipeline for single-particle analysis.
* [EMAN2](https://blake.bcm.edu/emanwiki/EMAN2) - A comprehensive package that contains a python interface and handy scripts for common tasks.
* [SPIDER](https://github.com/spider-em/SPIDER) - A well-known package that implements image processing methods for electron microscopy.
* [ASPIRE](http://spr.math.princeton.edu/) - A software that uses algorithms based on rigorous mathematical theory. 



# Workflow
## Import Data
1. From [EMPIAR](https://www.ebi.ac.uk/pdbe/emdb/empiar/) or [EMDB](https://www.ebi.ac.uk/pdbe/emdb/index.html/).

 DataSet (Molecule) | File Size | Movie (#frame) | Micrograph Size (Pixel Size) | Picked Particles (Size) | Final Resolution(A)(Symmetry)| Notes
 :--------: | :--------: | :--------: | :--------: | :--------: | :--------: | :--------:
 [70S ribosome](https://www3.mrc-lmb.cam.ac.uk/relion/index.php?title=Classification_example)  | 0.7GB     | N/A     |  N/A (2.82)    |  10,000 (130x130)    |  ~9 (C1) | Test set for classification (2 classes)
 [50S ribosome](https://www.ebi.ac.uk/pdbe/emdb/empiar/entry/10076/)   | 50.3GB     | N/A     |  N/A (1.31)    |  131,899 (320X320)    | N/A| Test set for classification (4~7 classes)
 [80S ribosome](https://www3.mrc-lmb.cam.ac.uk/relion/index.php?title=Benchmarks_%26_computer_hardware)   | 1.2TB     | 1081(16)     |  4096x4096 (1.34)    | 105,247 (360x360)     | 3.2 (C1) | Test set for computational performance
 [Beta-Gal](https://www.ebi.ac.uk/pdbe/emdb/empiar/entry/10204/)   | 321.4GB   | 1338(49)     |  3710x3838 (0.885)    | N/A     | 2.6 (D2)| Test set for high-resolution reconstruction
 [Apoferritin](https://www.ebi.ac.uk/pdbe/emdb/empiar/entry/10200/)   | 191.5GB     | 1255(40)     |  3710x3838 (0.814)    |   N/A   | 1.65 (O)| Test set for high-resolution reconstruction
 [T20S](https://www.ebi.ac.uk/pdbe/emdb/empiar/entry/10025/)   | 2.0TB     | 196(38)     |  7420x7676 (0.6575)    |  49,955(448X448)    | 2.8 (D7)| Test set for high-resolution reconstruction
 [TRPV1](https://www.ebi.ac.uk/pdbe/emdb/empiar/entry/10059/)   | 93.8GB     | 1200(1)     |  3710x3838 (1.256)    |  218,805 (192X192)    | 2.95 (C4)| Test set for Membrane protein (Nonuniform reconstruction)
 [Spliceosome](https://www.ebi.ac.uk/pdbe/emdb/empiar/entry/10180/)   | 126.5GB     | N/A     |  N/A (1.699)    |  327,490 (320X320)    | N/A | Test set for continuous conformation
 

2. From tutorial data set.


 DataSet (Molecule) | File Size | Movie (#frame) | Micrograph Size (Pixel Size) | Picked Particles (Size) | Final Resolution(A)(Symmetry)
 :--------: | :--------: | :--------: | :--------: | :--------: | :--------: 
 [Scipion](https://github.com/I2PC/scipion/wiki/tutorials/scipion_tutorial_betagal.pdf) <br>  ([Beta-gal](https://scipion.cnb.csic.es/downloads/scipion/data/tests/relion13_tutorial/))    | 4.0GB     | 15(16)     |  1950x1950 (3.54)    |  (100x100)    | 7.3 (D2) 
 [Relion 3](https://relion.readthedocs.io/en/latest/SPA_tutorial/Introduction.html) <br>  ([Beta-gal](https://www.ebi.ac.uk/pdbe/emdb/empiar/entry/10204/))    | 3.1GB     | 24(24)     |  3710x3838 (0.885)    | (256x256)     |2.9 (D2) 
 [CryoSPARC 2](https://guide.cryosparc.com/processing-data/get-started-with-cryosparc-introductory-tutorial) ([T20S](https://www.ebi.ac.uk/pdbe/emdb/empiar/entry/10025/))    | 8.1GB     | 20(38)     |  7420x7676 (0.6575)    | (440x440)     | 2.93 (D7)
 [CisTEM](https://cistem.org/documentation#tab-1-1) ([ApoFerritin](https://www.ebi.ac.uk/pdbe/emdb/empiar/entry/10146/))    | 5.6GB     | 20(50)     |  1240x1200 (1.5)    |      | 3.0 (O)

3. Generate simulation data
    * [Discrete](Simulation_data.ipynb) 
    * [Continuous](https://github.com/evanseitz/cryoEM_synthetic_continua)
    * [Continuous](https://github.com/ccpem/roodmus)
    * From [CryoDRGN](https://github.com/zhonge/cryodrgn) - Use [`write_star.py`](https://github.com/zhonge/cryodrgn/blob/master/cryodrgn/commands_utils/write_star.py) to convert to star format


DataSet (Molecule) | File Size | Micrograph Size (Pixel Size) | Picked Particles (Size) 
 :--------: | :--------: | :--------: | :--------: 
 [Ribosome](https://zenodo.org/record/4355284#.YHPD3a8zbmF)  | 3.1GB     | N/A (3)   | 50,000 (128x128) 
 [Uniform](https://zenodo.org/record/4355284#.YHPD3a8zbmF)   | 3.0GB     | N/A (6)   | 50,000 (128x128) 
 [Cooperative](https://zenodo.org/record/4355284#.YHPD3a8zbmF)  | 3.0GB     | N/A (6)   | 50,000 (128x128)
 [Noncontiguous](https://zenodo.org/record/4355284#.YHPD3a8zbmF)   | 3.0GB     | N/A (6)   | 50,000 (128x128) 

4. Public dataset
   * [`CryoPPP`](https://github.com/BioinfoMachineLearning/cryoppp) - [**A large expert-curated cryo-EM image dataset for machine learning protein particle picking**](https://www.nature.com/articles/s41597-023-02280-2)
   * [`CryoVirusDB`](https://github.com/BioinfoMachineLearning/CryoVirusDB) - [**CryoVirusDB: A Labeled Cryo-EM Image Dataset for AI-Driven Virus Particle Picking**](https://www.biorxiv.org/content/10.1101/2023.12.25.573312v1)
   * [`Cryo2Struct`](https://github.com/BioinfoMachineLearning/cryo2struct) - [**Cryo2Struct : A Large Labeled Cryo-EM Density Map Dataset for AI-based Reconstruction of Protein Structures**](https://www.biorxiv.org/content/10.1101/2023.06.14.545024v2)
   * [`CryoBench`](https://cryobench.cs.princeton.edu/) - [**CryoBench: Diverse and challenging datasets for the heterogeneity problem in cryo-EM**](https://www.arxiv.org/abs/2408.05526)

## Image Formation model
1. [`TEM Simulator`](http://tem-simulator.sourceforge.net/) - [**Simulation of transmission electron microscope images of biological specimens**](https://onlinelibrary.wiley.com/doi/10.1111/j.1365-2818.2011.03497.x)
2. [`InSilicoTEM`](https://github.com/M4I-nanoscopy/InSilicoTEM/tree/v2.0.0) - [**Image formation modeling in cryo-electron microscopy**](https://www.sciencedirect.com/science/article/abs/pii/S1047847713001226)
3. [`CisTEM_Simulate`](https://github.com/timothygrant80/cisTEM/blob/master/src/programs/simulate/simulate.cpp) - [**Cryo-TEM simulations of amorphous radiation-sensitive samples using multislice wave propagation**](https://www.biorxiv.org/content/10.1101/2021.02.19.431636v2) ([Tutorial](https://cistem-org.github.io/developmental-docs/docs/sim/intro.html))
4. [`icemodeling`](https://github.com/ac8g19/icemodelling) - [**Computational models of amorphous ice for accurate simulation of cryo-EM images of biological samples**](https://www.sciencedirect.com/science/article/pii/S0304399123001997)

## [Motion correction](https://www.sciencedirect.com/science/article/pii/S0076687916300271?via%3Dihub) 

* ### Whole frame alignment
1. [`Unblur`](https://grigoriefflab.umassmed.edu/unblur_summovie) - [**Measuring the optimal exposure for single particle cryo-EM using a 2.6 Å reconstruction of rotavirus VP6**](https://elifesciences.org/articles/06980) ( Use in [`CisTEM`](https://cistem.org/documentation#tab-1-6))
2. `Full-frame motion correction` - (Use in `CryoSPARC`)
3. `Optical Flow` - [**Alignment of direct detection device micrographs using a robust Optical Flow approach**](https://www.sciencedirect.com/science/article/pii/S1047847715000313) (Use in [`Xmipp`](http://xmipp.i2pc.es/))

* ### Patch-based/Per-particle based alignment
1. [`MotionCorr2`](https://emcore.ucsf.edu/ucsf-motioncor2) - [**MotionCor2: anisotropic correction of beam-induced motion for improved cryo-electron microscopy**](https://www.nature.com/articles/nmeth.4193?proof=t) (Use in `Relion` and `CryoSPARC`)
2. [`Alignparts`](https://sites.google.com/site/rubinsteingroup/direct-detector-align_lmbfgs) - [**Alignment of cryo-EM Movies of Individual Particles by Optimization of Image Translations**](https://pubmed.ncbi.nlm.nih.gov/26296328/) (Use in [`CryoSPARC`(local, patch)](https://cryosparc.com/docs/tutorials/patch-motion-ctf))
3. [`Warp`](http://www.warpem.com/warp/?page_id=185) - Contains [Patch-based motion correction](http://www.warpem.com/warp/).
4. `FlexAlign` - [**FlexAlign: An Accurate and Fast Algorithm for Movie Alignment in Cryo-Electron Microscopy**](https://www.mdpi.com/2079-9292/9/6/1040/htm) - (Use in `Scipion`)

* ### [Damage compensation](https://www.sciencedirect.com/science/article/pii/S0076687910810158?via%3Dihub)
    * This functionality is le in most of the motion correction tool
    * The [**dark/gain corrected**](https://pubmed.ncbi.nlm.nih.gov/27572724/) is also conducted in this stage

## [CTF estimation](https://www.sciencedirect.com/science/article/pii/S0076687910820026?via%3Dihub)
* ### Whole frame
1. [`CTFFIND5`](https://github.com/GrigorieffLab/cisTEM/tree/ctffind5) - [**CTFFIND5 provides improved insight into quality, tilt and thickness of TEM samples**](https://elifesciences.org/articles/97227) ( Use in [`CisTEM`](https://cistem.org/development))
2. [`gCTF`](https://www2.mrc-lmb.cam.ac.uk/research/locally-developed-software/zhang-software/#gctf) - [**Gctf: Real-time CTF determination and correction**](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4711343/)
* ### Patch-based/tilt data
1. `Patch-Based CTF Estimation` - [**Real-time cryo-electron microscopy data preprocessing with Warp**](https://www.nature.com/articles/s41592-019-0580-y) ( Use in [`CryoSPARC`](https://cryosparc.com/docs/tutorials/patch-motion-ctf), `Warp`)
2. [`goCTF`](https://www.lsi.umich.edu/science/centers-technologies/cryo-electron-microscopy/research/goctf) - [**goCTF: Geometrically optimized CTF determination for single-particle cryo-EM**](https://www.lsi.umich.edu/science/centers-technologies/cryo-electron-microscopy/research/goctf)
3. [`Warp`](http://www.warpem.com/warp/?page_id=185) - Contains Patch-based CTF estimation.
4. [`novaCTF`](https://github.com/turonova/novaCTF) - [**Efficient 3D-CTF correction for cryo-electron tomography using NovaCTF improves subtomogram averaging resolution to 3.4 Å**](https://www.sciencedirect.com/science/article/pii/S1047847717301272?via%3Dihub)

* ### Denoising micrograph
1. [`NoiseTransfer2clean`](https://github.com/Lihongjia-ict/NoiseTransfer2clean) - [**Noise-Transfer2Clean: denoising cryo-EM images based on noise modeling and transfer**](https://academic.oup.com/bioinformatics/article/38/7/2022/6522116)
2. [`Restore`](https://github.com/eugenepalovcak/restore) - [**Enhancing SNR and generating contrast for cryo-EM images with convolutional neural networks**](https://journals.iucr.org/m/issues/2020/06/00/pw5015/)
3. `Topaz` - [**Topaz-Denoise: general deep denoising models for cryoEM**](https://www.nature.com/articles/s41467-020-18952-1)
4.  [`JANNI`](https://sphire.mpg.de/wiki/doku.php?id=janni) - Just Another Noise 2 Noise Implementation 
5.  `Warp` - Contains methods base on noise2noise and deconvolution filter 

* ### Filtering micrograph
1. [`Miffi`](https://github.com/ando-lab/miffi) - [**Miffi: Improving the accuracy of CNN-based cryo-EM micrograph filtering with fine-tuning and Fourier space information**](https://www.sciencedirect.com/science/article/pii/S1047847724000121)

## Particle picking
* ### Semi-supervised picking
1. [`CRISP`](https://github.com/phonchi/CryoParticleSegment) - [**CRISP: A Framework for Cryo-EM Image Segmentation and Processing with Conditional Random Field**](https://arxiv.org/abs/2502.08287)
2. [`Topaz`](https://github.com/tbepler/topaz) - [**Positive-unlabeled convolutional neural networks for particle picking in cryo-electron micrographs**](https://www.nature.com/articles/s41592-019-0575-8). [[Video]](https://www.youtube.com/watch?v=FnCnsT3GIC4&list=PLFEB3YHuxu11Jp_pOCIEtXxSqozFHve0O&index=10)
3. [`Cryolo`](https://cryolo.readthedocs.io/en/stable/) - [**SPHIRE-crYOLO is a fast and accurate fully automated particle picker for cryo-EM**](https://www.nature.com/articles/s42003-019-0437-z). [[Video](https://www.youtube.com/watch?v=JTgldM4wAAk&list=UUbo1TnKiXGtkE_R5b526JmQ&index=6&t=1s&app=desktop)]
4. `Xmipp` - [**A pattern matching approach to the automatic selection of particles from low-contrast electron micrographs**](https://academic.oup.com/bioinformatics/article/29/19/2460/189951)
5. [`EPicker`](https://github.com/thuem/EPicker) - [**EPicker is an exemplar-based continual learning approach for knowledge accumulation in cryoEM particle picking**](https://www.nature.com/articles/s41467-022-29994-y)
6. [`CryoTransformer`](https://github.com/jianlin-cheng/CryoTransformer) - [**CryoTransformer: A Transformer Model for Picking Protein Particles from Cryo-EM Micrographs**](https://www.biorxiv.org/content/10.1101/2023.10.19.563155v1)
7. [`CryoSegNet`](https://github.com/jianlin-cheng/CryoSegNet) - [**Accurate cryo-EM protein particle picking by integrating the foundational AI image segmentation model and specialized U-Net**](https://www.biorxiv.org/content/10.1101/2023.10.02.560572v1)
8. [`Upicker`](https://github.com/JachyLikeCoding/UPicker) - [**UPicker: a semi-supervised particle picking transformer method for cryo-EM micrographs**](https://academic.oup.com/bib/article/26/1/bbae636/7919967)
9. [`CASSPER`](https://github.com/airis4d/CASSPER/releases) - [**CASSPER is a semantic segmentation-based particle picking algorithm for single-particle cryo-electron microscopy**](https://www.nature.com/articles/s42003-021-01721-1)
10. [`TARDIS`](https://github.com/SMLC-NYSBC/TARDIS) - [**Automated Segmentation of 3D Cytoskeletal Filaments from Electron Micrographs with TARDIS**](https://academic.oup.com/mam/article/29/Supplement_1/970/7228849?login=true)
11. [`REPIC`](https://github.com/ccameron/REPIC) - [**REPIC — an ensemble learning methodology for cryo-EM particle picking**](https://www.nature.com/articles/s42003-024-07045-0)
12. [`Vesicle Picker`](https://github.com/r-karimi/vesicle-picker) - [**Vesicle Picker: A tool for efficient identification of membrane protein complexes in vesicles**](https://www.sciencedirect.com/science/article/pii/S1047847724000881)

* ### Template-based picking
1. [`Relion`](https://www.sciencedirect.com/science/article/pii/S1047847714002615), `CryoSPARC` - Use 2D class averages or 3D projection for more accurate particle picking
* ### Automatic picking
1. [`DoG`](https://emg.nysbc.org/redmine/projects/software/wiki/DoGpicker) - [**DoG Picker and TiltPicker: software tools to facilitate particle selection in single particle electron microscopy**](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2768396/)
2. `LoG` - [**The Laplacian of Gaussian and Arbitrary Z-Crossings Approach Applied to Automated Single Particle Reconstruction**](https://pubmed.ncbi.nlm.nih.gov/17490891/) (Use in `Relion` auto-picking) 
3. [`APPLE`](https://github.com/PrincetonUniversity/APPLEpicker) - [**APPLE picker: Automatic particle picking, a low-effort cryo-EM framework**](https://www.sciencedirect.com/science/article/pii/S1047847718302326) (Use in `ASPIRE` auto-picking) 
4. [`KLT picker`](https://github.com/ShkolniskyLab/kltpicker) - [**KLT picker: Particle picking using data-driven optimal templates**](https://www.sciencedirect.com/science/article/pii/S1047847720300356)

* ### Denoising particle/dimenison reduction and its applications
1. [`2SDR`](http://sabid.stat.sinica.edu.tw/start) - [**Two-stage dimension reduction for noisy high-dimensional images and application to Cryogenic Electron Microscopy**](https://www.intlpress.com/site/pub/pages/journals/items/amsa/content/vols/0005/0002/a004/index.php)
2. `PrePro` - [**Pre-pro is a fast pre-processor for single-particle cryo-EM by enhancing 2D classification**](https://www.nature.com/articles/s42003-020-01229-0)
3. [`MScale`](https://github.com/zhanghui186/Mscale) - [**A strategy combining denoising and cryo-EM single particle analysis**](https://academic.oup.com/bib/article/24/3/bbad148/7140293)
4. [`CryoEM Signal Enhancement`](https://github.com/TamirBendory/CryoEMSignalEnhancement) - [**Signal enhancement for two-dimensional cryo-EM data processing**](https://www.cambridge.org/core/journals/biological-imaging/article/signal-enhancement-for-twodimensional-cryoem-data-processing/7FA5DE71969B1BF15FC615DC05C9226C)
5. [`CWF`](https://github.com/PrincetonUniversity/cwf_denoise) - [**Denoising and covariance estimation of single particle cryo-EM images**](https://www.sciencedirect.com/science/article/pii/S104784771630082X) (Use in `ASPIRE`) 
6. [`GAN`](https://github.com/cianfrocco-lab/GAN-for-Cryo-EM-image-denoising) - [**Generative adversarial networks as a tool to recover structural information from cryo-electron microscopy data**](https://www.biorxiv.org/content/10.1101/256792v1.article-info)


## 2D classification

* ### Multirefence alignment-based classification
1. `ISAC` - [**Iterative Stable Alignment and Clustering of 2D Transmission Electron Microscope Images**](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3426367/). [[GPU version]](https://sphire.mpg.de/wiki/doku.php?id=gpu_isac)
2. `CL2D` - [**A clustering approach to multireference alignment of single-particle projections in electron microscopy**](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2893300/)
3. `RE2DC` - [**RE2DC: a robust and efficient 2D classifier with visualization for processing massive and heterogeneous cryo-EM data**](https://www.biorxiv.org/content/10.1101/2022.11.21.517443v2)

* ### [Maximum-likelihood based classification](https://www.sciencedirect.com/science/article/pii/S0076687910820117?via%3Dihub)
1. `Relion` - Bayesian (Empirical Bayes) approach
2. `CryoSPARC` - Bayesian with Branch and bound method
3. `CisTEM` - Maximum likelihood method
4. [`SubspaceEM`](https://www.mathworks.com/matlabcentral/fileexchange/50091-subspaceem-a-fast-maximum-a-posteriori-algorithm-for-cryo-em-single-particle-reconstruction) - [**SubspaceEM: A fast maximum-a-posteriori algorithm for cryo-EM single particle reconstruction**](https://www.sciencedirect.com/science/article/pii/S1047847715000714)

* ### Mixed approach classification
6. [`ROME`](http://ipccsb.dfci.harvard.edu/rome/) - [**Massively parallel unsupervised single-particle cryo-EM data clustering via statistical manifold learning**](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0182130)

* ### Automatic selection of 2D classes
1. [`Cryoassess`](https://github.com/cianfrocco-lab/Automatic-cryoEM-preprocessing) -[**High-Throughput Cryo-EM Enabled by User-Free Preprocessing Routines**](https://www.sciencedirect.com/science/article/pii/S0969212620300800?via%3Dihub)
2. [`Cinderella`](https://sphire.mpg.de/wiki/doku.php?id=auto_2d_class_selection) - Cinderella: Deep learning based binary classification tool
* ### New clustering methods
1. [`γ-SUP`](http://sabid.stat.sinica.edu.tw/start) - [**γ-SUP: A clustering algorithm for cryo-electron microscopy images of asymmetric particles**](https://projecteuclid.org/euclid.aoas/1396966286)
2. [`Wasserstein-k-means`](https://github.com/4tywon/wasserstein-k-means) - [**Wasserstein K-Means for Clustering Tomographic Projections**](https://arxiv.org/abs/2010.09989)

## [3D Tomographic Reconstruction](https://www.sciencedirect.com/science/article/pii/S0076687910820014)
1. [**A Survey of the Use of Iterative Reconstruction Algorithms in Electron Microscopy**](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5623807/)
2. [`ASTRA`](https://github.com/astra-toolbox/astra-toolbox)
3. `ZART`- [**ZART: A Novel Multiresolution Reconstruction Algorithm with Motion-blur Correction for Single Particle Analysis**](https://www.sciencedirect.com/science/article/pii/S002228362300150X#s0070) ( Use in `XMIPP`)

## Ab-initial model 
* ### Class-averages-based method
1. [`Simple`](https://simplecryoem.com/)-[**Single-particle cryo-EM-Improved Ab Initio 3D Reconstruction With SIMPLE/PRIME**](https://pubmed.ncbi.nlm.nih.gov/28795512/)
* ### Particles based method
1. `CryoSPARC` - [**cryoSPARC: algorithms for rapid unsupervised cryo-EM structure determination**](https://www.nature.com/articles/nmeth.4169). [[Slides]](https://nramm.nysbc.org/wp-content/seminars/2017/slides/nysbc-nov2017-Brubaker.pdf)

## 3D refinement
* ### 3D Homogeneous Refinement
1. `Relion` - [**RELION: Implementation of a Bayesian approach to cryo-EM structure determination**](https://www.sciencedirect.com/science/article/pii/S1047847712002481). [[Video]](https://www.youtube.com/watch?time_continue=2&v=TfLFCeehfjM&feature=emb_title)
2. [`CryoSPARC`](https://www.nature.com/articles/nmeth.4169) - Use Expectation-Maximization with branch and bound method for higher resolution
3. [`OPUS-SSRI`](https://github.com/alncat/cryoem) - [**Sparseness and Smoothness Regularized Imaging for improving the resolution of Cryo-EM single-particle reconstruction**](https://www.pnas.org/content/118/2/e2013756118)
4. [`CryoNeFEN`](https://github.com/yuehuang2023/cryoNeFEN) - [**High-resolution real-space reconstruction of cryo-EM structures using a neural field network**](https://www.nature.com/articles/s42256-024-00870-2)

* ### [New 3D reconstruction paradigm](https://www.sciencedirect.com/science/article/pii/S1047847722000909)
1. [`Cryo-Forum`](https://github.com/phonchi/cryo-forum) - [**Cryo-forum: A framework for orientation recovery with uncertainty measure with the application in cryo-EM image analysis**](https://www.sciencedirect.com/science/article/abs/pii/S1047847723001211)
2. [`Pose Estimation with VAE-GAN`](https://github.com/compSPI/article-CVPR-workshop-2020)-[**Estimation of Orientation and Camera Parameters from Cryo-Electron Microscopy Images with Variational Autoencoders and Generative Adversarial**](https://openaccess.thecvf.com/content_CVPRW_2020/html/w57/Miolane_Estimation_of_Orientation_and_Camera_Parameters_From_Cryo-Electron_Microscopy_Images_CVPRW_2020_paper.html). [[Related work]](https://arxiv.org/abs/2107.02958)
3. [`CryoGAN`](https://github.com/harshit-gupta-cor/CryoGAN) - [**CryoGAN: A New Reconstruction Paradigm for Single-Particle Cryo-EM Via Deep Adversarial Learning**](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=9483649)
4. [`Orientation recovery with Siamese neural network`](https://github.com/JelenaBanjac/protein-reconstruction) - [**Learning to recover orientations from projections in single-particle cryo-EM**](https://arxiv.org/abs/2104.06237)
5. [`CryoAI`](https://github.com/compSPI/cryoAI) - [**Amortized Inference of Poses for Ab Initio Reconstruction of 3D Molecular Volumes from Real Cryo-EM Images**](https://arxiv.org/abs/2203.08138)
6. [`DRGN-AI`](https://github.com/ml-struct-bio/drgnai) - [**Revealing biomolecular structure and motion with neural ab initio cryo-EM reconstruction**](https://www.biorxiv.org/content/10.1101/2024.05.30.596729v1)

* ### 3D classification
1. [`Relion`](http://franklab.cpmc.columbia.edu/franklab/Learning_Materials/Meeting_7_Maximum_Likelihood/Papers/Scheres_2016_MIE_v579.pdf), `CryoSPARC`  - Perturb the initial model and use projection matching with weighted assignment
2. [`LCTC`](https://github.com/ghl1995/LCTC) - [**An Efficient Method to Quantify Structural Distributions in Heterogeneous cryo-EM Datasets**](https://www.biorxiv.org/content/10.1101/2021.05.27.446075v1)

* ### 3D non-uniform Refinemnet
1. `CryoSPARC` - [**Non-uniform refinement: Adaptive regularization improves single particle cryo-EM reconstruction**](https://www.nature.com/articles/s41592-020-00990-8)
2. [`SideSplitter`](https://github.com/StructuralBiology-ICLMedicine/SIDESPLITTER) - [**Mitigating Local Over-fitting During Single Particle Reconstruction with SIDESPLITTER**](https://www.sciencedirect.com/science/article/pii/S1047847720301180). [[Video]](https://www.youtube.com/watch?v=jTNH6Z0n254&list=PLFEB3YHuxu11Jp_pOCIEtXxSqozFHve0O&index=12)

## [3D variability analysis](http://scripts.iucr.org/cgi-bin/paper?S2053230X18015108)
1. [`CryoSTAR`](https://github.com/bytedance/cryostar) - [**CryoSTAR: Leveraging Structural Prior and Constraints for Cryo-EM Heterogeneous Reconstruction**](https://www.nature.com/articles/s41592-024-02486-1)
1. [`OPUS-DSD`](https://github.com/alncat/opusDSD) - [**OPUS-DSD: deep structural disentanglement for cryo-EM single-particle analysis**](https://www.nature.com/articles/s41592-023-02031-6)
1. [`RECOVAR`](https://github.com/ma-gilles/recovar) - [**A Bayesian Framework for Cryo-EM Heterogeneity Analysis using Regularized Covariance Estimation**](https://www.biorxiv.org/content/10.1101/2023.10.28.564422v1)
1. [`sbackprop`](https://github.com/dkimanius/sbackprop) - [**Sparse Fourier Backpropagation in Cryo-EM Reconstruction**](https://openreview.net/pdf?id=51f5sPXJD_E)
1. [`Flexutils`](https://github.com/scipion-em/scipion-em-flexutils) - [**Estimating conformational landscapes from Cryo-EM particles by 3D Zernike polynomials**](https://www.nature.com/articles/s41467-023-35791-y) ( Use in `Xmipp`)
1. [`DynaMight`](https://github.com/3dem/DynaMight) - [**DynaMight: estimating molecular motions with improved reconstruction from cryo-EM images**](https://www.nature.com/articles/s41592-024-02377-5) (Use in `Relion5`)
1. `Diffusion Prior` - [**Latent Space Diffusion Models of Cryo-EM Structures**](https://arxiv.org/abs/2211.14169)
1. [`DGP-SPR`](https://github.com/benjamin3344/DGP-SPR) - [**Deep Generative Priors for Biomolecular 3D Heterogeneous Reconstruction from Cryo-EM Projections**](https://www.sciencedirect.com/science/article/pii/S1047847724000133)
1. [`3DFlex`](https://cryosparc.com/3dflex) - [**3D Flexible Refinement: Structure and Motion of Flexible Proteins from Cryo-EM**](https://www.biorxiv.org/content/10.1101/2021.04.22.440893v1) ( Use in `CryoSPARC`)
1. [`e2gmm`](https://blake.bcm.edu/emanwiki/EMAN2/e2gmm) - [**Deep learning-based mixed-dimensional Gaussian mixture model for characterizing variability in cryo-EM**](https://www.nature.com/articles/s41592-021-01220-5)  ( Use in `EMAN2`, more information see [here](https://www.sciencedirect.com/science/article/pii/S0022283623000700))
1. `3DVA` - [**3D Variability Analysis: Directly resolving continuous flexibility and discrete heterogeneity from single particle cryo-EM images**](https://www.sciencedirect.com/science/article/pii/S1047847721000071) ( Use in `CryoSPARC`)
1. [`CryoDRGN2`](https://github.com/zhonge/cryodrgn/tree/vb/v2_quickstart) - [**CryoDRGN2: Ab initio neural reconstruction of 3D protein structures
from real cryo-EM images**](https://openaccess.thecvf.com/content/ICCV2021/papers/Zhong_CryoDRGN2_Ab_Initio_Neural_Reconstruction_of_3D_Protein_Structures_From_ICCV_2021_paper.pdf)
1. [`CryoDRGN`](https://github.com/zhonge/cryodrgn) - [**CryoDRGN: Reconstruction of heterogeneous structures from cryo-electron micrographs using neural networks**](https://www.nature.com/articles/s41592-020-01049-4?utm_source=other&utm_medium=other&utm_content=null&utm_campaign=JRCN_1_DD01_CN_NatureRJ_article_paid_XMOL) (For processing with large dataset see [here](https://zhonge.github.io/cryodrgn/index.html))
1. [`ManifoldEM`](https://github.com/evanseitz/ManifoldEM_Python) - [**Retrieving functional pathways of biomolecules from single-particle snapshots**](https://www.nature.com/articles/s41467-020-18403-x)
1. [`DMSA`](https://github.com/evanseitz/cryoEM_DMSA) - [**Recovery of conformational continuum from single-particle cryo-EM data: Optimization of ManifoldEM informed by ground-truth studies**](https://www.biorxiv.org/content/10.1101/2021.06.18.449029v1)
1. [`AlphaCryo4D`](https://github.com/AlphaCryo4D/AlphaCryo4D) - [**Visualizing Conformational Space of Functional Biomolecular Complexes by Deep Manifold Learning**](https://www.mdpi.com/1422-0067/23/16/8872)
1. [`BioEM`](https://github.com/bio-phys/BioEM) - [**A Bayesian approach to extracting free-energy profiles from cryo-electron microscopy experiments**](https://www.nature.com/articles/s41598-021-92621-1)
1. `VAE` - [**Inferring a Continuous Distribution of Atom Coordinates from Cryo-EM Images using VAEs**](https://arxiv.org/abs/2106.14108)
1. `cryoFIRE` - [**Amortized Inference for Heterogeneous Reconstruction in Cryo-EM**](https://arxiv.org/abs/2210.07387)
1. `Atomic VAE` - [**Heterogeneous reconstruction of deformable atomic models in Cryo-EM**](https://arxiv.org/abs/2209.15121)
1. [`SpecVols`](https://github.com/PrincetonUniversity/specvols) - [**Cryo-EM reconstruction of continuous heterogeneity by Laplacian spectral volumes**](https://iopscience.iop.org/article/10.1088/1361-6420/ab4f55) (Use in [`ASPIRE`](https://github.com/ComputationalCryoEM/ASPIRE-Python/blob/main/src/aspire/reconstruction/mean.py#L18))
2. [`CryoTRANS`](https://github.com/mxhulab/cryotrans) - [**CryoTRANS: predicting high-resolution maps of rare conformations from self-supervised trajectories in cryo-EM**](https://www.nature.com/articles/s42003-024-06739-9)
3. [`cryoENsemble`](https://github.com/dydymos/cryoENsemble) - [**Bayesian reweighting of biomolecular structural ensembles using heterogeneous cryo-EM maps with the cryoENsemble method**](https://www.nature.com/articles/s41598-024-68468-7)

* ### Latent space analysis
1. [`CLEAPA`](https://github.com/tengyulin/energy_aware_pathfinding)- [**CLEAPA: a framework for exploring the conformational landscape of cryo-EM using energy-aware pathfinding algorithm**](https://academic.oup.com/bioinformatics/article/40/6/btae345/7688336)
2. [`Polaris`](https://github.com/evanseitz/POLARIS) - [**POLARIS: Path of Least Action Analysis on Energy Landscapes**](https://pubs.acs.org/doi/full/10.1021/acs.jcim.9b01108)
3. [`MAVEn`](https://github.com/lkinman/MAVEn) - [**Uncovering structural ensembles from single-particle cryo-EM data using cryoDRGN**](https://www.nature.com/articles/s41596-022-00763-x)

* ### [Focus classifcation](https://www.frontiersin.org/articles/10.3389/fmolb.2019.00033/full)
1. [**Focused classifications and refinements in high-resolution single particle cryo-EM analysis**](https://www.sciencedirect.com/science/article/pii/S1047847723000783)
1. [`localrec`](https://github.com/OPIC-Oxford/localrec) - [**Localized reconstruction of subunits from electron cryomicroscopy images of macromolecular complexes**](https://www.nature.com/articles/ncomms9843) (Use in `Scipion`)
2. `Multi-body refinement` - [**Characterisation of molecular motions in cryo-EM single-particle data by multi-body refinement in RELION**](https://elifesciences.org/articles/36861) (Use in `Relion`)


## [Postprocessing](https://www.sciencedirect.com/science/article/pii/S0079610720300699)
* ### Per-particle-based motion and CTF refinement
1. `CTF refinement` - [`Relion3`](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6250425/)/[`CisTEM`](https://cistem.org/documentation#tab-1-12)/[`CryoSPARC`](https://cryosparc.com/docs/tutorials/ctf-refinement), 3D Reference required
2. `Ewald sphere correction` - [**New tools for automated high-resolution cryo-EM structure determination in RELION-3**](https://elifesciences.org/articles/42166#bib45) (Use ` relion_reconstruct --reverse_curvature`)
3.  `High-order aberrations` - [**Estimation of high-order aberrations and anisotropic magnification from cryo-EM data sets in RELION-3.1**](https://journals.iucr.org/m/issues/2020/02/00/fq5009/index.html)
4. `Bayesian Polishing` - [**A Bayesian approach to beam-induced motion correction in cryo-EM single-particle analysis**](https://journals.iucr.org/m/issues/2019/01/00/fq5003/)  (Use in Relion, 3D Reference required)
5. [`M`](http://www.warpem.com/warp/?page_id=827) - [**Multi-particle cryo-EM refinement with M visualizes ribosome-antibiotic complex at 3.5 Å inside cells**](https://www.nature.com/articles/s41592-020-01054-7). [[Video]](https://www.youtube.com/watch?v=kiS-ELvQ1gc&list=PLFEB3YHuxu11Jp_pOCIEtXxSqozFHve0O&index=18)

* ### 3D Refinemnet with anisotropy correction
1. [`spIsoNet`](https://github.com/IsoNet-cryoET/spIsoNet) - [**Overcoming the preferred orientation problem in cryoEM with self-supervised deep-learning**](https://www.nature.com/articles/s41592-024-02505-1)
2. [`CryoPROS`](https://github.com/mxhulab/cryopros) - [**Addressing preferred orientation in single-particle cryo-EM through AI-generated auxiliary particles**](https://www.biorxiv.org/content/10.1101/2023.09.26.559492v1)
3. [`SIRM`](https://github.com/homurachan/SIRM_RELION) - [**Correction of preferred orientation–induced distortion in cryo–electron microscopy maps**](https://www.science.org/doi/full/10.1126/sciadv.adn0092)

* ### [Local resolution](https://www.sciencedirect.com/science/article/pii/S0959440X20301044) and directional resolution
1. [`Blocres`](https://lsbr.niams.nih.gov/bsoft/programs/blocres.html) - [**One number does not fit all: Mapping local variations in resolution in cryo-EM reconstructions**](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3837392/)
1. [`ResMap`](https://sourceforge.net/projects/resmap-latest/) - [**Quantifying the Local Resolution of Cryo-EM Density Maps**](https://www.nature.com/articles/nmeth.2727)
2. `MonoRes` - [**MonoRes: Automatic and Accurate Estimation of Local Resolution for Electron Microscopy Maps**](https://pubmed.ncbi.nlm.nih.gov/29395788/) (Use in `Scipion`)
3. [`3DFSC`](https://github.com/nysbc/Anisotropy) - [**Addressing preferred specimen orientation in single-particle cryo-EM through tilting**](https://www.nature.com/articles/nmeth.4347)
4. `MonoDir` - [**Measuring local-directional resolution and local anisotropy in cryo-EM maps**](https://www.nature.com/articles/s41467-019-13742-w) (Use in `Scipion`)

* ### [Sharpening](https://www.sciencedirect.com/science/article/pii/S0022283603010222) and local filtering to enhance [interpretability](https://www.sciencedirect.com/science/article/pii/S0079610720300699)
1. [`EMReady`](http://huanglab.phys.hust.edu.cn/EMReady/)
2. [`EM-GAN`](https://kiharalab.org/emsuites/emgan.php) - **Improved Protein Structure Modeling Using Enhanced Cryo-EM Maps With 3D Deep Generative Networks**
3. [`DeepEnhancer`](https://github.com/rsanchezgarc/deepEMhancer)-[**DeepEMhancer: a deep learning solution for cryo-EM volume post-processing**](https://www.biorxiv.org/content/10.1101/2020.06.12.148296v3)
4. [`Confidence Maps`](https://git.embl.de/mbeckers/FDRthresholding/-/tree/master) - [**Thresholding of cryo-EM density maps by false discovery rate control**](https://journals.iucr.org/m/issues/2019/01/00/pw5002/index.html) (Use in [`ccpem`](https://www.ccpem.ac.uk/download.php))
5. [`LocScale`](https://git.embl.de/jakobi/LocScale)[**Model-based local density sharpening of cryo-EM maps**](https://elifesciences.org/articles/27131) (Use in [`ccpem`](https://www.ccpem.ac.uk/download.php))
6. [`LocalDeblur`](https://github.com/I2PC/scipion-em-xmipp/wiki/XmippProtLocSharp) - [**Automatic local resolution-based sharpening of cryo-EM maps**](https://academic.oup.com/bioinformatics/article/36/3/765/5554698)

* ### Denoising 3D volume
1. [`Warp`](http://www.warpem.com/warp/?page_id=389) - Based on Noise2Noise
2. `Topaz` - Contains 3D denoise functionality
3. [`Relion`](https://github.com/3dem/externprior) - [**Exploiting prior knowledge about biological macromolecules in cryo-EM structure determination**](https://journals.iucr.org/m/issues/2021/01/00/fq5015/)
4. [`Blush regularisation`](https://relion.readthedocs.io/en/release-5.0/Whats-new.html) - [**Data-driven regularisation lowers the size barrier of cryo-EM structure determination**](https://www.nature.com/articles/s41592-024-02304-8)
5. [`crefDenoiser`](https://github.com/ajrzepiela/crefDenoiser) - [**Refinement of cryo-EM 3D maps with a self-supervised denoising model: crefDenoiser**](https://journals.iucr.org/m/issues/2024/05/00/fq5024/index.html)

* ### Particle sorting
1. [`CryoSieve`](https://github.com/mxhulab/cryosieve) - [**A minority of final stacks yields superior amplitude in single-particle cryo-EM**](https://www.nature.com/articles/s41467-023-43555-x)

* ### [Helical reconstruction](https://www.cambridge.org/core/journals/quarterly-reviews-of-biophysics/article/cryoem-reconstruction-of-helical-polymers-beyond-the-simple-cases/F9ED5390A396E502657F02D7D27773C6)

## Model Building
* ### 3D Map Alignment
1. [`BOTalign`](https://github.com/RuiyiYang/BOTalign) - [**Alignment of density maps in Wasserstein distance**](https://www.cambridge.org/core/journals/biological-imaging/article/alignment-of-density-maps-in-wasserstein-distance/59068B152B07ECD15614A8654608E86D)
2. [`CryoAlign`](https://github.com/HeracleBT/CryoAlign) - [**Accurate global and local 3D alignment of cryo-EM density maps using local spatial structural features**](https://www.nature.com/articles/s41467-024-45861-4)
   
* ### Map to model
1. [`EModelX`](https://github.com/biomed-AI/EModelX) - [**Protein complex structure modeling by cross-modal alignment between cryo-EM maps and protein sequences**](https://www.nature.com/articles/s41467-024-53116-5)
2. [`Cryo2Struct`](https://github.com/jianlin-cheng/Cryo2Struct) - [**De novo atomic protein structure modeling for cryoEM density maps using 3D transformer and HMM**](https://www.nature.com/articles/s41467-024-49647-6)
3. [`DeepMainMast`](https://github.com/kiharalab/DeepMainMast) - [**DeepMainmast: integrated protocol of protein structure modeling for cryo-EM with deep learning and structure prediction**](https://www.nature.com/articles/s41592-023-02099-0)
4. [`ModelAngelo`](https://github.com/3dem/model-angelo) - [**ModelAngelo: Automated Model Building in Cryo-EM Maps**](https://arxiv.org/abs/2210.00006)
5. [`DiffModeler`](https://github.com/kiharalab/DiffModeler) - [**DiffModeler: Large Macromolecular Structure Modeling in Low-Resolution Cryo-EM Maps Using Diffusion Model**](https://www.biorxiv.org/content/10.1101/2024.01.20.576370v2)
6. [`adp-3d`](https://axel-levy.github.io/adp-3d/) - [**Solving Inverse Problems in Protein Space Using Diffusion-Based Priors**](https://arxiv.org/abs/2406.04239) (Based on [`chroma`](https://github.com/generatebio/chroma))
7. [`EMBuild`](http://huanglab.phys.hust.edu.cn/EMBuild/) - [**Model building of protein complexes from intermediate-resolution cryo-EM maps with deep learning-guided automatic assembly**](https://www.nature.com/articles/s41467-022-31748-9)
8. [`CryoREAD`](https://github.com/kiharalab/CryoREAD) - [**CryoREAD: de novo structure modeling for nucleic acids in cryo-EM maps using deep learning**](https://www.nature.com/articles/s41592-023-02032-5)
9. [`CSA`](https://github.com/nimijkrap/CSA_for_cryo-EM_results) - [**Application of conformational space annealing to the protein structure modeling using cryo-EM maps**](https://onlinelibrary.wiley.com/doi/full/10.1002/jcc.27200)

* ### [Metrics](https://www.nature.com/articles/s41592-020-01051-w)
1. [`TEMPy`](https://tempy.topf-group.com/) - [**TEMPy2: A Python library with improved 3D electron microscopy density-fitting and validation workflows**](https://journals.iucr.org/d/issues/2021/01/00/qr5003/index.html)
1. [`Phenix`](https://phenix-online.org/documentation/reference/validation_cryo_em.html) - [**New tools for the analysis and validation of cryo-EM maps and atomic models.**](https://doi.org/10.1107/S2059798318009324)
1. [**DeepQs: Local quality assessment of cryo-EM density map by deep learning map-model fit score**](https://www.sciencedirect.com/science/article/pii/S1047847723001223)
1. [`MapQ`](https://github.com/gregdp/mapq) - [**Measurement of atom resolvability in cryo-EM maps with Q-scores**](https://www.nature.com/articles/s41592-020-0731-1)
1. [`FSC-Q`](https://github.com/I2PC/scipion-em-xmipp) - [**FSC-Q: a CryoEM map-to-atomic model quality validation based on the local Fourier shell correlation**](https://www.nature.com/articles/s41467-020-20295-w) (Use in `Scipion`)
1. [`MEDIC`](https://github.com/gabriellareggiano/MEDIC) - [**Residue-level error detection in cryoelectron microscopy models**](https://www.sciencedirect.com/science/article/pii/S0969212623001582)

## Visualization
1. [`Chimera`](https://www.cgl.ucsf.edu/chimera/) - [**UCSF Chimera--a Visualization System for Exploratory Research and Analysis**](https://pubmed.ncbi.nlm.nih.gov/15264254/)
2. [`ChimeraX`](http://www.rbvi.ucsf.edu/chimerax/) - [**UCSF ChimeraX: Meeting modern challenges in visualization and analysis**](https://onlinelibrary.wiley.com/doi/full/10.1002/pro.3235)

# Conventions
## 3DEM Convention
* [3DEM Conventions](https://github.com/azazellochg/3DEM-conventions) - Contains most of the convention in pouplar software (Through the `rst` file)
* [Relion](https://relion.readthedocs.io/en/release-5.0/Reference/Conventions.html#conventions)
* [Symmetry](https://scipion-em.github.io/docs/release-3.0.0/docs/developer/symmetries/symmetries.html)
* [Resolution Measure](https://www.sciencedirect.com/science/article/pii/S0079610716300037)

## Image contrast
`White on Black` - Relion, Xmipp, EMAN2, CryoSPARC (Cryo-EM data is typically recorded as Black on White but will invert during processing)

`Black on White` - Frealign (CisTEM)

## Pixel size
For the format defined in RELION, the actual pixel size is calculated as `rlnDetectorPixelSize * 10000 / rlnMagnification`.
In Relion 3.1 it has been replaced with `rlnImagePixelSize`.


## FSC calculation
Using [e2proc3d](http://sphire.mpg.de/wiki/doku.php?id=pipeline:utilities:e2proc3d)

## Mask generation in [CryoSPARC](https://discuss.cryosparc.com/t/tight-corrected-and-loose-gsfsc-curves/201/5)

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

## Sharpen and filtering in [CryoSPARC](https://discuss.cryosparc.com/t/how-is-the-non-uniform-refinement-map-filtered-map-created/4388)
The `map_filtered` output in non-uniform refinement is generated as follows after refinement has converged:

1. both raw, unfiltered halfmaps are averaged together
2. the raw map is filtered using the Gold-Standard FSC curve
3. the filtered map is sharpened using the Guinier-plot estimated b-factor
4. the sharpened map is outputted as `_map_sharp_local.mrc` (confusing filename… sorry)
5. the sharpened map is locally filtered using a local resolution estimate computed from the half-maps and the locally filtered map is outputted as `_map_filtered.mrc`


# Tips
## Format Conversion
1. Using [PyRelion](https://github.com/OPIC-Oxford/localrec/wiki/Tips-and-tricks)
Operate Star files

1. Using [PyEM](https://github.com/asarnow/pyem)
Convert metadata

1. Using [EMAN2](https://github.com/cryoem/eman2/blob/master/examples/e2convertrelion.py)
Convert from relion to eman2

1. Using [EMAN2](https://blake.bcm.edu/emanwiki/EMAN2)
Convert binary data

## Parse `Star file`
1. [`starfile`](https://github.com/teamtomo/starfile) - Read star file as DataFrame
2. [`starparser`](https://github.com/sami-chaaban/starparser) - Command line tool for star file
3. Using Custom function like [here](Parse_Star.ipynb)
4. [`starpy`](https://github.com/fuzikt/starpy) - Lots of useful script like [`rel31_to_rel30_star.py`](https://github.com/fuzikt/starpy/blob/master/rel31_to_rel30_star.py)

## Parse `CryoSPARC file`
1. Using [`PyEM`](https://github.com/asarnow/pyem)
2. Using Custom function like [here](Parse_Cryosparc.ipynb). See full tutorial [here](https://guide.cryosparc.com/processing-data/manipulating-.cs-files-created-by-cryosparc) 
3. [`cryosparc-tools`](https://github.com/cryoem-uoft/cryosparc-tools) 

## Performing Focus Classification
### With Chimera
### [CisTEM](https://cistem.org/frequently-asked-questions#tab-1-4)
A focus mask is defined as a sphere specified by radius and x,y,z coordinates of the sphere center, all given in Å. In order to find x,y,z, in CisTEM
1. Open the 3D map in Chimera. The map should be assigned model #0.
1. Display the command line by selecting Tools > General Controls > Command Line.
1. Execute vop threshold #0 maximum -1000 setMaximum 1.0 (this assumes that the minimum voxel value in the 3D map is larger than 1000). This will create a new model #1.
1. Execute shape sphere radius 30 color red mesh true on the Command Line. This will generate a sphere with a 30 Å radius, numbered model #2 (change the radius as needed).
1. Open Tools > General Controls > Model Panel and deactivate models #0 and #1. Then, move the sphere (model #2) into model #1 until it is fully contained in that volume.
1. Execute mask #1 #2 on the Command Line. This will generate a new model #3 of a solid sphere with a 30 Å radius.
1. Close models #1 and #2 in the Model Panel and make sure model #0 is visible but deactivated.
1. Select model #3 (the solid sphere) in Volume Viewer and change its color to red (or something easily distinguishable from the original 3D map) and make it transparent.
1. Move model #3 to the desired location of the focus mask in the 3D map.
1. Execute vop resample #3 onGrid #0 on the Command Line. This will generate a copy of the solid sphere as a new model #1, now resampled in the same coordinate system as the original 3D map.
1. Execute measure center #1 on the Command Line. This will display the x,y,z coordinates of the mask in pixel coordinates below the command line. These coordinates have to be converted to Å by multiplying them with the pixel size of the 3D map before they can be used in cisTEM's Manual Refine panel.

### [Local classification in CryoSPARC](https://cryosparc.com/blog/local-refinement-snRNP-case-study/)

## Display images
### Micrographs
In Matlab use `grayImage = uint8(255 * mat2gray(originalImage)); imshow(grayImage);`

## Using Chimera
### Create a synthetic map from PDB
1. Open chimera and import that protein: File -> Fetch By ID… -> Select PDB and type the PDB ID of the protein -> Fetch. Now, you will see the 3D structure of the protein.
2. Create synthetic map from PDB model: Modify the density of the protein: Tools -> General Controls -> Command Line -> Type: molmap #0 5 (molmap = is a command that generates a density map from the specified atom; # is atom specification, i.e. number assigned to the model by default; 5 = resolution).
3. Store reference map as MRC: Save to a file: Tools -> Volume Data -> Volume Viewer -> File -> Save map as… -> Give it the protein_PDB_ID.mrc.

### [Dispaly local resolution](https://discuss.cryosparc.com/t/view-coloured-3d-map-in-chimera-using-output-from-local-resolution/1003)
### [Flip handedness of model and map](https://github.com/asarnow/pyem/wiki/Z-Flip-for-Models-and-Maps)
### Slice view
`volume #0 planes z,220 step 1 level -1 style surface`
### [Visualizing dynamic movies](https://guide.cryosparc.com/processing-data/tutorials-and-case-studies/tutorial-3d-variability-analysis-part-one#visualization)
#### [Using Script](https://github.com/zhonge/cryodrgn/discussions/79) 


# Contributing
Your contributions are highly appreciated! Please take a look at the [contribution guidelines](https://github.com/phonchi/Computational-CryoEM/blob/master/CONTRIBUTING.md) first.
