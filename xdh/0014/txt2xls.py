#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, os.path
import re
import sys, getopt
import xlsxwriter



def txt2xls_impl(inputf, outf):
    print("inputfile is ", inputf)
    print("outfile is ", outf)
    other = ['{', '}', ',', ':', '"', '[', ']', '\t', '\n']
    t = []
    with open(inputf, 'r') as st:
        br = 0
        for s in st:
            for i in other:
                s = s.replace(i, ' ')
            if s != '' :
                t.append(s)
    
    with open(outf, 'w') as rs:
        rs.seek(0)
    
    workbook = xlsxwriter.Workbook(outf)
    worksheet = workbook.add_worksheet('student')
    row = 0
    for i in t:
        if i != '':
            st = i.split()
            st = list(filter(None, st))
            for j in range(0, len(st)):
                worksheet.write(chr(65+j)+str(row), str(st[j]))
            row += 1
    workbook.close()

def main(argv):
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv, "-h-i:-o:",["--help", "--input=","--output="])
    except getopt.GetoptError:
        print("run <filename>.py -i <inputFile> -o <outputFile>")
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print("run <filename>.py -i <inputFile> -o <outputFile>")
        if opt == '-i':
            inputfile = arg
        if opt == '-o':
            outputfile = arg

    txt2xls_impl(inputfile, outputfile)
    print("Finshed convert from text to xls\n")

if __name__ == '__main__':
    main(sys.argv[1:])
