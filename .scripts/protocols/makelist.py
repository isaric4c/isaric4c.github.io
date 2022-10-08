#!/usr/bin/env python3
'''
Makes an html list of pdf files in a directory
Also makes a lunr search index


settings:
json format
Any file path objects can be lists for os.path.join and use '~' for user home; these object names must end with "dir" or "file"

'''
import json
import os
import re
from io import StringIO

import pandas as pd
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage

# -----------------------------
scriptpath = os.path.dirname(os.path.realpath(__file__))
# -----------------------------
with open(os.path.join(scriptpath, "settings.json")) as f:
    settings = json.load(f)
# -----------------------------
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-l', '--location', default='genomicc', choices=list(settings))
parser.add_argument('-f', '--fast', default=False, action="store_true")
args = parser.parse_args()
# -----------------------------
# fix filepaths
for s in settings[args.location]:
    if s.endswith('dir') or s.endswith("file"):
        if 'scriptpath' in settings[args.location][s]:
            settings[args.location][s] = [scriptpath if x == "scriptpath" else x for x in settings[args.location][s]]
        settings[args.location][s] = os.path.expanduser(os.path.join(*settings[args.location][s]))


# -----------------------------
def convert_pdf_to_txt(thisfile):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'  # 'utf16','utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = open(thisfile, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos = set()
    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password, caching=caching,
                                  check_extractable=True):
        interpreter.process_page(page)
    fp.close()
    device.close()
    str = retstr.getvalue()
    retstr.close()
    return str


def readpdf(thisfile):
    try:
        return convert_pdf_to_txt(thisfile)
    except:
        return ""


def get_unique_words(bigstring):
    for char in ['\ufb01', '\u00e2', '\u2021', '\u2013', '\ufb02', '\ufb02', '\ufb00', '-']:
        bigstring = bigstring.replace(char, '')
    for char in ['\t', '.', '[', ']', '(', ')', '{', '}', '"', "'"]:
        bigstring = bigstring.replace(char, ' ')
    bs = [x.strip() for x in re.split(';| |,|\n|\r', bigstring)]
    bs = list(set([x for x in bs if len(x) > 1]))
    return ' '.join(bs)


def add_pdf_to_search(thisfile):
    if not args.fast:
        searchlist.append({
            'href': os.path.relpath(thisfile, settings[args.location]['basedir']),
            'title': fixname(os.path.split(thisfile)[1]),
            'content': get_unique_words(readpdf(thisfile)),  # this is the slow bit
        })


def accept(filename):
    if filename.startswith('.') or filename.startswith('_') or filename.startswith('offline'):
        return False
    if filename.strip() in settings[args.location]['choices']['excluded']:
        return False
    for this_regex in settings[args.location]['choices']['excluded']:
        reg = re.compile(this_regex)
        if re.match(reg, filename.strip()):
            return False
    return True


def fixname(thisname):
    # return thisname.replace("_"," ").split('.')[0]
    return thisname


def makeid(thisname):
    thisid = ''.join(thisname.split())
    thisid = ''.join(thisname.split("."))
    return thisid


def is_int(val):
    try:
        num = int(val)
    except ValueError:
        return False
    return True


def getversion(thisstring):
    vlist = [x for x in thisstring.split("v") if re.match("^[0-9]", x)]
    if len(vlist) > 0:
        vsplit = [int(x) for x in vlist[0].split('.') if is_int(x)]
        return vsplit
    else:
        return [0]


def sort_by_version(thislist, rev=True):
    if len(thislist) < 2:
        return thislist
    d = {x: getversion(x) for x in thislist}
    print(d)
    maxlen = max([len(d[x]) for x in d])
    for x in d:
        while len(d[x]) < maxlen:
            d[x].append(0)
    df = pd.DataFrame.from_dict(d, orient="index")
    df['name'] = df.index
    df.sort_values(by=list(df.columns), inplace=True, ascending=[False for x in df.columns][:-1] + [True])
    return (list(df.index))


