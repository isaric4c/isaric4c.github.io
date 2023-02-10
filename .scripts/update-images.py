#!/opt/local/bin/python
# -*- coding: UTF-8 -*-

import os
import io
import json
import requests
import subprocess
import pandas as pd
#-----------------------------
i4c_source_url = "https://raw.githubusercontent.com/SurgicalInformatics/ccp_recruitment_flat_file/master/ccp_recruit_daily.csv"
g_source_url = "https://genomicc.roslin.ed.ac.uk/GCC/json-summary"
#-----------------------------
t1 = 10
m = 10
g = 10
c = 10
p = 10
h0 = 10
h2 = 10
#-----------------------------
imgdir = "img/ap/"
sourcefiles = [os.path.join(imgdir, x) for x in [
        "i4c-map-source.svg",
        "i4c-map-data-source.svg",
        "i4c-analysis-platform-source.svg",
    ]
]
#-----------------------------
gsource=requests.get(g_source_url).content
gdic = json.loads(gsource)

isource=requests.get(i4c_source_url).content
df=pd.read_csv(io.StringIO(isource.decode('utf-8')))
#-----------------------------

replacedict = {
    "151,123": "{}".format(12),
    "2,526": "{}".format(12),
    "8,213": "{}".format(12),
    "21,234": "{}".format(12),
    "1,077": "{}".format(12),
    "253": "{}".format(12),
    "53": "{}".format(12),
    "500,000": "{}".format(12),
}

for sourcefile in sourcefiles:
    outputfile = sourcefile.replace("-source.svg", "-updated.svg")
    with open(sourcefile) as f:
        svgtext = f.read()
    for x in replacedict:
        svgtext = svgtext.replace(x,replacedict[x])
    with open(outputfile,"w") as o:
        o.write(svgtext)

'''
now run: 
inkscape --export-type="pdf" img/ap/*-updated.svg
inkscape --export-type="png" img/ap/*-updated.svg
'''








