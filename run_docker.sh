#!/bin/bash
# build docker image
echo "building docker image"
docker build -t nasm_builder .

echo "building and running assembly files"
docker run -dt -v `pwd`:/opt/,ro -v `pwd`/output:/build,rw --cap-add=SYS_PTRACE --security-opt seccomp=unconfined nasm_builder:latest /bin/bash /opt/build_and_run.sh
