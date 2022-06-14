import json
pathfile = 'src\import\json_marc.json'

del_marc = {
    "controfields" : ["001"],
    "datafields": ["999"]
}

def delete_marc(pathfile, typedata, tag):
    with open(pathfile, encoding="utf8") as file:
        records = json.load(file)
        file.close()

    for record in records:
        try:
            record[typedata].pop(tag)
        except:
            pass

    with open(pathfile, 'w', encoding="utf8") as file:
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

field900 = {
                "indicators": {
                    "Ind1": "_",
                    "Ind2": "_"
                },
                "subfields": {
                    "a": "Livro"
                }
}

def add_marc(pathfile, tag, field):
    list_json = list()
    with open(pathfile, encoding="utf8") as file:
        records = json.load(file)
        file.close()

    for record in records:
        
        record['datafields'][tag] = field
        list_json.append(record)

    with open(pathfile, 'w', encoding="utf8") as file:
            json.dump(list_json, file, indent=4, ensure_ascii=False)



def callNumber(pathfile):
    with open(pathfile, encoding="utf8") as file:
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

#add_marc(pathfile, '900', field900)
# callNumber("import/json_marc.json")
# delete_marc("controlfields", "001")
#delete_marc(pathfile, "datafields", "942")