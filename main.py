#!/bin/python3

#Build by DanLP6 v.a.0.1

import sys
import os
from pathlib import Path

try:
	import requests
	import argparse
	import ast
except:
	req=Path('requiremtnts.txt').read_text()
	print("requirements to run this program are\n" + req)

udb="1"

if udb=="1":
	branch="https://schooldanlp6.github.io/SimpleBinaryPackageManager6/"

if udb=="0":
	print("add a branch. with the protocol current support is https costum branches arent supported and save it in a file branches.txt")
	branch=input()

print("Branch is " + branch)

try:
	funktion = sys.argv
	funktionstr = 0
except:
	print("Well done you have succsesfully seen the help page \nThis is the simple binary (and app image) package manager by DanLP6 \nTo install type main.py install <package>")

funktionpkgnr = funktion.index("install",1,10)
funktionpkgnr = funktionpkgnr + 1
funktionpkg = funktion[funktionpkgnr]

if "install" in funktion:
	print ("Downloading...")
	purldw = branch + funktionpkg
	pr = requests.get(purldw, allow_redirects=True)
	open(funktionpkg, 'wb').write(pr.content)

import os
script = """
echo $0
ls -l
echo done
"""
os.system("bash -c '%s'" % script)
