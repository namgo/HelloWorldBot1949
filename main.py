from generate import generate_asm
import string
import random
import os
import docker
import logging

NUM_FILES = 10
FILENAME_LEN = 20

current_path = os.path.dirname(os.path.realpath(__file__))
build_dir = current_path + '/output'
try:
    os.mkdir(build_dir)
except:
    pass

# generate lots and lots and lots of files
for i in range(0, NUM_FILES):
    filename = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(FILENAME_LEN)) + '.asm'
    with open(build_dir+'/'+filename, 'w') as f:
        f.write(generate_asm())

client = docker.from_env()
image = client.images.build(path=current_path, tag='nasm_builder')

container = client.containers.create(
    image='nasm_builder:latest', command='/bin/bash /opt/build_and_run.sh', name='hwb_build',
    cap_add='SYS_PTRACE', security_opt=['apparmor:unconfined','seccomp:unconfined'],
    volumes={
        current_path: {'bind': '/opt', 'mode':'ro'},
        build_dir: {'bind': '/build', 'mode': 'rw'}
    }
)
container.start()
print(container.logs(stdout=True, stderr=True))
