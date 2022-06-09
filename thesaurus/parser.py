import json

def parser_bn(path_file):

    authority = dict()
    datafields = dict()
    ver = list()
    ver_tambem = list()
    source = list()

    with open(path_file, encoding='utf8') as file:
        lines = file.readlines()
        file.close() 

    for line in lines:
        if line[:3] == '000':
            authority['leader'] = line[4:].replace('\n','')
        elif line[0] == '9':
            pass
        elif line[:3] == '008':
            authority['controlfields'] = {'008': line[4:].replace('\n','')}
        elif line[0] == '4':
            remissiva = {"indicators": {
                                        "Ind1": line[4:5],
                                        "Ind2": line[5:6]
                                        }}
            subfields = line[7:].split('|')[1:]
            subs = dict()
            for subfield in subfields:
                sub = subfield.split(' ', 1)
                subs[sub[0]] = sub[1].replace('\n', '').rstrip()

            remissiva['subfields'] = subs
            ver.append(remissiva)
            datafields[line[:3]] = ver
        
        elif line[0] == '5':
            remissiva = {"indicators": {
                                        "Ind1": line[4:5],
                                        "Ind2": line[5:6]
                                        }}
            subfields = line[7:].split('|')[1:]
            subs = dict()
            for subfield in subfields:
                sub = subfield.split(' ', 1)
                subs[sub[0]] = sub[1].replace('\n', '').rstrip()

            remissiva['subfields'] = subs
            ver_tambem.append(remissiva)
            datafields[line[:3]] = ver_tambem

        elif line[:3] == '670':
            remissiva = {"indicators": {
                                        "Ind1": line[4:5],
                                        "Ind2": line[5:6]
                                        }}
            subfields = line[7:].split('|')[1:]
            subs = dict()
            for subfield in subfields:
                sub = subfield.split(' ', 1)
                subs[sub[0]] = sub[1].replace('\n', '').rstrip()

            remissiva['subfields'] = subs
            source.append(remissiva)
            datafields[line[:3]] = source
         
        elif int(line[:3]) > 35:
               
            datafields[line[:3]] = {"indicators": {
                                        "Ind1": line[4:5],
                                        "Ind2": line[5:6]
                                        }}
            subfields = line[7:].split('|')[1:]
            subs = dict()
            for subfield in subfields:
                sub = subfield.split(' ', 1)
                subs[sub[0]] = sub[1].replace('\n', '').rstrip()

            datafields[line[:3]]['subfields'] = subs

        authority['datafields'] = datafields

        with open("thesaurus/local.json", "w", encoding='utf8') as file:
            json.dump(authority, file, indent=4, ensure_ascii=False)

    return authority





authority = parser_bn('thesaurus/local.txt')



    



