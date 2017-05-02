import sys
from managefiles import *
from localizeVo import *
from translatorServices.translatorGoogle import *

##------------------Main---------------------##

#args = [pylocalize, filename, languageOrigin -translatorService, language1, language2, language3, ...]
args = sys.argv
if(len(args) < 4):
    print ("Error! type a filename and languages to translate the file. For example: \n pylocalize C:/localize_en en -google es fr")
    sys.exit()

# statics variables:
languages = ['en','es','fr','ge']
translators = ['google']

# Get parameters:
languagesSelected = [];
translatorSelected = "google"
languageOrigin = args[2]

if (args[3].find("-") >= 0):
    languagesSelected = args[4:len(args)]
    translatorSelected = args[3][1:]
else:
    translatorSelected = args[3:len(args)]

#Check if service exists:
if (translatorSelected not in translators):
    print ("Error! translator service doesn't exist or is not available. Services available: ",translators)
    sys.exit()

#Check if selected languages exist:
if (set(languagesSelected).issubset(languages) == False):
    print ("Error! Languages available: ",languages)
    sys.exit()

print ('Languages selected: ',languagesSelected)
print ('Using service: ',translatorSelected)

#Open file and read it:
locList = getTextToLocalize(args[1])
for lang in languagesSelected:
    tempLocList = []
    print ("Translating ",languageOrigin," to ",lang,"...")
    for loc in locList:
        tr = makeCall(languageOrigin,lang,loc.getValue())
        tempLocList.append(LocalizeVo(loc.getName(),tr))

    #for loc in tempLocList:
    #    loc.printLocalizeVo()

    #Create new file with tempLocList:
    createLocalizeFile(tempLocList,lang)

print ("Translation finalized")
