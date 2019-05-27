#!/bin/bash
# build docker image
echo "building docker image"
docker build -t nasm_builder .

echo "building assembly files"
docker run -dt hwb_build nasm_builder:latest \
       --cap-add SYS_PTRACE \
       --security-opt seccomp=unconfined \
       -v `pwd`:/opt/,ro \
       -v `pwd`/output:/build,rw \
       /bin/bash /opt/hwb_build.sh

echo "running assembly files through gdb"
docker run -dt hwb_build nasm_builder:latest \
       --cap-add SYS_PTRACE \
       --security-opt seccomp=unconfined \
       -v `pwd`:/opt/,ro \
       -v `pwd`/output:/build,rw \
       /bin/bash /opt/hwb_run.sh
