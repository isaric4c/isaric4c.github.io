import sys

import pandas as pd

try:
    url = "https://www.dropbox.com/s/t70kmn9lri6jl47/master_author_list.xlsx?dl=1"
    df = pd.read_excel(url)
except Exception as e:
    print(e)
    sys.exit()
    
print("Successfully loaded from Dropbox into Pandas dataframe")

with open("./about/authors.md", "w") as fp:
    sys.stdout = fp

    print("""---
title: 'About'
layout: 'page'
---


ISARIC4C Consortium Authors
=======

The ISARIC4C author list aims to respect contributions to the
Protocol, MRC and DHSC grant applications and those who since have made
a substantive academic contribution to delivering the CCP-UK, which
includes CO-CIN related activity (described in the protocol as CCP-UK
Tier Zero activity).

This document is managed by the co-leads of the ISARIC4C.
We hope we have done everything we can to recognise your contribution.
Please email ccp@liverpool.ac.uk if there you spot any omission.

The **Protocol Authors** are: J Kenneth Baillie, Malcolm (Calum) G Semple,
Gail Carson, Peter Openshaw, Jake Dunning, Laura Merson, Clark D
Russell, Maria Zambon, Meera Chand, Richard Tedder, Saye Khoo, Peter
Horby, Lance CW Turtle, Tom Solomon, Samreen Ijaz, Tom Fletcher, Massimo
Palmarini, Antonia Ho, Nicholas Price.

ISARIC4C Investigators
--------
""")

    previous_contribution = None
    names = []

    for ind, row in df.iterrows():
        if isinstance(row["supplemental_labels"], str):
            print(f"*{row['contribution']}*: {row['Name']}.\n")
            continue

        if str(previous_contribution) == str(row["contribution"]):
            names.append(row["Name"])

        else:
            if names:
                print(f"*{previous_contribution}*:" + "\n" + ",\n".join(names) + ".\n")
            names = []
            previous_contribution = row["contribution"]

    print(f"*{previous_contribution}*:" + "\n" + ",\n".join(names) + ".\n")

    print("## Acknowledgements")
    print(
        "This work uses data provided by patients and collected by the NHS as part of their care and support #DataSavesLives. We are extremely grateful to the 2,648 frontline NHS clinical and research staff and volunteer medical students, who collected this data in challenging circumstances; and the generosity of the participants and their families for their individual contributions in these difficult times. We also acknowledge the support of Jeremy J Farrar and Nahoko Shindo.")
