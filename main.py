from generate import generate_asm
import string
import random
import os
import docker
import logging

NUM_FILES = 20000
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

print('''files generated, now please run:
run_docker.sh''')
