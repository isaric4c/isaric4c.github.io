#!/opt/local/bin/python
# -*- coding: UTF-8 -*-

import os
import io
import json
import requests
import subprocess
import pandas as pd
#-----------------------------
def get_text(filepath):
    '''return stripped plain text from file'''
    with open(filepath) as f:
        c = f.read().strip()
    return c
#-----------------------------
i4c_source_url = "https://raw.githubusercontent.com/SurgicalInformatics/ccp_recruitment_flat_file/master/ccp_recruit_daily.csv"
g_source_url = "https://genomicc.roslin.ed.ac.uk/GCC/json-summary"
#-----------------------------
numdir = "numbers"
t1 = os.path.join(numdir, "crf_count.txt")
m = os.path.join(numdir, "multiomics_count.txt")
g = os.path.join(numdir, "genomicc_count.txt")
c = os.path.join(numdir, "cog_count.txt")
p = os.path.join(numdir, "phosp_count.txt")
h0 = os.path.join(numdir, "hospitals_tier0.txt")
h2 = os.path.join(numdir, "hospitals_tier2.txt")
#-----------------------------
imgdir = "img/ap/"
sourcefiles = [os.path.join(imgdir, x) for x in [
        "i4c-map-source.svg",
        "i4c-map-data-source.svg",
        "i4c-analysis-platform-source.svg"
    ]
]
#-----------------------------
gsource=requests.get(g_source_url).content
gdic = json.loads(gsource)

isource=requests.get(i4c_source_url).content
df=pd.read_csv(io.StringIO(isource.decode('utf-8')))

with open(t1,"w") as o:
    o.write("{:,d}".format(int(df["n_in_all_tiers"][0])))
with open(m,"w") as o:
    o.write("{:,d}".format(int(df["n_tier1"][0]+df["n_tier2"][0])))
with open(g,"w") as o:
    o.write("{:,d}".format(int(gdic["total"])))
with open(c,"w") as o:
    o.write("{:,d}".format(int(21230)))
with open(p,"w") as o:
    o.write("{:,d}".format(int(1075)))
with open(h0,"w") as o:
    o.write("{:,d}".format(int(253)))
with open(h2,"w") as o:
    o.write("{:,d}".format(int(53)))
#-----------------------------

replacedict = {
    "151,123": "{}".format(get_text(t1)),
    "2,526": "{}".format(get_text(m)),
    "8,213": "{}".format(get_text(g)),
    "21,234": "{}".format(get_text(c)),
    "1,077": "{}".format(get_text(p)),
    "253": "{}".format(get_text(h0)),
    "53": "{}".format(get_text(h2)),
}

for sourcefile in sourcefiles:
    outputfile = sourcefile.replace("-source.svg", "-updated.svg")
    with open(sourcefile) as f:
        svgtext = f.read()
    for x in replacedict:
        svgtext = svgtext.replace(x,replacedict[x])
    with open(outputfile,"w") as o:
        o.write(svgtext)











