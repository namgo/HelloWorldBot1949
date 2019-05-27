# multithreaded run with timeout
import os
import glob
import json
import shlex
from subprocess import call, TimeoutExpired
import threading
import queue

 # 20 seconds
TIMEOUT = 20

q = queue.Queue()
os.chdir('/build')

filenames = [filename.split('.')[0] for filename in glob.glob('*.asm')]
print('processing {} files'.format(len(filenames)))

def run_command(filename):
    cmd = 'gdb {0} -ex "set logging file /build/{0}.output" -ex "set logging on" -ex r -ex "bt full" -ex "info registers" -ex quit'.format(filename)
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

def worker():
    while True:
        item = q.get()
        if item is None:
            break
        run_command(item)
        q.task_done()

threads = []
for i in range(10):
    t = threading.Thread(target=worker)
    t.start()
    threads.append(t)

for filename in filenames:
    q.put(filename)

q.join()

for i in range(10):
    q.put(None)
for t in threads:
    t.join()
