#/bin/bash

if [ $# == 1 ] ; then

filename=$1

nasm -f elf32  $filename     # or elf64 
ld -m elf_i386 -o ${filename::-2} ${filename::-1}'o'    # or elf_x86_64
rm ${filename::-1}'o'

fi

