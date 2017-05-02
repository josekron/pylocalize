import requests
from requests.utils import quote
import urllib

def makeCall(langOrigin, langTr, text):
    textEncoded = quote(text)
    r = requests.get('https://translate.googleapis.com/translate_a/single?client=gtx&sl='+langOrigin+'&tl='+langTr+'&dt=t&q='+textEncoded)
    s = r.json()

    result = ""
    for res in s[0]:
        result = result + res[0]

    #print(result)
    return result;
