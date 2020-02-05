import xml.etree.ElementTree as ET

tree = ET.parse("annot.xml")
root = tree.getroot()

for child in root.iter('source'):
    print(child.text)
