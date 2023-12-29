# Garmin File Formatter #

## Purpose ##
This python script reads a .tcx input file and returns it formatted to be uploaded to Garmin. Normally, there is a separate script I run that downloads any new peloton workouts as .fit files, which can be uploaded to Garmin. But this script is used if that script has problems.

## Problems with normal process ##
The main reason why the script doesn't work is because certain numbers aren't rounded. Watts, Average Heart Rate (BPM), Maximum Heart Rate (BPM), Calories, and Cadence all need to be rounded to the nearest whole number, or else the upload will fail. This script rounds those numbers.

## Steps ##
1. Export workout as original tcx from Strava
2. Go to [JSON Formatter](https://jsonformatter.org/xml-formatter) to format/beautify the tcx file (which is, at its core, an XML file). This step is necessary because the script iterates over the tcx file's lines, and the original files tend to only have a few carriage returns
3. Change the input and output file locations
4. Open the command line and run `python garmin-file-formatter.py`. If there are no errors, the console is completely empty, and the output file is generated, it should be able to upload to Garmin
5. Upload newly generated file to Garmin
