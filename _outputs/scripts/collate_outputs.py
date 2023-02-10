#!/opt/local/bin/python
# -*- coding: UTF-8 -*-

import os
import re
import oyaml as yaml
from numpy import mean
from pyaltmetric import Altmetric

scriptpath = os.path.dirname(os.path.realpath(__file__))
os.chdir(scriptpath)
sourcedirectory = "../"

def readheader(filecontents):
    '''
        Read a valid markdown header
        Input is full text of file
        Returns list of header items + full text of remainder
    '''
    t = filecontents.strip()
    t = t.replace('\r','\n')
    h = ""
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
        remainder = filecontents.replace(h,'')
    return h, remainder

def replace_liquid(thistext, ymldic):
    '''
        Replace liquid-style {{page.doi}} tags with the relevant bit from yaml header
    '''
    lm = "\{\{ *page\..*?\}\}"
    for thismatch in re.findall(lm, thistext):
        key = thismatch.replace("{{","").replace("}}","").replace("page.","").strip()
        try:
            ymldic[key]
        except:
            continue
        thistext = thistext.replace(thismatch, ymldic[key])
    return thistext

def get_altmetric(thisdoi):
    a = Altmetric()
    alt = a.doi(thisdoi.split("doi.org/")[1])
    return int(alt["score"])

def slugify(value, allow_unicode=False):
    value = str(value)
    value = re.sub(r'[^\w\s-]', '', value.lower())
    return re.sub(r'[-\s]+', '-', value).strip('-_')

def replace_imagepath(thistext, root="../../"):
    figureformat = '!\[.*?\]\(.*?\).*?\n'
    figures_found = re.findall(figureformat, thistext)
    for f in figures_found:
        path = f.split("(")[1]
        path = path.split(")")[0]
        ps = 0
        if path.startswith("/"):
            ps = 1
        g = f.replace(path, os.path.abspath(os.path.join(root, path[ps:])))
        thistext = thistext.replace(f, g)
    return thistext

outputfiles = [x for x in os.listdir(sourcedirectory) if not x.startswith(".") and not x.startswith("Icon") and x.endswith(".md") and not x.startswith("_")]

weightdict = {}
outdict = {}
filedict = {}
altdict = {}
projectdict = {}
listdict = {}
for filename in outputfiles:
    print (filename)
    thispath = os.path.join(sourcedirectory, filename)
    with open(thispath) as f:
        text = f.read()
        y, r = readheader(text)
        try:
            gen = yaml.safe_load_all(y)
            for generator_item in gen:
                yml = generator_item
                break
        except:
            yml = ""
            continue
        altscore = ""
        ref = ""
        if "doi" in yml:
            try:
                a = get_altmetric(yml["doi"])
                altdict[yml["doi"]] = a
                altscore = "Altmetric score: {}".format(a)
            except:
                pass
            ref = "[{}]".format(yml["doi"])
            try:
                filedict[yml["doi"]]
                print ("***Duplicate doi***\n\t{}\n\t{}\n\t{}\n".format(yml["doi"], filedict[yml["doi"]], filename))
            except:
                pass
            filedict[yml["doi"]] = filename
        if "projects" in yml:
            for project in yml["projects"]:
                try:
                    projectdict[project]
                except:
                    projectdict[project]=[]
                projectdict[project].append(filename)
        r = replace_liquid(r, yml)
        r = replace_imagepath(r)
        weightdict[filename] = yml["weight"]
        outdict[filename] = "# {}\n\n".format("\n\n".join([
                yml["title"].strip(),
                r.strip(),
                str(altscore) + ref,
                ])
            )
        listdict[filename] = "- {}".format(yml["title"].strip())
        if "doi" in yml:
            listdict[filename] += (" [{}]".format(yml["doi"]))

for project in projectdict:
    textfile = os.path.join("reports", "{}.md".format(slugify(project)))
    listfile = os.path.join("reports", "{}_list.md".format(slugify(project)))
    with open(textfile,"w") as o:
        with open(listfile,"w") as p:
            o.write("**ISARIC4C has produced {} papers with an average altmetric score of {:.0f}.**\n\n".format(len(altdict), mean(list(altdict.values()))))
            for k,v, in [(k, weightdict[k]) for k in sorted(weightdict, key=weightdict.get, reverse=False)]:
                if k in projectdict[project]:
                    o.write("{}\n".format(outdict[k]))
                    p.write("{}\n".format(listdict[k]))





