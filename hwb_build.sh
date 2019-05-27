#!/bin/bash

# $gdb_cmd = 'gdb a.out -batch -ex "set logging on" -ex r -ex "bt full" -ex "info registers" -ex quit'

cd $output_dir
for f_asm in `ls *.asm`
do 
    echo "built $f_asm"
    generic_name=$(echo $f_asm | cut -d'.' -f1)
    nasm -f elf64 -F dwarf -g $f_asm
    echo "linked $f_asm"
    ld -o $generic_name $generic_name.o
    rm $generic_name.o
done
cd /opt
