import requests
from requests.utils import quote
import urllib

def makeCall(langOrigin, langTr, text):
    textEncoded = quote(text)
    r = requests.get('http://www.transltr.org/api/translate?text='+textEncoded+'&to='+langTr+'&from='+langOrigin)
    s = r.json()

    return s['translationText']
