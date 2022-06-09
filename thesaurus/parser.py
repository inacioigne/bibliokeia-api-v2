import json

def parser_authority(path_file):

    authority = dict()
    datafields = dict()

    with open(path_file) as file:
        lines = file.readlines()
        file.close()

    for line in lines:
        if line[:3] == '000':
            authority['leader'] = line[4:].replace('\n','')
        elif line[:3] == '008':
            authority['controlfields'] = {'008': line[4:].replace('\n','')}
        elif int(line[:3]) > 35:
            
            datafields[line[:3]] = {"indicators": {
                                        "Ind1": line[4:5],
                                        "Ind2": line[5:6]
                                        }
                                        }
            subfields = line[7:].split('|')[1:]
            subs = dict()
            for subfield in subfields:
                sub = subfield.split(' ', 1)
                subs[sub[0]] = sub[1].replace('\n', '')

            datafields[line[:3]]['subfields'] = subs

        authority['datafields'] = datafields

        with open("nome_pessoal.json", "w") as file:
            json.dump(authority, file, indent=4)

    return authority

authority = parser_authority('thesaurus/nome_pessoal.txt')



    



