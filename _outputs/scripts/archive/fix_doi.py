#!/opt/local/bin/python
# -*- coding: UTF-8 -*-

import os
import re

outputdir = os.path.expanduser("~/Dropbox/6_websites/isaric4c.github.io/_outputs")

files = [x for x in os.listdir(outputdir) if not x.startswith(".")]

for thisfile in files:
    filepath = os.path.join(outputdir, thisfile)
    if os.path.isdir(filepath):
        continue
    print (thisfile)
    with open(filepath) as f:
        lines = f.readlines()
        done = False
        for line in lines:
            if line.startswith("doi:"):
                done = True
        if done:
            continue
        for i,line in enumerate(lines):
            doi = re.findall(r"\]\(https:\/\/doi\.org\/.+?\)\n", line)
            if len(doi)>0:
                doi = doi[0][2:-2]
                lines[i] = lines[i].replace(doi, '{{page.doi}})')
                lines = lines[:4] + ["doi: {}\n".format(doi)] + lines[4:]
        newcontents = "".join(lines)
    print (newcontents)
    if True:
        with open(filepath, "w") as o:
            o.write(newcontents)
