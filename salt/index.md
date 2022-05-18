---
title: 'Summary Analysis of Laboratory Tests (SALT)'
layout: 'page'
---

<!--
Contributors
Iain Jones

Clark Russel
Maaike Swets
Geert Groenveld
Calum Semple

Louisa Pollock
Kenneth Baillie

build:
pandoc index.md -o pdf
-->


# ISARIC4C Incidence series study of elevated liver transaminases

## Background 

A series of cases of severe hepatitis in young children was recognised in central Scotland in March 2022. The aetiology is unknown but an infection or co-infection is a strong possibility. It is possible that this outbreak has been more widespread. In particular, milder, self-limiting disease may not have been recognised. 

This analysis is being conducted under instruction from Public Health.
Please visit [this page for information about recruiting new patients to the ISARIC CCP-UK](https://isaric4c.net/hepatitis)


## Aim

To determine if an increase in the proportion of elevated transaminases has occurred, where, and over what period. 

## Method

A rapid, pragmatic survey of clinically-measured transaminase levels. 
d
## Script

We have written a script to read through a table of blood results and create a summary table in the right format for this analysis. The script works even if there are tens of millions of lines, as long as the column headers match. 

The script is written in a computing language called python. Because python doesn't come pre-installed on windows computers, we've bundled our script with a python version that can be used without any installation or special permissiona.

OPERATING SYSTEM | DOWNLOAD LINK
----- | ------
Windows (standalone) | [download_windows](AST_ALT_counter_win.zip)
Windows (script only) | [download_script](AST_ALT_counter.zip)
Mac/Linux | [download_script](AST_ALT_counter.zip)

To read more about the script, please see the [README.md file](code/README)

## Data collection

In order to comply with information governance requirements, eliminate the risk of confidential disclosure, and make use of routine lab data, the following summary data will be collected in [csv](template.csv) format from hospitals:

We will count the number of *hospital inpatients* tested for blood levels of AST or ALT for whom the result was >200iu/l on at least one occasion, and the total number of patients for whom AST or ALT was measured. We will also calculate the mean and variance of these measurements. This will be done for

- each month from Jan 2018 and March 2022 to the present
- each age bracket in this list: <3wks, 3wks-5y, 6-10y, 11-16y, 17-30y, 31-50y, 51-70y, >70

<!--
\* Please use the same reference range for all age groups: The reference range for your laboratory at the time of the test, for patients aged 5yrs. e.g. If the upper end of reference range #for AST in a 5-year-old was 50 iu/ml in March 2018, count all patients with AST > 50 iu/ml for that month.
-->

Where the same patient has more than one result, the first result over the threshold is counted, or the first result from that patient, if no results over the threshold are present.


## Sending data

If you are sending data from multiple hospitals, please use a separate file for each one.

Please send your *summary data files only* to this email address: 

[ccp@ed.ac.uk](mailto:ccp@ed.ac.uk)

Please also include the following details so that we can credit you appopriately with your contribution:

- location of hospital
- institutional email addresses of contributing scientists
























