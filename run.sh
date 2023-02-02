#!/bin/bash
/bin/pwd
/bin/uname -a
/bin/hostname

# set up CMSSW (Sneha's version)
source /cvmfs/cms.cern.ch/cmsset_default.sh
echo $PWD
export X509_USER_PROXY=$PWD/x509up_u15148
EOS_HOME=/eos/user/a/algomez
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

# get text file as $INP and create output filename
INP=$1
echo "input: $INP"

if [[ $INP == Single* ]]; then
    SCRIPT=data_cfg.py
else
    SCRIPT=nanoaod15_cfg.py
fi

# create nanoAOD
cp ../../$SCRIPT .
echo "running cmsRun $SCRIPT split-datasets/$INP"
cmsRun $SCRIPT split-datasets/$INP
echo "saving to out.root"

cd ../..
ls -lh

# transfer file
echo "EOS home:" $EOS_HOME
OUTPUT_DIR=${EOS_HOME}/tmpFiles/opendata_files/
echo "Output directory:" $OUTPUT_DIR

echo ""xrdcp -f out.root root://eosuser.cern.ch/${OUTPUT_DIR}/${INP}.root""
xrdcp -f out.root root://eosuser.cern.ch/${OUTPUT_DIR}/${INP}.root
ls

