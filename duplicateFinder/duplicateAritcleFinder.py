import codecs

filename = 'texts\\linkedinHTMLfile.txt'
myArticles = []

def read_file(fname):
    path = "texts\\savedArticles.txt"
    with codecs.open(fname,encoding='utf-8') as f:
        for line in f:
            if '<span dir="ltr">' in line:
                with codecs.open(path,'a',encoding='utf-8') as parsed:
                    newLine = line.replace('<span dir="ltr">','').replace('</span>','')
                    parsed.write(newLine.lstrip())

def getArticlesInLists():
    with codecs.open('texts\\savedArticles.txt', 'r', encoding='utf-8') as f:
        for line in f:
            myArticles.append(line)

def duplicateFinder():
    seen = []
    duplicateValue = []
    for elem in myArticles:
        if elem not in seen:
            seen.append(elem)
        elif elem not in duplicateValue:
            duplicateValue.append(elem)

    return list(duplicateValue)

if __name__ == "__main__":
    read_file(filename)
    getArticlesInLists()
    print(*duplicateFinder())
    print(len(duplicateFinder()))