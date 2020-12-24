"""This script moves your scrapped PDFs to the desired folders"""

import os
from os import system
from glob import glob
import shutil


def mover(unit):

    if glob(unit):
        print("\nDestination folder already exists\n")
    else:
        system("mkdir /home/gamin3/Desktop/school work/"+ unit)
        print("\nDestination folder was created successfully\n")

    dest = '/home/gamin3/Desktop/school work/' + unit

    os.chdir('/home/gamin3/Downloads')
    files = os.listdir()
    print(files)

    for i in files:
        system('mv '+ i + dest)

def test(unit):

    cwd = '/home/gamin3/Desktop/schoolWork/'
    if glob(unit):
        print("\nDestination folder already exists\n")
    else:
        system("mkdir " + cwd + unit)
        print("\nDestination folder was created successfully\n")

    dest = cwd + unit
    origin = '/home/gamin3/Downloads/'

    os.chdir(origin)
    files = os.listdir()
    print(files)
    # system("rm -r "+ unit)

    for i in files:
        print(i)
        shutil.move(origin+i , dest)

# test("SPH309")