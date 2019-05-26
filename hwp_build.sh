#!/bin/bash

$output_dir = '/opt/build'
$build = 'nasm -f elf64 -F dwarf -g'
$link = 'ld -o'
# $gdb_cmd = 'gdb a.out -batch -ex "set logging on" -ex r -ex "bt full" -ex "info registers" -ex quit'

cd $output_dir
for f_asm in `ls *.asm`
do 
    $generic_name = `echo $f_asm | cut -d'.' -f1`
    `$build $f_asm`
    `$link $generic_name $generic_name.o`
done
cd /opt
