#!/usr/bin/python3
import os, sys

ret = os.fork()

if ret == 0:
    print(f"child_process: pid={os.getpid()}, parent_process: pid={os.getppid()}")
elif ret > 0:
    print(f"child_process: pid={ret}, parent_process: pid={os.getpid()}")
