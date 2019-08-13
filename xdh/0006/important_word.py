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
    q = pwd + "/" +res
    if os.path.isdir(dir):
        os.chdir(dir)
        for f in glob.glob("*.txt"):
            with open(f, 'r') as test:
                data = test.read()
                pattern = re.compile(u'\t|\n|\.|-|:|;|\)|\(|\?|"|#|{|}|!|\#|\*|=|\_|\/|\[|\]|\,')
                data = re.sub(pattern, ' ', data)
                data_s = data.split()
                c = collections.Counter(data_s)
                c10 = c.most_common(10)
                #print(c10)
                #for i, j in c10:
                #    print(i, j)
                with open(q, 'a+') as result:
                    result.write(f+"the top 10 important word is ")
                    result.write(str(c10))
                    result.write("\n")

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
