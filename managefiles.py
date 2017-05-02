from localizeVo import *

#getTextToLocalize: Open and read the file and return a list of localizeVo {name,value} to translate.
def getTextToLocalize(fileName):
    fileOrigin = None
    locList = []

    try:
        fileOrigin = open(fileName,'r')
        for line in fileOrigin.readlines():
            lineSpl = line.split('"')
            if(len(lineSpl)>3):
                locVo = LocalizeVo(lineSpl[1],lineSpl[3])
                locList.append(locVo)

    except (IOError, OSError) as e:
        print ("error! file doesn't exist or is corrupted")
        if(fileOrigin != None):
            fileOrigin.close()
        sys.exit()

    finally:
        if(fileOrigin != None):
            fileOrigin.close()

    return locList

def createLocalizeFile(locList, lang):
    nameFile = "localize_"+lang+".json"
    with open(nameFile,'w') as f:
        f.write("{\n")
        for loc in locList:
            line = '"'+loc.getName() + '" : "'+loc.getValue()+'",\n'
            f.write(line)

        f.write("}\n")
