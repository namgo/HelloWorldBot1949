# What is this?
HelloWorldBot1949 is an assembly generation bot that uses the power of the cloud☁

# Careful now
I don't really know what I'm doing, I haven't really touched assembly in a long time and it's quite possible that the generated code could do something very strange. I've done my best to keep it contained. I'm also writing as I go.

We'll be using docker to build and run the system.

# Note
We need to disable some security features to be able to run gdb properly

docker run -it -v `pwd`:/opt/ --cap-add=SYS_PTRACE --security-opt seccomp=unconfined nasm /bin/bash

## to run
nasm -f elf64 -F dwarf -g $name.asm
ld $name.o
gdb a.out -batch \
  -ex "set logging on" \
  -ex r \
  -ex "bt full" \
  -ex quit
