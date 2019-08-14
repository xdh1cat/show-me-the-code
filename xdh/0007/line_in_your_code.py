#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, os.path
import re
import sys, getopt
import glob
import collections
import numpy as np


def important_w(dir, res):
    pwd = os.getcwd()
    res = pwd + "/" + res
    with open(res, 'a+') as result:
        result.write("fname code space comment\n")
    if os.path.isdir(dir):
        os.chdir(dir)
        for f in glob.glob("*"):
            #TODO
            if not os.path.isabs(f):

                with open(f, 'r') as test:
                    data = test.readlines()
                    c = 0
                    space = 0
                    cmd = 0
                    pcmd = re.compile('^\s*#.*|\s*//.*')
                    for l in data:
                        c += 1
                        if len(l.split()) == 0:
                            space += 1
                        if pcmd.match(l) != None:
                            cmd += 1
                    code = c - cmd - space
                #print(c, space, cmd)
                    with open(res, 'a+') as result:
                        result.write(f+ " "+ str(code) + "  " + str(space) + "  " + str(cmd) + "\n")
                        #result.write(str(code)+"        "+str(space)+"      "+str(cmd)+"\n")

def main(argv):
    try:
        opts, args = getopt.getopt(argv, "-h-i:o:",["--help", "--input=", "--output="])
    except getopt.GetoptError:
        print("run <filename>.py -i <inputFile> -s <size>")
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print("run <filename>.py -i <inputFile> -s <size>")
        if opt == '-i':
            inputfile = arg
        if opt == '-o':
            outputfile = arg

    with open(outputfile, 'w') as resf:
        resf.seek(0)

    important_w(inputfile, outputfile)

if __name__ == '__main__':
    main(sys.argv[1:])
