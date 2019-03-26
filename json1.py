import json

#from urllib.request import urlopen

jsonstring = {
    "glossary": {
        "title": "example glossary",
		"GlossDiv": {
            "title": "S",
			"GlossList": {
                "GlossEntry": {
                    "ID": "SGML",
					"SortAs": "SGML",
					"GlossTerm": "Standard Generalized Markup Language",
					"Acronym": "SGML",
					"Abbrev": "ISO 8879:1986",
					"GlossDef": {
                        "para": "A meta-markup language, used to create markup languages such as DocBook.",
						"GlossSeeAlso": ["GML", "XML"]
                    },
					"GlossSee": "markup"
                }
            }
        }
    }
}


print jsonstring
jsonDump = json.dumps(jsonstring)
jsonObj = json.loads(jsonDump)
print (jsonObj.get("glossary"))
printprint (jsonObj.get("glossary")[1])


#def getCountry(ipAddress):
#   response = urlopen("http://freegeoip.net/json/50.78.253.58")read()

