#!/usr/bin/python3

import subprocess

size = 1000000

mem_before = subprocess.run('free')
print(f'before: {mem_before}')

array = [0] * size

mem_after = subprocess.run('free')
print(f'after: {mem_after}')