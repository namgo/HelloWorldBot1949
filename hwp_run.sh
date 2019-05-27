#!/bin/bash

working_dir='/build'
gdb_cmd='gdb -batch -ex "set logging on" -ex r -ex "bt full" -ex "info registers" -ex quit'

cd $working_dir
for f_asm in `ls *.asm`
do 
    executable_name=`echo $f_asm | cut -d'.' -f1`
    `$gdb_cmd $executable_name > $executable_name.output`
done
cd /opt
