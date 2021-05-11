#!/opt/local/bin/python
# -*- coding: UTF-8 -*-

import os
import re

outputdir = os.path.expanduser("~/Dropbox/6_websites/isaric4c.github.io/_outputs")
outfile = "outputs.md"

#-------
def getyaml(y):
    yml = {}
    for line in y:
        line = line.split(": ")
        if len(line)>1:
            yml[line[0]]=line[1]
        else:
            yml[line[0]]=""
    return yml

def readheader(filecontents):
    '''
        Read a valid markdown header
        Input is full text of file
        Returns list of header items + full text of remainder
    '''
    t = filecontents.strip()
    t = t.replace('\r','\n')
    header = []
    remainder = filecontents
    lines = [x for x in t.split('\n')] # don't strip because indentation matters
    if lines[0]=='---':
        h1 = re.findall( '---[\s\S]+?---',filecontents)
        h2 = re.findall( '---[\s\S]+?\.\.\.',filecontents)

        if len(h1)>0 and len(h2)>0:
            #print ("both yaml header formats match! Taking the shorter one")
            if len(h1[0]) < len(h2[0]):
                h=h1[0]
                #print ("Choosing ---/---\n", h)
            else:
                h=h2[0]
                #print ("Choosing ---/...\n", h)
        elif len(h1)>0:
            h = h1[0]
        elif len(h2)>0:
            h = h2[0]
        if len(h)>0:
            header = h.split('\n')[1:-1]
        remainder = filecontents.replace(h,'')
    return header, remainder
#-------


outputfiles = [x for x in os.listdir(outputdir) if not x.startswith(".") and not x.startswith("Icon") and x.endswith(".md")]

outdict = {}
for filename in outputfiles:
    thispath = os.path.join(outputdir, filename)
    with open(thispath) as f:
        text = f.read()
    h, r = readheader(text)
    y = getyaml(h)
    w = int(y["weight"])
    outdict[r]=w

with open(outfile,"w") as o:
    for k,v, in [(k, outdict[k]) for k in sorted(outdict, key=outdict.get, reverse=True)]:
        print (v)
        o.write("{}\n".format(k))




