---
layout: page
title: COVID-19 Outcomes - Version 1.0
description: The UK ISARIC Coronavirus Clinical Characterisation Consortium.
intro_image_absolute: false
intro_image_hide_on_mobile: false
special_command: "onload='draw_static(); setup(); calculateBMI();'"
---

<script src="https://d3js.org/d3.v5.min.js"></script>

<div class="wrapper">
  
  <section>

    <p> This is an old version of the ISARIC 4C risk calculator, showing data that was last updated on <b>21st May 2020</b>.</p>

    <p>
      The ISARIC4C consortium has studied one third of all patients who have been admitted to hospital in the England, 
      Wales and Scotland with COVID-19. However not all people who have been admitted to hospital have completed their
      admission. Our analysis is a snapshot of what was known for 20,133 people admitted between 6th February and 19th
      April and have had at least 14 days follow up. This large dataset makes it possible to estimate the outcomes for
      groups of people admitted to hospital, and how age, sex and some medical conditions affects likely outcomes.
    </p>

    <p>
      It must be emphasised that most people who get COVID-19 only develop mild symptoms, and will recover at home
      without needing any medical help. Our calculator predicts outcome for a group of people from the general UK popultion
      with the features entered. It can not predict any individual person's risk because it does not know all their unique
      characteristics, and their full medical history. 
    </p>


    <h2>Measured outcomes for all patients</h2>

    <p>
      This plot summarises what happened to patients who were admitted to hospital with COVID-19.
    </p>
    <p>
      Each circle represents <b>50</b> patients.
      The green circles represent the patients who were discharged from hospital alive, the black-outlined circles represent
      patients who died in hospital, and the grey circles represent patients who were continuing to receive on-going
      care in hospital.
    </p>


    <div style="display: block; font-size: 11pt;">
      <svg id='waffle-static' height="500" style="max-width: 100%; max-height: auto;">
      </svg>
    </div>


    <h2>Anticipated outcomes for specific patient groups</h2>

    <p>
      People who are older, male, or have existing medical problems, are at a higher risk than the general population.
    </p>

    <p>
      This tool allows you to estimate the risk to a group of people with specific characteristics <i>who have been
      admitted to hospital</i> with COVID-19.
      As most people with COVID-19 do not need to go to hospital, the risk to a group of people <i>who have been
      infected</i> is likely much lower.
    </p>

    <p>
      This calculator does not simply look at the subset of patients who match the entered criteria, and report the
      proportion who survived. Instead, it uses a statistical model, specifically, a Cox Proportional Hazard model.
      The research paper that explains the patient data and analysis is <a href="https://www.bmj.com/content/369/bmj.m1985">Docherty AB et al. BMJ 2020;369:m1985</a>  
    </p>

    <p>This calculator should be considered a tool for illustrating how age and comorbidity influences likley outcome. This 
      calculator must never be used as a predictive tool in practice or to inform individual treatment decisions.</p>


    <div id="risk-div">
      <h3>Anticipated Outcome 14 days after admission</h3>
      <form onsubmit="return false;">

        <p>
          <label for="age">Age: </label><select id="age" onchange="calculateRisk()" value="18">
          <option value="<50" selected="selected">Under 50</option>
          <option value="50-59">50-59</option>
          <option value="60-69">60-69</option>
          <option value="70-79">70-79</option>
          <option value=">80">Over 80</option>
        </select>
        </p>


        <p>
          <label for="female">Sex at birth: </label><select id="female" onchange="calculateRisk()">
          <option value="no">Male</option>
          <option value="yes">Female</option>
        </select>
        </p>


        <p>
          <label for="cardiac_disease">
            Chronic Cardiac Disease:
            <small class="help-text">Diseases affecting the heart</small>
          </label>
          <select id="cardiac_disease" onchange="calculateRisk()">
          <option value="yes">Yes</option>
          <option value="no" selected="selected">No</option>
            <abbr title="this is help">?</abbr>
        </select>
        </p>

        <p>
          <label for="pulmonary_disease">
            Chronic Pulmonary Disease: 
            <small class="help-text">Diseases affecting breathing but not asthma</small>
          </label>
          <select id="pulmonary_disease" onchange="calculateRisk()">
          <option value="yes">Yes</option>
          <option value="no" selected="selected">No</option>
        </select>
        </p>


        <p>
          <label for="kidney_disease">Chronic Kidney Disease: </label>
          <select id="kidney_disease" onchange="calculateRisk()">
          <option value="yes">Yes</option>
          <option value="no" selected="selected">No</option>
        </select>
        </p>

        <p>
          <label for="diabetes">Diabetes: </label>
          <select id="diabetes" onchange="calculateRisk()">
          <option value="yes">Yes</option>
          <option value="no" selected="selected">No</option>
        </select>
        </p>

        <div style="border: 1px solid black;  border-radius: 10px; padding: 10px; margin: 10px">
          <p>
            <label for="obesity">Obesity: </label>
            <select id="obesity" onchange="clearBMIinputs()">
            <option value="yes">Yes</option>
            <option value="no" selected="selected">No</option>
          </select>
          </p>

          <p><b>Or:</b></p>

          <p>
            <label for="height">Height/cm: </label>
            <input id="height" onkeyup="calculateBMI()" />
            <label for="weight">Weight/kg: </label>
            <input id="weight" onkeyup="calculateBMI()" />
          </p>

          <p id="bmi"></p>

        </div>


        <p>
          <label for="neurological">
            Chronic neurological disorder:
            <small class="help-text">Diseases affecting the brain, spinal cord or other nerves.</small>
          </label>
          <select id="neurological" onchange="calculateRisk()">
          <option value="yes">Yes</option>
          <option value="no" selected="selected">No</option>
        </select>
        </p>


        <p>
          <label for="malignancy">
            Malignancy:
            <small class="help-text">A cancer that grows to invade surrounding tissues</small>
          </label>
          <select id="malignancy" onchange="calculateRisk()">
          <option value="yes">Yes</option>
          <option value="no" selected="selected">No</option>
        </select>
        </p>



        <p>
          <label for="dementia">Dementia: </label>
          <select id="dementia" onchange="calculateRisk()">
          <option value="yes">Yes</option>
          <option value="no" selected="selected">No</option>
        </select>
        </p>

        <p>
          <label for="liver_disease">Moderate/severe liver disease: </label>
          <select id="liver_disease" onchange="calculateRisk()">
          <option value="yes">Yes</option>
          <option value="no" selected="selected">No</option>
        </select>
        </p>

      </form>


      <svg id='waffle' width="500" height="500" style="margin-top: 20px"></svg>
      <p id="calculation-result"></p>
    </div>

    <h2>What you should do</h2>

    <p>
      It is important that <i>everyone</i> follows the Government's advice on <a
      href="https://www.gov.uk/government/publications/staying-alert-and-safe-social-distancing">Staying alert and safe
      (social distancing)</a>,
      and on <a href="https://www.gov.uk/government/publications/covid-19-stay-at-home-guidance">self-isolating</a> if
      they or someone in their household has symptoms of COVID-19.
      This is important not only to protect yourself, but also to prevent you from accidentally infecting more
      vulnerable people.
    </p>

    <p>
      People who are defined as extremely vulnerable on medical grounds should also follow the government's <a
      href="https://www.gov.uk/government/publications/guidance-on-shielding-and-protecting-extremely-vulnerable-persons-from-covid-19">advice
      on shielding</a>.
    </p>

    <p>
      If you think that you might have COVID-19, you should stay at home and consult the <a
      href="https://www.nhs.uk/conditions/coronavirus-covid-19/check-if-you-have-coronavirus-symptoms/">NHS Website</a>
      for advice.
    </p>

  </section>
