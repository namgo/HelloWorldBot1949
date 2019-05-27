# multithreaded run with timeout
import os
import glob
import json
import shlex
from subprocess import call, TimeoutExpired

 # 4 seconds
TIMEOUT = 4

os.chdir('/build')

filenames = [filename.split('.')[0] for filename in glob.glob('*.asm')]
print('processing {} files'.format(len(filenames)))

for filename in filenames:
    cmd = ['gdb {0} "set logging file /build/{0}.output" -ex "set logging on" -ex r -ex "bt full" -ex "info registers" -ex quit'.format(filename)]
    cmd = shlex.shlex(cmd)
    data = {
        'timeout_time': TIMEOUT,
        'timeout_hit': False
    }
    try:
        call(cmd, timeout=TIMEOUT)
    except TimeoutExpired:
        data['timeout_hit'] = True
    with open(filename+'.timeout.json', 'w') as f:
        f.write(json.dumps(data))
