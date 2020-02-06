import xml.etree.ElementTree as ET
import codecs

tree = ET.parse("annot.xml")
root = tree.getroot()

file = codecs.open("annot.txt", "w", "utf-8")
textlist = []
for element in root.iter():
    if element.text is not None and not element.text.isspace():
           textlist.append(element.text)
file.write("\n".join(textlist))
file.close()
