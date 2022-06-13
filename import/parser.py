from xml.dom.minidom import parse, parseString
import xml.etree.ElementTree as et

dom = parse('import/koha.xml')
records = dom.getElementsByTagName('record')
record = records[0]
leader = record.getElementsByTagName('leader')[0]
tree = et.parse('import/koha.xml')
root = tree.getroot()