</div>


<style>
  form {
    display: table;
  }

  form > p {
    display: table-row;
  }

  form > select {
    margin-bottom: 10px;
  }

  label {
    display: table-cell;
  }

  input {
    display: table-cell;
  }

  b {
    font-weight: bold;
  }

  h2 {
    margin-top: 20px;
  }

  #risk-div {
    background: aliceblue;
    border-radius: 10px;
    padding: 10px;
    width: min-content;
    max-width: 100%;
    margin: 0 auto;
  }

  .help-text {
    color: #6c757d !important;
    display: block;
    margin-top: .25rem;
    font-size: 80%;
    font-weight: 400;

    margin-top: -5px;
    margin-bottom: 10px;
  }

</style>

<script>

  const age_coefficients = {'<50': 1, '50-59': 2.63, '60-69': 4.99, '70-79': 8.51, '>80': 11.09};
  const binary_risks = {
    female: 0.81,
    cardiac_disease: 1.16,
    pulmonary_disease: 1.17,
    kidney_disease: 1.28,
    diabetes: 1.06,
    obesity: 1.33,
    neurological: 1.17,
    dementia: 1.40,
    malignancy: 1.13,
    liver_disease: 1.51
  };

  const numRows = 10, numColumns = 10;

  function setup() {

    const margin = {top: 10, right: 0, bottom: 10, left: 115};
    const width = 305 - margin.left - margin.right,
      height = 300 - margin.top - margin.bottom;


    const x = d3.scaleLinear().domain([0, numColumns]).range([0, width]);
    const y = d3.scaleLinear().domain([0, numRows]).range([0, height]);
    const radius = 7;

    const svg = d3.select("#waffle")
      .attr("width", width + margin.left + margin.right)
      .attr("height", height + margin.top + margin.bottom)
      .append("g")
      .attr("transform", "translate(" + margin.left + "," + margin.top + ")");


    const data = d3.range(0, numRows * numColumns)
      .map(i => {
        const column = i % numColumns;
        return {column: column, row: Math.floor(i / numColumns), i: i};
      });

    console.log(data)

    svg.selectAll('circle')
      .data(data)
      .enter()
      .append('circle')
      .attr('cx', d => x(d.column))
      .attr('cy', d => y(d.row))
      .attr('r', radius)
      .append('title').text((d, i) => i);

    svg
      .append('text')
      .attr('x', -margin.left)
      .attr('y', y(1) - 20)
      .text('Anticipated to')
      .style('fill', 'darkgreen')
      .style('font-weight', 'bold')

    svg
      .append('text')
      .attr('x', -margin.left)
      .attr('y', y(1))
      .text('still be alive')
      .style('fill', 'darkgreen')
      .style('font-weight', 'bold')

    svg
      .append('text')
      .attr('x', -margin.left)
      .attr('y', y(numRows - 2) - 20)
      .text('Anticipated to')
      .style('fill', 'black')
      .style('font-weight', 'bold')

    svg
      .append('text')
      .attr('x', -margin.left)
      .attr('y', y(numRows - 2))
      .text('have not')
      .style('fill', 'black')
      .style('font-weight', 'bold')

    svg
      .append('text')
      .attr('x', -margin.left)
      .attr('y', y(numRows - 2) + 20)
      .text('survived')
      .style('fill', 'black')
      .style('font-weight', 'bold')

    calculateRisk();
  }

  function calculateRisk() {

    const baseline_cumulative_hazard = 0.0282264496;

    // handle_age
    let overall_hazard_ratio = age_coefficients[document.getElementById('age').value]

    Object.keys(binary_risks).forEach(risk_factor => {
      if (document.getElementById(risk_factor).value === 'yes') {
        overall_hazard_ratio *= binary_risks[risk_factor];
      }
    });

    const survive = Math.exp(-baseline_cumulative_hazard) ** overall_hazard_ratio;

    const rounded_percentage = Math.ceil(survive * 100) / 1;
    document.getElementById("calculation-result").innerHTML = `Out of <b>100</b> people matching the criteria above admitted to hospital with COVID-19, <b>${rounded_percentage}</b> would be anticipated to still be alive 14 days later.`;

    d3.select("#waffle")
      .selectAll('circle')
      .style('stroke', d => (d.i < survive * numRows * numColumns) ? 'darkgreen' : 'black')
      .style('fill', d => (d.i < survive * numRows * numColumns) ? 'darkgreen' : 'none');
  }

  function calculateBMI(){
    const weight_kg = +document.getElementById("weight").value;
    const height_m = +document.getElementById("height").value / 100;
    const bmi = weight_kg / (height_m**2);

    if (!isNaN(bmi)){
      document.getElementById('obesity').value = (bmi > 30) ? 'yes' : 'no';
      document.getElementById('bmi').innerText = `Calculated BMI is ${Math.round(bmi * 1)}. A value over 30 might be physician defined obesity.`;
      calculateRisk();
    }
  }

  function clearBMIinputs(){
    document.getElementById('height').value = '';
    document.getElementById('weight').value = '';
    document.getElementById('bmi').innerText = "";
    calculateRisk();
  }
