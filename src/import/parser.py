import json
from xml.dom.minidom import parse, parseString
import xml.etree.ElementTree as et

shelf = 'P1'


def tranform_json(marcxml_file):
    dom = parse(marcxml_file)
    records = dom.getElementsByTagName('record')

    json_list = list()
    repetiveis = ['610', '650','651', "710","700", "952"]

    for record in records:
        json_marc = dict()
        root = et.fromstring(record.toxml())

        #LEADER
        leader = root.find('leader').text 
        json_marc['leader'] = leader

        #CONTROFIELDS
        control = dict()
        controfields = root.findall('controlfield')
        for controfield in controfields:
            tag = controfield.attrib['tag']
            control[tag] = controfield.text
        json_marc["controlfields"] = control

        #DATAFIELDS
        data = dict()             
        datafields = root.findall('datafield')

        for datafield in datafields: 
            tag = datafield.attrib['tag']
            ind1 = datafield.attrib['ind1']
            ind2 = datafield.attrib['ind2']
            indicators = {
                "Ind1": ind1,
                "Ind2": ind2
            }
            # Subfields
            sub = dict()
            subfields = datafield.findall('subfield')
            for subfield in subfields:
                code = subfield.attrib['code']
                sub[code] = subfield.text

            if tag in repetiveis:
                if tag in data.keys():
                    listTag.append({"indicators": indicators, 'subfields': sub })
                else:
                    listTag = [{"indicators": indicators, 'subfields': sub }]
                data[tag] = listTag
            else:
                data[tag] = {"indicators": indicators, 'subfields': sub }  
            
        json_marc['datafields'] = data  
        json_list.append(json_marc)

        with open(f'src\import\E1\{shelf}\marc.json', 'w', encoding="utf8") as file:
            json.dump(json_list, file, indent=4, ensure_ascii=False)


        

    return json_list

json_list = tranform_json(f"src\import\E1\{shelf}\koha.xml")