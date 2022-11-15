# produce-nanoAODs
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
