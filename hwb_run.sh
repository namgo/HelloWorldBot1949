#!/bin/bash

working_dir='/build'

cd $working_dir
for f_asm in `ls *.asm`
do 
    executable_name=`echo $f_asm | cut -d'.' -f1`
    `gdb '$executable_name' -batch -ex "set logging file /build/'$executable_name'.output" -ex r -ex "bt full" -ex "info registers" -ex quit`
done
cd /opt
