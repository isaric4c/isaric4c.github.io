---
layout: home
title: ISARIC4C consortium
description: The UK ISARIC Coronavirus Clinical Characterisation Consortium.
intro_image: "https://baillielab.net/img/isaric4c/ISARIC_UKmap.svg"
intro_image_absolute: false
intro_image_hide_on_mobile: false
special_command: "onload='updatePatientCounts();'"

---

# ISARIC4C (Coronavirus Clinical Characterisation Consortium)

We are a UK-wide consortium of doctors and scientists committed to answering urgent questions about COVID-19 quickly, openly, and for the benefit of all.

- how long are people infectious, and what body fluids are infectious?
- what puts people at higher risk of severe illness?
- what is the best way to diagnose the disease?
- who should we treat early with drugs, and which drugs cause harm?
- does the immune system in some patients do more harm than good?
- what other infections(such as pneumonia or flu) happen at the same time?


Over the last 8 years we have been preparing for such a major outbreak worldwide [International Severe Acute Respiratory Infection Consortium Clinical Characterisation Protocol](https://isaric.net/ccp); our team deployed immediately and has been collecting data and samples since the first cases were reported in the UK.

## Funding

ISARIC4C is funded by two major awards from UK Reasearch and Inovation (UKRI) and The National Institute For Health Research (NIHR).
A grant from UKRI Medical Research Council with a total value of £5.9M to JK Baillie (PI), University of Edinburgh; MG Semple, University of Liverpool; and P Openshaw, Imperial College London (co-leads). Full list of [investigators and specific deliverables](about/structure).
A grant from NIHR with a current value of £4.9M to MG Semple (CI), University of Liverpool; AD Docherty, University of Edinburgh, and CA Green, University of Birmingham.
We share data and samples to get answers as fast as possible. We will not end this outbreak sitting on a biobank; our intention is to use every drop of every sample, now, to have the biggest possible impact on the COVID-19 crisis. Any investigators with the ability to contribute can [access our data and samples](sample_access). The ISARIC-4C study provides a foundation for other studies, such as clinical trials of new treatments, to help better understand the best way to use interventions.

## Recruitment


<span id="date">We</span> have recruited:
- <span id="num-tier-2">1772</span> patients at Tier 2 (serial sampling)
- <span id="num-tier-1">702</span> at Tier 1 (single sample)
- <span id="num-tier-0">77268</span> patients at Tier Zero (case report forms - source data for the COVID-19 Clinical Information Network (CO-CIN))
- Critically-ill patients can also be recruited to a sister study, the [ISARIC GenOMICC study](https://genomicc.org) 

<script>
    function updatePatientCounts(){
        const format = x => x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");

        fetch("https://raw.githubusercontent.com/SurgicalInformatics/ccp_recruitment_flat_file/master/ccp_recruit_daily.csv")
        .then(res => res.text())
        .then(res => {
            const [fieldLine, valueLine] = res.split('\n');
            const fields = fieldLine.split(',');
            const values = valueLine.split(',');
            let data = {};
            for (let i=0; i<fields.length; i++){
                data[fields[i]] = values[i];
            }
            
            document.getElementById("date").innerText = "As of " + data["date_last_run"].split("T")[0] + ", we";
            document.getElementById("num-tier-0").innerText = format(data["n_tier0"]);
            document.getElementById("num-tier-1").innerText = format(data["n_tier1"]);
            document.getElementById("num-tier-2").innerText = format(data["n_tier2"]);
        });
    }
</script>
