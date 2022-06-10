def getBiblioNumber(pathfile):
    with open(pathfile) as file:
        r = file.read()
        file.close()
    items = r.split('@book{')[1:]
    biblionumbers = list()
    for item in items:
        biblionumber = item.split(',', 1)[0]
        biblionumbers.append(biblionumber)

    return biblionumbers

biblionumbers = getBiblioNumber('import/shelf.bibtex')

# list of names
names = ['Jessa', 'Eric', 'Bob']


with open(r'import/biblionumbers.txt', 'w') as fp:
    for biblionumber in biblionumbers:
        # write each item on a new line
        fp.write("%s\n" % biblionumber)
    print('Done')

