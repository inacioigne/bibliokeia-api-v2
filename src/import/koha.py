shelf = 'P5'
def getBiblioNumber(pathfile, shelf=shelf):
    with open(pathfile) as file:
        r = file.read()
        file.close()
    items = r.split('@book{')[1:]
    biblionumbers = list()
    for item in items:
        biblionumber = item.split(',', 1)[0]
        biblionumbers.append(biblionumber)

    return biblionumbers

biblionumbers = getBiblioNumber(f'src\import\E1\{shelf}\shelf.bibtex')




with open(f'src/import/E1/{shelf}/biblionumbers.txt', 'w') as fp:
    for biblionumber in biblionumbers:
        # write each item on a new line
        fp.write("%s\n" % biblionumber)
    print('Done')

