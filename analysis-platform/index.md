# ISARIC 4C consortium

The [ISARIC Coronavirus Clinical Characterisation Consortium
(4C)](https://isaric4c.net) is the largest observational study of
COVID-19 anyhwere in the world. Data from this study are held on an
integrated analysis platform, comprising:

-   prospective clinical data from 59246 cases
-   serial samples of blood, respiratory secretions, urine, and stool
    from 2159 cases
-   the [GenOMICC study](https://genomicc.org/uk): whole genome sequence
    data from 2758 cases

It is built on top of existing pandemic preparedness infrastructure,
designed, established, maintained and tested during the interpandemic
period (fig. 1),^1^ and harmonised across the world.^2^ It is an
open-access national resource: we have already shared data on 59246
participants and 4273 samples with 26 external groups.

![Figure 1: ISARIC 4C
study](/Users/jkb/Dropbox/6_websites/baillielab.net/docs/img/isaric4c/ISARIC_UKmap.pdf){#fig:map
width="50%"}

# Principles

The success of ISARIC 4C is largely due to the following foundational
principles:

-   no group, funder, collaborator or other party will have exclusive
    access to data or samples
-   consortium resources (samples, data and funds) will be prioritised
    according to likelihood of rapid impact on the COVID-19 pandemic
-   all data generated using ISARIC 4C resources is shared in a
    machine-readable format within the Integrated Analysis Platform

# Integrated Analysis Platform

## Back-end infrastructure

ISARIC 4C has developed a clinical and research data integration
platform to facilitate integrative analyses of multi-omic, serial
disease profiling, stratified by clinical phenotype and outcome. This is
hosted on nationally-leading, exabyte-scale computational infrastructure
including state-of-the-art security systems for protection of
identifiable data, and high-performance CPU/GPU computing (the Edinburgh
Parallel Compute Centre, EPCC, and ARCHER/ARCHER2).

This platform will serve as the hub for a coordinated UK national
research response to COVID-19.

## Earning trust from data contributors

The default position is that data are contributed under embargo,
prohibiting publication or general release until authorised by the data
contributor. All contributors will agree to abide by this rule in good
faith. Embargoed data will be available to other contributors during the
embargo period, and will be released into the open analysis platform at
or before the time of the first pre-print report.

A critical determinant of success is building sufficient trust among
contributors to ensure that data are contributed in an accessible format
as early as possible. Data sharing within the ISARIC 4C consortium
continues to have the support and goodwill of contributors, because: -
there is a palpable urgency created by the COVID-19 crisis; - the
platform has earned the trust of contributors and will maintain it by
enforcing embargo rules; - there is a clear expectation from patients,
the public, funders and government; - there is primary benefit to data
contributors to gain access to other unpublished data and analysis
platforms.

## Open analysis platform for deidentified data

The analysis platform will be used to provide itegrated analyses of
genetic associations with multiple phenotypes,^3^ functional
genomics,^4^ and multi-omics critical illness trajectories,^5^ within
the largest clinical study of COVID-19 anywhere in the world.^6^

![Figure 2: Overlapping data for surviving members of the ISARIC 4C
cohort.](/Users/jkb/Dropbox/4_projects/isaric4c/images/analysis_platform.png){#fig:dataplatform}

The platform will host overlapping datasets from across the UK.
Individual patient consent enables sharing of linked whole-genome
sequence data, whole-blood transcriptomics, proteomics, cytokine
measurements, viral load and sequence, and clinical data.

Providing clean, linked, deidentified data in a format that is easily
accessible to researchers from a range of backgrounds requires staff
with a high level of skill in clinical epidemiology, data science, and
software engineering. Data will be systematically cleansed and linked,
missing data completed where possible, and presented to users through
three interfaces:

1.  a user-friendly browsable interface enabling data selection and
    subgrouping through dropdown menus to subset patient populations by
    clinical and biological data and run *de novo* GWAS analyses using a
    GPU platform (GOLEM, Tenesa group), multivariable regression,
    propensity-matching and unsupervised clustering.

2.  flexible analysis through bespoke, secure virtual machines operated
    through a command line interface providing access to R, Python, and
    other software as required by the user.

3.  a limited, anonymised, downloadable dataset comprising key variables
    from all participants.

Deidentified data will be available openly to *bona fide* researchers
for unrestricted analyses

## Data safe haven

A linked, secure NHS data safe haven will provide access to identifiable
data, and data collected without individual patient consent, for
qualified, approved researchers performing research to improve patient
care. This incorporates full ISARIC COVID case report forms for 46,000
patients, together with health records linkage (CAG section 251 and PBPP
approvals in place).

This will enable detailed, rich clinical analyses with corrections for
confounding and bias caused by social factors, comorbid illness and
medications, and opens a range of detailed information to characterise
acute disease using clinical measurements acquired from electronic
health records.

# References {#references .unnumbered}

::: {#refs .references}
::: {#ref-DunningOpensourceclinical2014}
1.Dunning, J.W., Merson, L., Rohde, G.G.U., Gao, Z., Semple, M.G., Tran,
D., Gordon, A., Olliaro, P.L., Khoo, S.H., Bruzzone, R., Horby, P.,
Cobb, J.P., Longuere, K.-S., Kellam, P., Nichol, A., Brett, S., Everett,
D., Walsh, T.S., Hien, T.-T., Yu, H., Zambon, M., Ruiz-Palacios, G.,
Lang, T., Akhvlediani, T., ISARIC Working Group 3, ISARIC Council,
Hayden, F.G., Marshall, J., Webb, S., Angus, D.C., Shindo, N., van der
Werf, S., Openshaw, P.J.M., Farrar, J., Carson, G. & Baillie, J.K. Open
source clinical science for emerging infections. *The Lancet Infectious
Diseases* **14**, 8--9(2014).
:::

::: {#ref-AkhvledianiGlobaloutbreakresearch2020a}
2.Akhvlediani, T., Ali, S.M., Angus, D.C., Arabi, Y.M., Ashraf, S.,
Baillie, J.K., Bakamutumaho, B., Beane, A., Bozza, F., Brett, S.J.,
Bruzzone, R., Carson, G., Castle, L., Christian, M., Cobb, J.P.,
Cummings, M.J., D'Ortenzio, E., Jong, M.D. de, Denis, E., Derde, L.P.G.,
Dobell, E., Dondorp, A.M., Dunning, J.W., Everett, D., Farrar, J.,
Fowler, R., Gamage, D., Gao, Z., Gomersall, C.D., Gordon, A.C., Haniffa,
R., Hardwick, H., Hashmi, M., Hayat, M., Hayden, F.G., Ho, A., Horby,
P., Horby, P.W., Jamieson, N., Jawad, I., John, M., Kennon, K.,
Khaskheli, S., Khoo, S.H., Lang, T., Lee, J., Ling, L., Marshall, J.C.,
Memon, M.I., Mentré, F., Merson, L., Moore, S., Murthy, S., Nichol, A.,
O'Donnell, M.R., Olliaro, P.L., Olliaro, P., Openshaw, P.J., Parke, R.,
Pereira, R., Plotkin, D., Pritchard, M., Rabindrarajan, E.,
Ramakrishnan, N., Richards, T., Ruiz-Palacios, G.M., Russell, C.D.,
Scott, J.T., Semple, M.G., Shindo, N., Sigfrid, L., Somers, E.C., Taqi,
A., Turtle, L., Thevarajan, I., Vijayaraghavan, B.K.T., Udayanga, I.,
Werf, S. van der, Vatrinet, R., Vecham, P.K. & Webb, S. Global outbreak
research: Harmony not hegemony. *The Lancet Infectious Diseases* **0**,
(2020).
:::

::: {#ref-Canela-Xandriatlasgeneticassociations2018}
3.Canela-Xandri, O., Rawlik, K. & Tenesa, A. An atlas of genetic
associations in UK Biobank. *Nature Genetics* **50**, 1593--1599(2018).
:::

::: {#ref-fantom5_2014}
4.Forrest, A. R. R., Kawaji, H., Rehli, M., Baillie, J.K., et al A
promoter-level mammalian expression atlas. *Nature* **507**,
462--470(2014).
:::

::: {#ref-NeytonMultiomicdefinitiongeneralizable2019}
5.Neyton, L., Zheng, X., Skouras, C., Wilson, A.B., Gutmann, M.U., Yau,
C., Uings, I.J., Rao, F.V., Nicolas, A., Marshall, C., Wilson, L.-M.,
Baillie, J.K. & Mole, D.J. Multiomic definition of generalizable
endotypes in human acute pancreatitis. *bioRxiv*
539569(2019).doi:[10/gf2zwn](https://doi.org/10/gf2zwn)
:::

::: {#ref-DochertyFeatures20133patients2020}
6.Docherty, A.B., Harrison, E.M., Green, C.A., Hardwick, H.E., Pius, R.,
Norman, L., Holden, K.A., Read, J.M., Dondelinger, F., Carson, G.,
Merson, L., Lee, J., Plotkin, D., Sigfrid, L., Halpin, S., Jackson, C.,
Gamble, C., Horby, P.W., Nguyen-Van-Tam, J.S., Ho, A., Russell, C.D.,
Dunning, J., Openshaw, P.J., Baillie, J.K. & Semple, M.G. Features of
200.167em133 uk patients in hospital with covid-19 using the isaric who
clinical characterisation protocol: Prospective observational cohort
study. *BMJ (Clinical research ed.)* **369**, m1985(2020).
:::
:::
