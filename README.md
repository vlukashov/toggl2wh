# Convertion util from Toggl to Workhours

## Usage

- Step 1: export a 'Detailed' CSV report from Toggle for some time period (https://toggl.com/app/reports/detailed/)
- Step 2: run the toggl2wh.awk to conwert the report to the workhours import format:
	```
	$ chmod +x toggl2wh.awk
	$ ./toggl2wh.awk toggl-export.csv > wh.txt
	```
- Step 3: manually edit the workhours import file to add a header like:
	```
	# format=sami
	# PROJECT MAP START

	Vaadin=799,5,3
	vaadin.com=1090,5,3

	# PROJECT MAP END
	```
- Step 4: import the file into Workhours (select 'Import' in the top menu)