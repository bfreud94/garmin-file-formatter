import sys
import xml.etree.ElementTree as ET
ET.register_namespace('', 'http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2');

ns = {
  'tcd': 'http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2',
  'ae': 'http://www.garmin.com/xmlschemas/ActivityExtension/v2'
}

def roundtoint(root, xpath):
  """Given an xpath, replace the float value inside with a rounded int value"""
  for e in root.findall(xpath, ns):
    e.text = str(int(float(e.text)))

def main():
  # Read the file from stdin
  tree = ET.parse('PATH_TO_INPUT_FILE.tcx')
  root = tree.getroot()

  # Remove the creator tag, Garmin won't recognize that
  activity = root.find('./tcd:Activities/tcd:Activity', ns)
  creator = activity.find('./tcd:Creator', ns)
  activity.remove(creator)

  # Round these values to ints, since Garmin requires that
  roundtoint(root, './/ae:Watts')
  roundtoint(root, './/tcd:AverageHeartRateBpm/tcd:Value')
  roundtoint(root, './/tcd:MaximumHeartRateBpm/tcd:Value')
  roundtoint(root, './/tcd:HeartRateBpm/tcd:Value')
  roundtoint(root, './/tcd:Calories')
  roundtoint(root, './/tcd:Cadence')

  # Output to stdout
  tree.write('PATH_TO_OUTPUT_FILE.tcx')

if __name__ == "__main__":
  main()