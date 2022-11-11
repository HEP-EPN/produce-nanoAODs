#!/bin/bash

source /cvmfs/cms.cern.ch/cmsset_default.sh
echo $PWD
export X509_USER_PROXY=$PWD/x509up_u7652  # id -u ekauffma
voms-proxy-info --all
scram list CMSSW_10_6_
echo $SCRAM_ARCH
export SCRAM_ARCH=slc7_amd64_gcc820
scram project CMSSW_10_6_30
cd CMSSW_10_6_30/
cmsenv
cd src/
git cms-merge-topic 39040
ls -al
scram build -j5
echo "finished setting up cmssw"

cp ../../wjets_cfg.py .
echo "running cmsRun wjets_cfg.py"
cmsRun wjets_cfg.py
ls -lh
echo $PWD
echo "saving to nanoaod_wjets.root"
cd ../..
ls -lh
echo $PWD
