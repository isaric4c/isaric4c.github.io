---
layout: page
---

# AST_ALT_counter

This code takes data consisting of AST and ALT measurements for individuals, and produces a table consisting of monthly counts of total and elevated AST and ALT levels, as well as their mean and variance. The file input.csv indicates the format the input data should be in.

To use: 

1. Replace the file `input.csv` with a new one containing your data. This file must contain columns with the following data:
patient_id, sample_date, AST, ALT

It also must have at least one of: age, DOB

If age is included, it should be measured exactly in years, with one year equal to 365.25 days.

You can either rename the appropriate column headings of input.csv so that they are as above, or you can follow the command prompt messages that will direct you to choose which column headings correpond to the above.

2. 
	> **WINDOWS**:  
	>	double-click `WinPython Command Prompt`  
	>	In the black box that appears, type:  
	>	`python process_data.py`  
	>	And press Enter  

 
	> **MAC/LINUX**:  
	> 	Open finder and navigate to the AST_ALT_counter folder (don’t open the AST_ALT_counter folder directly, but navigate through finder!)
	>	In the left top corner click Finder, Services, New Terminal Tab at Folder. 
	> 	In the black box that appears, type:
	>   `python process_data.py`
	> 	And press enter

3. A File titled `summary_table.csv` should appear. Check the contents, and then email to us at [ccp@ed.ac.uk](mailto:ccp@ed.ac.uk)






