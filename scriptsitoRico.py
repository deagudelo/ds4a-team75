import unicodedata
import json

def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    return u"".join([c for c in nfkd_form if not unicodedata.combining(c)])


with open('database//GeoData/munis.geojson', encoding='utf-8') as geo:
    geojson = (remove_accents(geo.read()))
    with open('database//GeoData/munis-noaccents.geojson', "w") as noa:
        noa.write(geojson)
        noa.close()



