# produce-nanoAODs

This is a modified version of the main repository [produce-nanoAODs](https://github.com/ekauffma/produce-nanoAODs).

This version runs on CERN lxplus machines. To run one needs:

1. Modify the `filenames.txt` with the names of the datasets located in `split-datasets`.
1. Modify `trasnfer_input_files` in the `nanoaod_job.sub` script. Remove the voms proxy with your own certificate. One needs to run:
```
voms-proxy-init -voms cms -valid 72:0
```
and copy the file created into your home area. After that copy the location to that file into the `transfer_input_files`.
1. Modify `run.sh`. First modify user proxy `export X509_USER_PROXY=$PWD/x509up_u22222` with your own proxy. Then change the `EOS_HOME` variable with your user information. 
1. After that, in lxplus, you can run:
```
condor_submit nanoaod_job.sub
```
It will submit as many jobs as lines you have in `filenames.txt`. To check the status of the jobs one can run:
``` 
condor_q
```
the log files will be located in the `logs/` folder.


## Original README

This repository contains the HTCondor submit file and everything else necessary to produce nanoAODs from the CMS 2015 open data

This repo includes the filenames.txt file and split-datasets directory which contain text files with the paths for the ROOT files. 
Here, 30 files are used to produce each nanoAOD.

To change this setting, one should run split_txt_file.py inputfilepath.txt -n N -o outpath
where inputfilepath.txt is a file like in https://github.com/iris-hep/analysis-grand-challenge/blob/main/datasets/cms-open-data-2015/wjets/20548.txt
N is the number of files to combine, and outpath is the directory to write the output text files to.

Write all text files into one text file (like filenames.txt) in order to run job.

To run the job using HTCondor
1) create new log folder, e.g. 0000
   - mkdir logs/0000
2) update log subfolder in job.sub, e.g. with 0000
3) update list of files (if needed)
   - original located in filenames.txt
4) ensure up-to-date proxy
   - voms-proxy-init -voms cms -valid 72:0
5) submit
   - condor_submit nanoAOD_job.sub
