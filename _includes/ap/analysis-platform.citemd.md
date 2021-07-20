




# What it is

The outbreak data analysis platform exists to provide an accessible, usable data resource by linking and curating data from **clinical records**, **research studies** and **audit data** for UK patients. The platform combines trusted research environment infrastructure with >£100M of exabyte-scale computational capacity on the UK National Supercomputer. The solitary aim of the platform is to accelerate scientific understanding of new outbreaks for the beenfit of patients and the protection of the public.

# What it isn't

- It is not a viral sequence analysis platform. The excellent MRC CLIMB resource provides excellent resources and infrastructure for analysis, presentation and sharing of viral sequences. 
- It is not a replacement for public health activities. The platform will work closely with public health agencies across the 4 nations and with UK HSA, providing data feeds where useful to augment surveillance capacity, and a tried-and-tested route to engage additional analytic capacity and expertise from the academic sector.
- It is not a replacement for existing TREs. The analysis platform will provide curated data feeds to TREs across the UK to facilitate and supplement data held elsewhere.

# Design of the platform

## Data held

The platform already contains a unique aggregation of UK sovereign data assets, including the complete data resources of the ISARIC4C/CO-CIN, GenOMICC, PHOSP and UK-CIC studies, together with viral sequence data from COG-UK, and linkage to NHS clinical records and structured clinical audit data. This creates a unique opportunity to combine clinical, biological, genomics and virology research in as secure, openly-accessible framework. Manual curation of these linked datasets, in a single platform, is a key step to maximise data quality and usability.

## Compute power

- processing power
- 2.5Pb of storage
- GPU arrays for massively-parallel applications such as genomics and image analysis
- API structure for real-time data sharing with other trusted research environments across the UK
- data pipelines to supply surveillance feeds to public health

## Structure

There are two routes of access to the analysis platform (@fig:structure):

1. NHS Trusted Research Environment (Safe Haven) for access to personal clinical data and data collected without explicit consent.
2. Rapid-access flexible compute for access to non-disclosive research data collected with explicit consent.

Within both of these environments there are two levels of access, governed by the data contributors:

1. Publishable "open access" data which any user can use and report as they wish, according to data protection and privacy rules;
2. Embargoed active research data, shared by academic investigators and available for linked analysis but not for publication without agreement from all contributors.

This design is intended to build trust in order to encourage immediate contributions of research data from academic collaborators. It makes data available immediately for discovery, whilst protecting the rights of data creators and contributors.

![Structure of the Outbreak Analysis Platform](https://isaric4c.net/img/ap/i4c-analysis-platform-updated.png){#fig:structure width=80%}


# Research outputs

By generating, integrating and analysing clinical, biological, genetic and virological data on patients with Covid-19 in UK hospitals, the outbreak analysis platform has facilitated research that:

- provided essential weekly updates to SAGE that guide the public health response [isaric4c.net/reports/](https://isaric4c.net/reports/), 
- identified host genetic mechanisms of disease, [@pairocastineirageneticmechanismscritical2021]
- quantified the role of age, comorbid illness and obesity in disease severity,[@dochertyfeatures201332020] 
- created the global standard ISARIC4C score for prognostication [isaric4c.net/risk](isaric4c.net/risk),[@knightriskstratificationpatients2020] 
- determined the impact of long Covid following hospitalisation[@groupphysicalcognitivemental2021]
- identified the substantial effect of nosocomial transmission of Covid-19 within hospitals [SPI-M/SAGE report](https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/961210/S1056_Contribution_of_nosocomial_infections_to_the_first_wave.pdf),
- provided key evidence underlying the choice of therapeutic agents for clinical trials[@pairocastineirageneticmechanismscritical2021; @thwaitesinflammatoryprofilesspectrum2021]
- provided real world data on vaccine effectiveness and failure (SAGE 87 Egan et al,  Egan et al.) 
- observed data supporting identification of high risk groups for vaccination (highlighted in No10 briefing)
- described the complications of Covid-19 in hospitalised patients.[@drakecharacterisationinhospitalcomplications2021]

# Governance of the platform

## National core studies

The platform is funded by UKRI and the National Core Studies programme (Data and Connectivity).

## Advisory committee

A UK-wide advisory committee, initially convened by HDR UK to solve data linkage problems in Covid research, will provide guidance on all aspects of platform management and delivery. The committee comprises representation from public health agencies in the 4 nations of the UK, representatives of key studies, TREs and data resources, and representatives of government and industry. 

## Executive group

An executive committee will be charged with managing resources and delivering on the goals set by the advisory committee.

# Current data content

This platform now serves as a hub for a coordinated UK national research response to COVID-19. Data are included from:

- ISARIC4C tier 0: (unconsented) prospective clinical data from 215,825 cases
- ISARIC4C tiers 1 and 2: serial multiomic assays from research samples of blood, respiratory secretions, urine, and stool from 2,401 cases
- COG-UK: (unconsented) summary variant data from COG-UK viral sequencing study is already included for matched patients
- GenOMICC study complete data: microarray and whole genome sequence data from 13,868 cases
- PHOSP complete data: follow-up clinical and biological data generated by the Post-Hospitalisation for COVID-19 follow-up study (1,075 cases)
- UK-CIC: deep immunological phenotyping data from across the UK Coronavirus Immunology Consortium, using ISARIC4C samples and local collections.

Research data within the analysis platform is already linked to:

- NHS Scotland primary, secondary care and death records
- NHS Digital health records data

In future, plans are in place to transfer data to link with:

- ICNARC and SICSAG critical care audit databases
- NIMS National Immunisation Dataset
- Pillar 1 testing
- Pillar 2 testing
- ONS














\newpage

# References