def formatdir(thisdir, depth=0):
    text = ''
    num_added = 0
    for entry in sort_by_version(os.listdir(thisdir), rev=True):
        if os.path.isdir(os.path.join(thisdir, entry)):
            num_added += 1
            # text+=("<h5 style='margin-left:{}em;'>{}:</h5><ul class='list-group'>\n{}\n</ul>\n".format(depth+1, fixname(entry), formatdir(os.path.join(thisdir, entry), depth+1)))
            text += ('''
                <div class='panel-group' id='{}'>
                    <div class='panel'>
                        <h5 style='margin-left:{}em;'>
                            <a data-toggle='collapse' data-parent='#{}' href='#collapse{}'>
                                {} &raquo;
                            </a>
                        </h5>
                        <div id="collapse{}" class="panel-collapse collapse">
                            <ul class='list-group'>{}</ul>
                        </div>
                    </div>
                </div>
                '''.format(
                makeid(entry),
                depth + 1,
                makeid(entry),
                makeid(entry),
                fixname(entry),
                makeid(entry),
                formatdir(os.path.join(thisdir, entry), depth + 1))
            )
        else:
            if accept(entry):
                num_added += 1
                if settings[args.location]['choices']['use_viewerjs']:
                    text += ('''
                        <a href='ViewerJS/#../{}'>
                            <li class='list-group-item' style='margin-left:{}em;'>{}</li>
                        </a>
                        '''.format(
                        os.path.relpath(os.path.join(thisdir, entry), settings[args.location]['basedir']),
                        depth,
                        fixname(entry))
                    )
                else:
                    text += ('''
                        <a href='{}'>
                            <li class='list-group-item' style='margin-left:{}em;'>{}</li>
                        </a>
                        '''.format(
                        os.path.relpath(os.path.join(thisdir, entry), settings[args.location]['basedir']),
                        depth,
                        fixname(entry))
                    )
                add_pdf_to_search(os.path.join(thisdir, entry))
        if num_added == 0:
            pass
            # text+=('''<li class='list-group-item' style='margin-left:{}em;'>Nothing added yet</li>'''.format(depth))
    return text


# -----------------------------

# https://codepen.io/marklsanders/pen/OPZXXv


searchlist = []

outfiletext = ""
outfiletext += ('<div class="panel-group" id="accordion" role="tablist" aria-multiselectable="true">\n')
i = 0
uncategorised = []
for d in sort_by_version(os.listdir(settings[args.location]['sourcedir'])):
    if os.path.isdir(os.path.join(settings[args.location]['sourcedir'], d)) and accept(d):
        outfiletext += ('''
            <div class="panel panel-default">
                <a role="button" data-toggle="collapse" data-parent="#accordion" href="#collapse{}" aria-expanded="true" aria-controls="collapse{}">
                    <div class="panel-heading" role="tab" id="heading{}" style="background: #f5f5f5;">
                        <h4 class="panel-title">
                          {}
                        </h4>
                    </div>
                </a>
                <div id="collapse{}" class="panel-collapse collapse" role="tabpanel" aria-labelledby="heading{}">
                        {}
                </div>
            </div>
          '''.format(
            i,
            i,
            i,
            fixname(d),
            i,
            i,
            formatdir(os.path.join(settings[args.location]['sourcedir'], d))
        ))
        i += 1
    else:
        if os.path.exists(os.path.join(settings[args.location]['sourcedir'], d)) and accept(d):
            uncategorised.append(d)
            add_pdf_to_search(os.path.join(settings[args.location]['sourcedir'], d))
outfiletext += ('</div>\n')

uncategorised_text = ""

# re-order uncategorised
for i, item in enumerate(uncategorised):
    for pinthis in settings[args.location]['choices']['pin_to_top']:
        if item.startswith(pinthis):
            print(uncategorised)
            uncategorised.insert(0, uncategorised.pop(i))
            print(uncategorised)

if len(uncategorised) > 0:
    print(uncategorised)
    uncategorised_text += ("<div class='panel panel-default' style='margin-top:1em;'><ul class='list-group'>\n")
    for entry in uncategorised:
        if accept(entry):
            highlight = ""
            for pinthis in settings[args.location]['choices']['pin_to_top']:
                if entry.startswith(pinthis):
                    highlight = " h4"
            uncategorised_text += (("\t<a href='{}'><li class='list-group-item {}'>{}</li></a>\n".format(
                os.path.relpath(os.path.join(settings[args.location]['sourcedir'], entry),
                                settings[args.location]['basedir']),
                highlight,
                fixname(entry)))
            )
            add_pdf_to_search(os.path.join(settings[args.location]['sourcedir'], entry))
    uncategorised_text += ('</ul></div>\n')
# prepend for this
outfiletext = uncategorised_text + outfiletext

with open(settings[args.location]['outputfile'], 'w') as o:
    o.write(outfiletext)

if not args.fast and settings[args.location]['choices']['makesearch']:
    with open(args.indexfile, 'w') as o:
        json.dump(searchlist, o, indent=4)

print('list made')
