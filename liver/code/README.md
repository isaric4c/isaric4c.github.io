---
layout: page
---

# AST_ALT_counter

This code takes data consisting of AST and ALT measurements for individuals, and produces a dataset consisting of monthly counts of total and elevated AST and ALT levels, as well as a table consisting of the monthly mean and variances of total and elevated AST and ALT measurements. The file input.csv indicates the format the input data should be in.

To use: 

1. Replace the file `input.csv` with a new one containing your data. This file MUST have the following column headings: 
patient_id, DOB, sample_date, AST, ALT

	It also must have at least one of: age, DOB

	If age is included, it should be measured exactly in years, with one year equal to 365.25 days.

	Your `input.csv` file must not have any extra text at the top of the file - the first row should be these column headings

2. 
	> **WINDOWS**:  
	>	double-click `WinPython Command Prompt`  
	>	In the black box that appears, type:  
	>	`cd ../`  
	>	And press Enter  
	>	Then type:  
	>	`python-3.9.10/python.exe process_data.py`  
	>	And press Enter  

 
	> **MAC/LINUX**:  
	>	open a terminal window (e.g. on mac, hit CMD-SPACE and type `terminal`)
	>	In the black box that appears, type:  
	>	`python ` (with a space afterwards)  
	>	Then drag the `process_data.py` file icon from your finder/filebrowser window onto the black box. When you let go, a long file path should appear. 
	>	Then press Enter  

3. A File titled `summary_table.csv` should appear. Check the contents, and then email to us at [ccp@roslin.ed.ac.uk](mailto:ccp@roslin.ed.ac.uk)