</script>

<script>


  function draw_static() {
    const numColumns = 10;

    const margin = {top: 0, right: 100, bottom: 10, left: 100};
    const width = 850 - margin.left - margin.right,
      height = 1000 - margin.top - margin.bottom;

    const patientsPerCircle = 50;
    const subplotWidth = 220, subplotPadding = 30;
    const circleRadius = 7;

    const x = d3.scaleLinear().domain([0, numColumns]).range([0, subplotWidth]);

    const y = i => circleRadius * 3 * i;

    const svg = d3.select("#waffle-static")
      .attr('viewBox', `0 0 ${width + margin.left + margin.right} ${height + margin.top + margin.bottom}`)
      .append("g")
      .attr("transform", "translate(" + margin.left + "," + margin.top + ")");


    const data = [
      {'group': 'All admitted patients', outcomes: {'Died': 5165, 'Ongoing care': 6769, 'Discharged alive': 8199}},
      {'group': 'Patients admitted to ICU/HDU', outcomes: {'Died': 958, 'Ongoing care': 1217, 'Discharged alive': 826}},
      {'group': 'Patients receiving invasive ventilation', outcomes: {'Died': 618, 'Ongoing care': 764, 'Discharged alive': 276}
      }
    ];

    const subplots = svg.selectAll('g')
      .data(data)
      .enter()
      .append('g')
      .attr('transform', (d, i) => `translate(${i * (subplotWidth + subplotPadding)}, 0)`)
      .attr('id', (d, i) => `group-${i}`);

    data.forEach((d, group_num) => {
      const g = d3.select(`#group-${group_num}`).append('g').attr('transform', 'translate(0, 50)');

      const numCircles = Math.ceil((d.outcomes['Died'] + d.outcomes['Ongoing care'] + d.outcomes['Discharged alive']) / patientsPerCircle);
      const circleData = d3.range(0, numCircles)
        .map(i => {
          const numRows = Math.ceil(numCircles / numColumns)
          const column = i % numColumns;
          return {column: column, row: Math.floor(i / numColumns), i: i};
        });

      console.log((d.outcomes['Died'] + d.outcomes['Ongoing care'] + d.outcomes['Discharged alive']))

      g.selectAll('circles')
        .data(circleData)
        .enter()
        .append('circle')
        .attr('cx', d => x(d.column))
        .attr('cy', d => y(d.row))
        .attr('r', circleRadius)
        .style('fill', (_, i) => {
          if (i * patientsPerCircle < d.outcomes['Discharged alive']) {
            return 'darkgreen'
          } else if (i * patientsPerCircle < d.outcomes['Discharged alive'] + d.outcomes['Ongoing care']) {
            return 'grey';
          } else {
            return 'none'
          }
        })
        .style('stroke', (_, i) => {
          if (i * patientsPerCircle < d.outcomes['Discharged alive']) {
            return 'darkgreen'
          } else if (i * patientsPerCircle < d.outcomes['Discharged alive'] + d.outcomes['Ongoing care']) {
            return 'grey';
          } else {
            return 'black'
          }
        })

    });

    // title on top
    subplots.append('text')
      .text(d => d.group)
      .attr('text-anchor', 'middle')
      .attr('x', subplotWidth / 2)
      .attr('y', 20)
      .style('font-weight', 'bold');


    // counts on bottom
    subplots.append('text')
      .text(d => `${d.outcomes['Discharged alive']}  Discharged alive`)
      .attr('text-anchor', 'start')
      .attr('x', 0)
      .attr('y', 950)
      .style('font-weight', 'bold');

    subplots.append('text')
      .text(d => `${d.outcomes['Ongoing care']}  Receiving ongoing care`)
      .attr('text-anchor', 'start')
      .attr('x', 0)
      .attr('y', 970)
      .style('font-weight', 'bold');

  subplots.append('text')
    .text(d => `${d.outcomes.Died}  Did not survive`)
    .attr('text-anchor', 'start')
    .attr('x', 0)
    .attr('y', 990)
    .style('font-weight', 'bold');



    // labels on left
    svg
      .append('text')
      .attr('x', -margin.left)
      .attr('y', y(10))
      .text('Survived')
      .style('fill', 'darkgreen')
      .style('font-weight', 'bold')

    svg
      .append('text')
      .attr('x', -margin.left)
      .attr('y', y(24))
      .text('Receiving')
      .style('fill', 'black')
      .style('font-weight', 'bold');

    svg
      .append('text')
      .attr('x', -margin.left)
      .attr('y', y(25))
      .text('ongoing')
      .style('fill', 'black')
      .style('font-weight', 'bold');

    svg
      .append('text')
      .attr('x', -margin.left)
      .attr('y', y(26))
      .text('care')
      .style('fill', 'black')
      .style('font-weight', 'bold');


    svg
      .append('text')
      .attr('x', -margin.left)
      .attr('y', y(37))
      .text('Did not')
      .style('fill', 'black')
      .style('font-weight', 'bold');

    svg
      .append('text')
      .attr('x', -margin.left)
      .attr('y', y(38))
      .text('survive')
      .style('fill', 'black')
      .style('font-weight', 'bold');


  }
</script>



