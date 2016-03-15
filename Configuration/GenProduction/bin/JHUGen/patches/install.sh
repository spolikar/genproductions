#!/bin/bash

wget --no-check-certificate http://cms-project-generators.web.cern.ch/cms-project-generators/slc6_amd64_gcc481/JHUGenerator.v6.8.5.tar.gz -O JHUGenerator.v6.8.5.tar.gz 
tar xzvf JHUGenerator.v6.8.5.tar.gz 
rm -rf AnalyticMELA
rm -rf JHUGenMELA
cd JHUGenerator
sed -i "s/UseLHAPDF=No/UseLHAPDF=Yes/" makefile
sed -i 's|MyLHADir=.*|MyLHADir=${LHAPDF_DATA_PATH}/../../lib/|' makefile
make
rm ../JHUGenerator.v6.8.5.tar.gz

