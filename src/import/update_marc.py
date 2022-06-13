from cmath import e
import json

del_marc = {
    "controfields" : ["001"],
    "datafields": ["999"]
}

def delete_marc(typedata, tag):
    with open("import/json_marc.json", encoding="utf8") as file:
        records = json.load(file)
        file.close()

    for record in records:
        try:
            record[typedata].pop(tag)
        except:
            pass

    with open('import/json_marc.json', 'w', encoding="utf8") as file:
        json.dump(records, file, indent=4, ensure_ascii=False) 




field = {
                "indicators": {
                    "Ind1": "_",
                    "Ind2": "_"
                },
                "subfields": {
                    "a": "Obras gerais",
                    "c": "E1.P1"
                }
}

def add_marc(tag, field):
    list_json = list()
    with open("import/json_marc.json", encoding="utf8") as file:
        records = json.load(file)
        file.close()

    for record in records:
        
        record['datafields'][tag] = field
        list_json.append(record)

    with open('import/json_marc.json', 'w', encoding="utf8") as file:
            json.dump(list_json, file, indent=4, ensure_ascii=False)



def callNumber(pathfile):
    with open("import/json_marc.json", encoding="utf8") as file:
        records = json.load(file)
        file.close()

    for record in records:
        cdd = record['datafields']['090']['subfields']['a']
        cutter = record['datafields']['090']['subfields']['b']
        record['datafields']['090'] =  {
                "indicators": {
                    "Ind1": "_",
                    "Ind2": "_"
                },
                "subfields": {
                    "a": f"{cdd} {cutter}"
                }
            }

    with open('import/json_marc.json', 'w', encoding="utf8") as file:
            json.dump(records, file, indent=4, ensure_ascii=False) 

add_marc('852', field)
callNumber("import/json_marc.json")
delete_marc("controlfields", "001")
delete_marc("datafields", "999")
