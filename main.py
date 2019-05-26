from generate import generate_asm
import os
import docker
import logging
nasm_log = logging.getLogger('nasm_builder')
cloud_log = logging.getLogger('gcloud')

current_path = os.path.dirname(os.path.realpath(__file__))
try:
    os.mkdir(current_path + '/output')
except:
    pass

client = docker.from_env()
image = client.images.build(path=current_path, tag='nasm_builder')

container = client.containers.create(
    image=image, command='/bin/bash', name='hwb_build',
    cap_add='SYS_PTRACE', security_opt='seccomp:unconfined'
)
container.start()
