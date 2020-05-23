#!/usr/bin/python3
import subprocess
p,q = subprocess.getstatusoutput("ls")
print(q)
