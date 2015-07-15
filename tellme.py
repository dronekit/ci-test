from __future__ import print_function
import multiprocessing as mp
import subprocess
from multiprocessing import Pool
import time
import sys

def win_get_core():
    try:
        import winappdbg
        return int(winappdbg.win32.kernel32.GetCurrentProcessorNumber())
    except:
        return 0

print('CPU COUNT', mp.cpu_count())

print("main process initializing", mp.current_process())
print('main process on CPU', win_get_core())

from subprocess import Popen

import os

print('starting p1')
p2 = Popen(['start', '/affinity', '0x1', '/b', '/wait', '/realtime', sys.executable, 'whatcore.py'], shell=True)
p2.wait()
print('p1', p2.returncode)

print('starting p2')
p2 = Popen(['start', '/affinity', '0xe', '/b', '/wait', '/realtime', sys.executable, 'whatcore.py'], shell=True)
p2.wait()
print('p2', p2.returncode)

print('starting p2')
p2 = Popen(['start', '/affinity', '0xc', '/b', '/wait', '/realtime', sys.executable, 'whatcore.py'], shell=True)
p2.wait()
print('p2', p2.returncode)

print('starting p2')
p2 = Popen(['start', '/affinity', '0xd', '/b', '/wait', '/realtime', sys.executable, 'whatcore.py'], shell=True)
p2.wait()
print('p2', p2.returncode)

print('starting p2')
p2 = Popen(['start', '/affinity', '0x1', '/b', '/wait', '/realtime', sys.executable, 'whatcore.py'], shell=True)
p2.wait()
print('p2', p2.returncode)

print('done')
