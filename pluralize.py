import json 
with open('sing2plur.json') as f:
    pluralize = json.load(f)

pluralize["iâr"]

# pluralize["iâr"]
# >>> 'ieir'
