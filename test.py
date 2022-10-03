import json
import csv
from json2html import *

output_json = json.load(open('/home/user/Документы/table_jun/conf_jup.json'))
path = '/home/user/Документы/table_jun/juniper.txt'

juniper = []
#policy0
with open(path,'w') as out:
    name = output_json["configuration"]["security"]["policies"]["global"]["policy"][0]
    sour_addr = output_json["configuration"]["security"]["policies"]["global"]["policy"][0]["match"]["source-address"]
    #dest_addr = output_json["configuration"]["security"]["policies"]["global"]["policy"][0]["match"]["destination-address"]
    dest_ip = output_json["configuration"]["security"]["address-book"][0]["address"][40]
    applic = output_json["configuration"]["security"]["policies"]["global"]["policy"][0]["match"]["application"]
    fr_zone = output_json["configuration"]["security"]["policies"]["global"]["policy"][0]["match"]["from-zone"]
    th = output_json["configuration"]["security"]["policies"]["global"]["policy"][0]["then"]
    th_min = (min(th, key=th.get))
    juniper = str(name["name"]), sour_addr[0], dest_ip["name"], dest_ip["ip-prefix"], applic[0], fr_zone[0], "-", th_min
    out.write(', '.join(juniper))
    out.write('\n')
with open(path,'a') as out:
    dest_ip = output_json["configuration"]["security"]["address-book"][0]["address"][41]
    applic = output_json["configuration"]["security"]["policies"]["global"]["policy"][0]["match"]["application"]
    juniper = "_", "_", dest_ip["name"], dest_ip["ip-prefix"], applic[1], "_", "-", "_"
    out.write(', '.join(juniper))
    out.write('\n')
app = [2, 3, 4]
with open(path,'a') as out:
    for x in app:
        applic = output_json["configuration"]["security"]["policies"]["global"]["policy"][0]["match"]["application"]
        juniper = "_", "_", "_", "_", applic[x], "_", "-", "_"
        out.write(', '.join(juniper))
        out.write('\n')
#policy1
with open(path,'a') as out:
    name = output_json["configuration"]["security"]["policies"]["global"]["policy"][1]
    sour_addr = output_json["configuration"]["security"]["policies"]["global"]["policy"][1]["match"]["source-address"]
    #dest_addr = output_json["configuration"]["security"]["policies"]["global"]["policy"][0]["match"]["destination-address"]
    dest_ip = output_json["configuration"]["security"]["address-book"][0]["address"][53]
    applic = output_json["configuration"]["security"]["policies"]["global"]["policy"][1]["match"]["application"]
    fr_zone = output_json["configuration"]["security"]["policies"]["global"]["policy"][1]["match"]["from-zone"]
    th = output_json["configuration"]["security"]["policies"]["global"]["policy"][1]["then"]
    th_min = (min(th, key=th.get))
    juniper = str(name["name"]), sour_addr[0], dest_ip["name"], dest_ip["ip-prefix"], applic[0], fr_zone[0], "-", th_min
    out.write(', '.join(juniper))
    out.write('\n')
#policy2
with open(path,'a') as out:
    name = output_json["configuration"]["security"]["policies"]["global"]["policy"][2]
    sour_addr = output_json["configuration"]["security"]["policies"]["global"]["policy"][2]["match"]["source-address"]
    #dest_addr = output_json["configuration"]["security"]["policies"]["global"]["policy"][0]["match"]["destination-address"]
    dest_ip = output_json["configuration"]["security"]["address-book"][0]["address"][7]
    applic = output_json["configuration"]["security"]["policies"]["global"]["policy"][2]["match"]["application"]
    fr_zone = output_json["configuration"]["security"]["policies"]["global"]["policy"][2]["match"]["from-zone"]
    th = output_json["configuration"]["security"]["policies"]["global"]["policy"][2]["then"]
    th_min = (min(th, key=th.get))
    juniper = str(name["name"]), sour_addr[0], dest_ip["name"], dest_ip["ip-prefix"], applic[0], fr_zone[0], "-", th_min
    out.write(', '.join(juniper))
    out.write('\n')
with open(path,'a') as out:
    dest_ip = output_json["configuration"]["security"]["address-book"][0]["address"][8]
    fr_zone = output_json["configuration"]["security"]["policies"]["global"]["policy"][2]["match"]["from-zone"]
    juniper = "_", "_", dest_ip["name"], dest_ip["ip-prefix"], "-", fr_zone[1], "-", "_"
    out.write(', '.join(juniper))
    out.write('\n')
with open(path,'a') as out:
    dest_ip = output_json["configuration"]["security"]["address-book"][0]["address"][9]
    juniper = "_", "_", dest_ip["name"], dest_ip["ip-prefix"], "-", "-", "-", "_"
    out.write(', '.join(juniper))
    out.write('\n')
#policy3
with open(path,'a') as out:
    name = output_json["configuration"]["security"]["policies"]["global"]["policy"][3]
    sour_addr = output_json["configuration"]["security"]["policies"]["global"]["policy"][3]["match"]["source-address"]
    #dest_addr = output_json["configuration"]["security"]["policies"]["global"]["policy"][0]["match"]["destination-address"]
    dest_ip = output_json["configuration"]["security"]["address-book"][0]["address"][40]
    applic = output_json["configuration"]["security"]["policies"]["global"]["policy"][3]["match"]["application"]
    fr_zone = output_json["configuration"]["security"]["policies"]["global"]["policy"][3]["match"]["from-zone"]
    th = output_json["configuration"]["security"]["policies"]["global"]["policy"][3]["then"]
    th_min = (min(th, key=th.get))
    juniper = str(name["name"]), sour_addr[0], dest_ip["name"], dest_ip["ip-prefix"], applic[0], fr_zone[0], "-", th_min
    out.write(', '.join(juniper))
    out.write('\n')
with open(path,'a') as out:
    dest_ip = output_json["configuration"]["security"]["address-book"][0]["address"][41]
    juniper = "_", "_", dest_ip["name"], dest_ip["ip-prefix"], "_", "_", "-", "_"
    out.write(', '.join(juniper))
    out.write('\n')
#policy4
with open(path,'a') as out:
    name = output_json["configuration"]["security"]["policies"]["global"]["policy"][4]
    sour_addr = output_json["configuration"]["security"]["policies"]["global"]["policy"][4]["match"]["source-address"]
    #dest_addr = output_json["configuration"]["security"]["policies"]["global"]["policy"][0]["match"]["destination-address"]
    dest_ip = output_json["configuration"]["security"]["address-book"][0]["address"][7]
    applic = output_json["configuration"]["security"]["policies"]["global"]["policy"][4]["match"]["application"]
    fr_zone = output_json["configuration"]["security"]["policies"]["global"]["policy"][4]["match"]["from-zone"]
    th = output_json["configuration"]["security"]["policies"]["global"]["policy"][4]["then"]
    th_min = (min(th, key=th.get))
    juniper = str(name["name"]), sour_addr[0], dest_ip["name"], dest_ip["ip-prefix"], applic[0], fr_zone[0], "-", th_min
    out.write(', '.join(juniper))
    out.write('\n')
with open(path,'a') as out:
    dest_ip = output_json["configuration"]["security"]["address-book"][0]["address"][8]
    juniper = "_", "_", dest_ip["name"], dest_ip["ip-prefix"], "-", "-", "-", "_"
    out.write(', '.join(juniper))
    out.write('\n')
with open(path,'a') as out:
    dest_ip = output_json["configuration"]["security"]["address-book"][0]["address"][9]
    juniper = "_", "_", dest_ip["name"], dest_ip["ip-prefix"], "-", "-", "-", "_"
    out.write(', '.join(juniper))
    out.write('\n')
#policy5
with open(path,'a') as out:
    name = output_json["configuration"]["security"]["policies"]["global"]["policy"][5]
    sour_addr = output_json["configuration"]["security"]["policies"]["global"]["policy"][5]["match"]["source-address"]
    dest_addr = output_json["configuration"]["security"]["policies"]["global"]["policy"][5]["match"]["destination-address"]
    applic = output_json["configuration"]["security"]["policies"]["global"]["policy"][5]["match"]["application"]
    fr_zone = output_json["configuration"]["security"]["policies"]["global"]["policy"][5]["match"]["from-zone"]
    th = output_json["configuration"]["security"]["policies"]["global"]["policy"][5]["then"]
    th_min = (min(th, key=th.get))
    juniper = str(name["name"]), sour_addr[0], dest_addr[0], dest_addr[0], applic[0], fr_zone[0], "-", th_min
    out.write(', '.join(juniper))
    out.write('\n')
#policy6
with open(path,'a') as out:
    name = output_json["configuration"]["security"]["policies"]["global"]["policy"][6]
    sour_addr = output_json["configuration"]["security"]["policies"]["global"]["policy"][6]["match"]["source-address"]
    dest_addr = output_json["configuration"]["security"]["policies"]["global"]["policy"][6]["match"]["destination-address"]
    applic = output_json["configuration"]["security"]["policies"]["global"]["policy"][6]["match"]["application"]
    fr_zone = output_json["configuration"]["security"]["policies"]["global"]["policy"][6]["match"]["from-zone"]
    th = output_json["configuration"]["security"]["policies"]["global"]["policy"][6]["then"]
    th_min = (min(th, key=th.get))
    juniper = str(name["name"]), sour_addr[0], dest_addr[0], dest_addr[0], applic[0], fr_zone[0], "-", th_min
    out.write(', '.join(juniper))
    out.write('\n')
#policy7
with open(path,'a') as out:
    name = output_json["configuration"]["security"]["policies"]["global"]["policy"][7]
    sour_addr = output_json["configuration"]["security"]["policies"]["global"]["policy"][7]["match"]["source-address"]
    dest_addr = output_json["configuration"]["security"]["policies"]["global"]["policy"][7]["match"]["destination-address"]
    applic = output_json["configuration"]["security"]["policies"]["global"]["policy"][7]["match"]["application"]
    fr_zone = output_json["configuration"]["security"]["policies"]["global"]["policy"][7]["match"]["from-zone"]
    th = output_json["configuration"]["security"]["policies"]["global"]["policy"][7]["then"]
    th_min = (min(th, key=th.get))
    juniper = str(name["name"]), sour_addr[0], dest_addr[0], dest_addr[0], applic[0], fr_zone[0], "-", th_min
    out.write(', '.join(juniper))
    out.write('\n')
with open(path,'a') as out:
    applic = output_json["configuration"]["security"]["policies"]["global"]["policy"][7]["match"]["application"]
    juniper = "_", "_", "_", "_", applic[1], "_", "-", "_"
    out.write(', '.join(juniper))
    out.write('\n')
#policy8
with open(path,'a') as out:
    name = output_json["configuration"]["security"]["policies"]["global"]["policy"][8]
    sour_addr = output_json["configuration"]["security"]["policies"]["global"]["policy"][8]["match"]["source-address"]
    dest_addr = output_json["configuration"]["security"]["policies"]["global"]["policy"][8]["match"]["destination-address"]
    applic = output_json["configuration"]["security"]["policies"]["global"]["policy"][8]["match"]["application"]
    fr_zone = output_json["configuration"]["security"]["policies"]["global"]["policy"][8]["match"]["from-zone"]
    th = output_json["configuration"]["security"]["policies"]["global"]["policy"][8]["then"]
    th_min = (min(th, key=th.get))
    juniper = str(name["name"]), sour_addr[0], dest_addr[0], dest_addr[0], applic[0], fr_zone[0], "-", th_min
    out.write(', '.join(juniper))
    out.write('\n')
#policy9
with open(path,'a') as out:
    name = output_json["configuration"]["security"]["policies"]["global"]["policy"][9]
    sour_addr = output_json["configuration"]["security"]["policies"]["global"]["policy"][9]["match"]["source-address"]
    dest_addr = output_json["configuration"]["security"]["policies"]["global"]["policy"][9]["match"]["destination-address"]
    applic = output_json["configuration"]["security"]["policies"]["global"]["policy"][9]["match"]["application"]
    fr_zone = output_json["configuration"]["security"]["policies"]["global"]["policy"][9]["match"]["from-zone"]
    th = output_json["configuration"]["security"]["policies"]["global"]["policy"][9]["then"]
    th_min = (min(th, key=th.get))
    juniper = str(name["name"]), sour_addr[0], dest_addr[0], dest_addr[0], applic[0], fr_zone[0], "-", th_min
    out.write(', '.join(juniper))
    out.write('\n')
fr_zone9 = [1, 2, 3, 4, 5, 6]
with open(path,'a') as out:
    for x in fr_zone9:
        fr_zone = output_json["configuration"]["security"]["policies"]["global"]["policy"][9]["match"]["from-zone"]
        juniper = "_", "_", "_", "_", "_", fr_zone[x], "-", "_"
        out.write(', '.join(juniper))
        out.write('\n')
#policy10
with open(path,'a') as out:
    name = output_json["configuration"]["security"]["policies"]["global"]["policy"][10]
    sour_addr = output_json["configuration"]["security"]["policies"]["global"]["policy"][10]["match"]["source-address"]
    dest_addr = output_json["configuration"]["security"]["policies"]["global"]["policy"][10]["match"]["destination-address"]
    applic = output_json["configuration"]["security"]["policies"]["global"]["policy"][10]["match"]["application"]
    fr_zone = output_json["configuration"]["security"]["policies"]["global"]["policy"][10]["match"]["from-zone"]
    th = output_json["configuration"]["security"]["policies"]["global"]["policy"][10]["then"]
    th_min = (min(th, key=th.get))
    juniper = str(name["name"]), sour_addr[0], dest_addr[0], dest_addr[0], applic[0], fr_zone[0], "-", th_min
    out.write(', '.join(juniper))
    out.write('\n')
#policy11
with open(path,'a') as out:
    name = output_json["configuration"]["security"]["policies"]["global"]["policy"][11]
    sour_addr = output_json["configuration"]["security"]["policies"]["global"]["policy"][11]["match"]["source-address"]
    dest_addr = output_json["configuration"]["security"]["policies"]["global"]["policy"][11]["match"]["destination-address"]
    applic = output_json["configuration"]["security"]["policies"]["global"]["policy"][11]["match"]["application"]
    to_zone = output_json["configuration"]["security"]["policies"]["global"]["policy"][11]["match"]["to-zone"]
    th = output_json["configuration"]["security"]["policies"]["global"]["policy"][11]["then"]
    th_min = (min(th, key=th.get))
    juniper = str(name["name"]), sour_addr[0], dest_addr[0], dest_addr[0], applic[0], "-", to_zone[0], th_min
    out.write(', '.join(juniper))
    out.write('\n')
#policy12
with open(path,'a') as out:
    name = output_json["configuration"]["security"]["policies"]["global"]["policy"][12]
    sour_addr = output_json["configuration"]["security"]["policies"]["global"]["policy"][12]["match"]["source-address"]
    dest_addr = output_json["configuration"]["security"]["policies"]["global"]["policy"][12]["match"]["destination-address"]
    applic = output_json["configuration"]["security"]["policies"]["global"]["policy"][12]["match"]["application"]
    to_zone = output_json["configuration"]["security"]["policies"]["global"]["policy"][12]["match"]["to-zone"]
    th = output_json["configuration"]["security"]["policies"]["global"]["policy"][12]["then"]
    th_min = (min(th, key=th.get))
    juniper = str(name["name"]), sour_addr[0], dest_addr[0], dest_addr[0], applic[0], "-", to_zone[0], th_min
    out.write(', '.join(juniper))
    out.write('\n')
#policy13
with open(path,'a') as out:
    name = output_json["configuration"]["security"]["policies"]["global"]["policy"][13]
    sour_addr = output_json["configuration"]["security"]["policies"]["global"]["policy"][13]["match"]["source-address"]
    dest_addr = output_json["configuration"]["security"]["policies"]["global"]["policy"][13]["match"]["destination-address"]
    applic = output_json["configuration"]["security"]["policies"]["global"]["policy"][13]["match"]["application"]
    from_zone = output_json["configuration"]["security"]["policies"]["global"]["policy"][13]["match"]["from-zone"]
    th = output_json["configuration"]["security"]["policies"]["global"]["policy"][13]["then"]
    th_min = (min(th, key=th.get))
    juniper = str(name["name"]), sour_addr[0], dest_addr[0], dest_addr[0], applic[0], from_zone[0], "-", th_min
    out.write(', '.join(juniper))
    out.write('\n')
#policy14
with open(path,'a') as out:
    name = output_json["configuration"]["security"]["policies"]["global"]["policy"][14]
    sour_addr = output_json["configuration"]["security"]["policies"]["global"]["policy"][14]["match"]["source-address"]
    dest_addr = output_json["configuration"]["security"]["policies"]["global"]["policy"][14]["match"]["destination-address"]
    applic = output_json["configuration"]["security"]["policies"]["global"]["policy"][14]["match"]["application"]
    to_zone = output_json["configuration"]["security"]["policies"]["global"]["policy"][14]["match"]["to-zone"]
    th = output_json["configuration"]["security"]["policies"]["global"]["policy"][14]["then"]
    th_min = (min(th, key=th.get))
    juniper = str(name["name"]), sour_addr[0], dest_addr[0], dest_addr[0], applic[0], "-", to_zone[0], th_min
    out.write(', '.join(juniper))
    out.write('\n')
#policy15
with open(path,'a') as out:
    name = output_json["configuration"]["security"]["policies"]["global"]["policy"][15]
    sour_addr = output_json["configuration"]["security"]["policies"]["global"]["policy"][15]["match"]["source-address"]
    dest_addr = output_json["configuration"]["security"]["policies"]["global"]["policy"][15]["match"]["destination-address"]
    applic = output_json["configuration"]["security"]["policies"]["global"]["policy"][15]["match"]["application"]
    from_zone = output_json["configuration"]["security"]["policies"]["global"]["policy"][15]["match"]["from-zone"]
    th = output_json["configuration"]["security"]["policies"]["global"]["policy"][15]["then"]
    th_min = (min(th, key=th.get))
    juniper = str(name["name"]), sour_addr[0], dest_addr[0], dest_addr[0], applic[0], from_zone[0], "-", th_min
    out.write(', '.join(juniper))
    out.write('\n')
#policy16
with open(path,'a') as out:
    name = output_json["configuration"]["security"]["policies"]["global"]["policy"][16]
    sour_addr = output_json["configuration"]["security"]["policies"]["global"]["policy"][16]["match"]["source-address"]
    dest_addr = output_json["configuration"]["security"]["policies"]["global"]["policy"][16]["match"]["destination-address"]
    applic = output_json["configuration"]["security"]["policies"]["global"]["policy"][16]["match"]["application"]
    to_zone = output_json["configuration"]["security"]["policies"]["global"]["policy"][16]["match"]["to-zone"]
    th = output_json["configuration"]["security"]["policies"]["global"]["policy"][16]["then"]
    th_min = (min(th, key=th.get))
    juniper = str(name["name"]), sour_addr[0], dest_addr[0], dest_addr[0], applic[0], "-", to_zone[0], th_min
    out.write(', '.join(juniper))
    out.write('\n')
#policy17
with open(path,'a') as out:
    name = output_json["configuration"]["security"]["policies"]["global"]["policy"][17]
    sour_addr = output_json["configuration"]["security"]["policies"]["global"]["policy"][17]["match"]["source-address"]
    dest_addr = output_json["configuration"]["security"]["policies"]["global"]["policy"][17]["match"]["destination-address"]
    applic = output_json["configuration"]["security"]["policies"]["global"]["policy"][17]["match"]["application"]
    from_zone = output_json["configuration"]["security"]["policies"]["global"]["policy"][17]["match"]["from-zone"]
    th = output_json["configuration"]["security"]["policies"]["global"]["policy"][17]["then"]
    th_min = (min(th, key=th.get))
    juniper = str(name["name"]), sour_addr[0], dest_addr[0], dest_addr[0], applic[0], from_zone[0], "-", th_min
    out.write(', '.join(juniper))
    out.write('\n')
#policy18
with open(path,'a') as out:
    name = output_json["configuration"]["security"]["policies"]["global"]["policy"][18]
    sour_addr = output_json["configuration"]["security"]["policies"]["global"]["policy"][18]["match"]["source-address"]
    dest_addr = output_json["configuration"]["security"]["policies"]["global"]["policy"][18]["match"]["destination-address"]
    applic = output_json["configuration"]["security"]["policies"]["global"]["policy"][18]["match"]["application"]
    from_zone = output_json["configuration"]["security"]["policies"]["global"]["policy"][18]["match"]["from-zone"]
    th = output_json["configuration"]["security"]["policies"]["global"]["policy"][18]["then"]
    th_min = (min(th, key=th.get))
    juniper = str(name["name"]), sour_addr[0], dest_addr[0], dest_addr[0], applic[0], from_zone[0], "-", th_min
    out.write(', '.join(juniper))
    out.write('\n')
#policy19
with open(path,'a') as out:
    name = output_json["configuration"]["security"]["policies"]["global"]["policy"][19]
    sour_addr = output_json["configuration"]["security"]["policies"]["global"]["policy"][19]["match"]["source-address"]
    dest_addr = output_json["configuration"]["security"]["policies"]["global"]["policy"][19]["match"]["destination-address"]
    applic = output_json["configuration"]["security"]["policies"]["global"]["policy"][19]["match"]["application"]
    from_zone = output_json["configuration"]["security"]["policies"]["global"]["policy"][19]["match"]["from-zone"]
    th = output_json["configuration"]["security"]["policies"]["global"]["policy"][19]["then"]
    th_min = (min(th, key=th.get))
    juniper = str(name["name"]), sour_addr[0], dest_addr[0], dest_addr[0], applic[0], from_zone[0], "-", th_min
    out.write(', '.join(juniper))
    out.write('\n')
#policy20
with open(path,'a') as out:
    name = output_json["configuration"]["security"]["policies"]["global"]["policy"][20]
    sour_addr = output_json["configuration"]["security"]["policies"]["global"]["policy"][20]["match"]["source-address"]
    dest_addr = output_json["configuration"]["security"]["policies"]["global"]["policy"][20]["match"]["destination-address"]
    applic = output_json["configuration"]["security"]["policies"]["global"]["policy"][20]["match"]["application"]
    to_zone = output_json["configuration"]["security"]["policies"]["global"]["policy"][20]["match"]["to-zone"]
    try:
        th = output_json["configuration"]["security"]["policies"]["global"]["policy"][20]["then"]
    except TypeError:
        th_min = (min(th, key=th.get))
    juniper = str(name["name"]), sour_addr[0], dest_addr[0], dest_addr[0], applic[0], "-", to_zone[0], th_min
    out.write(', '.join(juniper))
    out.write('\n')
#policy21
with open(path,'a') as out:
    name = output_json["configuration"]["security"]["policies"]["global"]["policy"][21]
    sour_addr = output_json["configuration"]["security"]["policies"]["global"]["policy"][21]["match"]["source-address"]
    dest_addr = output_json["configuration"]["security"]["policies"]["global"]["policy"][21]["match"]["destination-address"]
    applic = output_json["configuration"]["security"]["policies"]["global"]["policy"][21]["match"]["application"]
    from_zone = output_json["configuration"]["security"]["policies"]["global"]["policy"][21]["match"]["from-zone"]
    try:
        th = output_json["configuration"]["security"]["policies"]["global"]["policy"][21]["then"]
    except TypeError:
        th_min = (min(th, key=th.get))
    juniper = str(name["name"]), sour_addr[0], dest_addr[0], dest_addr[0], applic[0], from_zone[0], "-", th_min
    out.write(', '.join(juniper))
    out.write('\n')
#policy22
with open(path,'a') as out:
    name = output_json["configuration"]["security"]["policies"]["global"]["policy"][22]
    sour_addr = output_json["configuration"]["security"]["policies"]["global"]["policy"][22]["match"]["source-address"]
    #dest_addr = output_json["configuration"]["security"]["policies"]["global"]["policy"][0]["match"]["destination-address"]
    dest_ip = output_json["configuration"]["security"]["address-book"][0]["address"][0]
    applic = output_json["configuration"]["security"]["policies"]["global"]["policy"][22]["match"]["application"]
    to_zone = output_json["configuration"]["security"]["policies"]["global"]["policy"][22]["match"]["to-zone"]
    th = output_json["configuration"]["security"]["policies"]["global"]["policy"][22]["then"]
    th_min = (min(th, key=th.get))
    juniper = str(name["name"]), sour_addr[0], dest_ip["name"], dest_ip["ip-prefix"], applic[0], "-", to_zone[0], th_min
    out.write(', '.join(juniper))
    out.write('\n')
with open(path,'a') as out:
    dest_ip = output_json["configuration"]["security"]["address-book"][0]["address"][1]
    applic = output_json["configuration"]["security"]["policies"]["global"]["policy"][22]["match"]["application"]
    to_zone = output_json["configuration"]["security"]["policies"]["global"]["policy"][22]["match"]["to-zone"]
    juniper = "_", "_", dest_ip["name"], dest_ip["ip-prefix"], applic[1], "-", to_zone[1], "_"
    out.write(', '.join(juniper))
    out.write('\n')
with open(path,'a') as out:
    dest_ip = output_json["configuration"]["security"]["address-book"][0]["address"][2]
    applic = output_json["configuration"]["security"]["policies"]["global"]["policy"][22]["match"]["application"]
    juniper = "_", "_", dest_ip["name"], dest_ip["ip-prefix"], applic[2], "-", "-", "_"
    out.write(', '.join(juniper))
    out.write('\n')
with open(path,'a') as out:
    dest_ip = output_json["configuration"]["security"]["address-book"][0]["address"][3]
    applic = output_json["configuration"]["security"]["policies"]["global"]["policy"][22]["match"]["application"]
    juniper = "_", "_", dest_ip["name"], dest_ip["ip-prefix"], applic[3], "-", "-", "_"
    out.write(', '.join(juniper))
    out.write('\n')
#policy23
with open(path,'a') as out:
    name = output_json["configuration"]["security"]["policies"]["global"]["policy"][23]
    sour_addr = output_json["configuration"]["security"]["policies"]["global"]["policy"][23]["match"]["source-address"]
    #dest_addr = output_json["configuration"]["security"]["policies"]["global"]["policy"][0]["match"]["destination-address"]
    dest_name = output_json["configuration"]["security"]["address-book"][0]["address"][4]
    dest_ip = output_json["configuration"]["security"]["address-book"][0]["address"][4]["dns-name"][0]
    applic = output_json["configuration"]["security"]["policies"]["global"]["policy"][22]["match"]["application"]
    to_zone = output_json["configuration"]["security"]["policies"]["global"]["policy"][22]["match"]["to-zone"]
    th = output_json["configuration"]["security"]["policies"]["global"]["policy"][22]["then"]
    th_min = (min(th, key=th.get))
    juniper = str(name["name"]), sour_addr[0], dest_name["name"], dest_ip["name"], applic[0], "-", to_zone[0], th_min
    out.write(', '.join(juniper))
    out.write('\n')
#policy24
with open(path,'a') as out:
    name = output_json["configuration"]["security"]["policies"]["global"]["policy"][24]
    sour_addr = output_json["configuration"]["security"]["policies"]["global"]["policy"][24]["match"]["source-address"]
    dest_name = output_json["configuration"]["security"]["address-book"][0]["address"][5]
    dest_ip = output_json["configuration"]["security"]["address-book"][0]["address"][5]["dns-name"][0]
    applic = output_json["configuration"]["security"]["policies"]["global"]["policy"][24]["match"]["application"]
    th = output_json["configuration"]["security"]["policies"]["global"]["policy"][24]["then"]
    th_min = (min(th, key=th.get))
    juniper = str(name["name"]), sour_addr[0], dest_name["name"], dest_ip["name"], applic[0], "-", "-", th_min
    out.write(', '.join(juniper))
    out.write('\n')
with open(path,'a') as out:
    dest_name = output_json["configuration"]["security"]["address-book"][0]["address"][6]
    dest_ip = output_json["configuration"]["security"]["address-book"][0]["address"][6]["dns-name"][0]
    applic = output_json["configuration"]["security"]["policies"]["global"]["policy"][24]["match"]["application"]
    juniper = "_", "_", dest_name["name"], dest_ip["name"], applic[1], "-", "_", "_"
    out.write(', '.join(juniper))
    out.write('\n')
dest24 = [19, 10, 11, 20, 51]
with open(path,'a') as out:
    for x in dest24:
        dest_name = output_json["configuration"]["security"]["address-book"][0]["address"][x]
        dest_ip = output_json["configuration"]["security"]["address-book"][0]["address"][x]["dns-name"][0]
        juniper = "_", "_", dest_name["name"], dest_ip["name"], "-", "-", "_", "_"
        out.write(', '.join(juniper))
        out.write('\n')
#policy25
with open(path,'a') as out:
    name = output_json["configuration"]["security"]["policies"]["global"]["policy"][25]
    sour_addr = output_json["configuration"]["security"]["policies"]["global"]["policy"][25]["match"]["source-address"]
    #dest_addr = output_json["configuration"]["security"]["policies"]["global"]["policy"][0]["match"]["destination-address"]
    dest_ip = output_json["configuration"]["security"]["address-book"][0]["address"][12]
    applic = output_json["configuration"]["security"]["policies"]["global"]["policy"][25]["match"]["application"]
    from_zone = output_json["configuration"]["security"]["policies"]["global"]["policy"][25]["match"]["from-zone"]
    th = output_json["configuration"]["security"]["policies"]["global"]["policy"][25]["then"]
    th_min = (min(th, key=th.get))
    juniper = str(name["name"]), sour_addr[0], dest_ip["name"], dest_ip["ip-prefix"], applic[0], from_zone[0], "-", th_min
    out.write(', '.join(juniper))
    out.write('\n')
dest25 = [13, 14, 42, 43, 48, 44, 45, 46, 47]
with open(path,'a') as out:
    for x in dest25:
        dest_ip = output_json["configuration"]["security"]["address-book"][0]["address"][x]
        juniper = "_", "_", dest_ip["name"], dest_ip["ip-prefix"], "-", "-", "-", "_"
        out.write(', '.join(juniper))
        out.write('\n')
#policy26
with open(path,'a') as out:
    name = output_json["configuration"]["security"]["policies"]["global"]["policy"][26]
    sour_addr = output_json["configuration"]["security"]["policies"]["global"]["policy"][26]["match"]["source-address"]
    dest_name = output_json["configuration"]["security"]["address-book"][0]["address"][23]
    dest_ip = output_json["configuration"]["security"]["address-book"][0]["address"][23]["dns-name"][0]
    applic = output_json["configuration"]["security"]["policies"]["global"]["policy"][26]["match"]["application"]
    rom_zone = output_json["configuration"]["security"]["policies"]["global"]["policy"][26]["match"]["from-zone"]
    th = output_json["configuration"]["security"]["policies"]["global"]["policy"][26]["then"]
    th_min = (min(th, key=th.get))
    juniper = str(name["name"]), sour_addr[0], dest_name["name"], dest_ip["name"], applic[0], from_zone[0], "-", th_min
    out.write(', '.join(juniper))
    out.write('\n')
dest26 = [26, 31, 30, 27, 28, 29]
with open(path,'a') as out:
    for x in dest26:
        dest_name = output_json["configuration"]["security"]["address-book"][0]["address"][x]
        dest_ip = output_json["configuration"]["security"]["address-book"][0]["address"][x]["dns-name"][0]
        juniper = "_", "_", dest_name["name"], dest_ip["name"], "-", "-", "_", "_"
        out.write(', '.join(juniper))
        out.write('\n')
#policy27
with open(path,'a') as out:
    name = output_json["configuration"]["security"]["policies"]["global"]["policy"][27]
    sour_addr = output_json["configuration"]["security"]["policies"]["global"]["policy"][27]["match"]["source-address"]
    #dest_addr = output_json["configuration"]["security"]["policies"]["global"]["policy"][0]["match"]["destination-address"]
    dest_ip = output_json["configuration"]["security"]["address-book"][0]["address"][15]
    applic = output_json["configuration"]["security"]["policies"]["global"]["policy"][27]["match"]["application"]
    from_zone = output_json["configuration"]["security"]["policies"]["global"]["policy"][27]["match"]["from-zone"]
    th = output_json["configuration"]["security"]["policies"]["global"]["policy"][27]["then"]
    th_min = (min(th, key=th.get))
    juniper = str(name["name"]), sour_addr[0], dest_ip["name"], dest_ip["ip-prefix"], applic[0], from_zone[0], "-", th_min
    out.write(', '.join(juniper))
    out.write('\n')
with open(path,'a') as out:
    dest_ip = output_json["configuration"]["security"]["address-book"][0]["address"][18]
    applic = output_json["configuration"]["security"]["policies"]["global"]["policy"][27]["match"]["application"]
    from_zone = output_json["configuration"]["security"]["policies"]["global"]["policy"][27]["match"]["from-zone"]
    juniper = "_", "_", dest_ip["name"], dest_ip["ip-prefix"], applic[1], from_zone[1], "-", "_"
    out.write(', '.join(juniper))
    out.write('\n')
from_zone27 = [2, 3, 4]
with open(path,'a') as out:
    for x in from_zone27:
        from_zone = output_json["configuration"]["security"]["policies"]["global"]["policy"][27]["match"]["from-zone"]
        juniper = "_", "_", "_", "_", "_", from_zone[x], "-", "_"
        out.write(', '.join(juniper))
        out.write('\n')
#policy28
with open(path,'a') as out:
    name = output_json["configuration"]["security"]["policies"]["global"]["policy"][28]
    sour_addr = output_json["configuration"]["security"]["policies"]["global"]["policy"][28]["match"]["source-address"]
    #dest_addr = output_json["configuration"]["security"]["policies"]["global"]["policy"][0]["match"]["destination-address"]
    dest_ip = output_json["configuration"]["security"]["address-book"][0]["address"][15]
    applic = output_json["configuration"]["security"]["policies"]["global"]["policy"][28]["match"]["application"]
    from_zone = output_json["configuration"]["security"]["policies"]["global"]["policy"][28]["match"]["from-zone"]
    th = output_json["configuration"]["security"]["policies"]["global"]["policy"][28]["then"]
    th_min = (min(th, key=th.get))
    juniper = str(name["name"]), sour_addr[0], dest_ip["name"], dest_ip["ip-prefix"], applic[0], from_zone[0], "-", th_min
    out.write(', '.join(juniper))
    out.write('\n')
with open(path,'a') as out:
    dest_ip = output_json["configuration"]["security"]["address-book"][0]["address"][18]
    from_zone = output_json["configuration"]["security"]["policies"]["global"]["policy"][28]["match"]["from-zone"]
    juniper = "_", "_", dest_ip["name"], dest_ip["ip-prefix"], "-", from_zone[1], "-", "_"
    out.write(', '.join(juniper))
    out.write('\n')
with open(path,'a') as out:
    dest_ip = output_json["configuration"]["security"]["address-book"][0]["address"][47]
    from_zone = output_json["configuration"]["security"]["policies"]["global"]["policy"][28]["match"]["from-zone"]
    juniper = "_", "_", dest_ip["name"], dest_ip["ip-prefix"], "-", from_zone[2], "-", "_"
    out.write(', '.join(juniper))
    out.write('\n')
from_zone28 = [3, 4]
with open(path,'a') as out:
    for x in from_zone28:
        from_zone = output_json["configuration"]["security"]["policies"]["global"]["policy"][28]["match"]["from-zone"]
        juniper = "_", "_", "_", "_", "_", from_zone[x], "-", "_"
        out.write(', '.join(juniper))
        out.write('\n')
#policy29
with open(path,'a') as out:
    name = output_json["configuration"]["security"]["policies"]["global"]["policy"][29]
    sour_addr = output_json["configuration"]["security"]["policies"]["global"]["policy"][29]["match"]["source-address"]
    #dest_addr = output_json["configuration"]["security"]["policies"]["global"]["policy"][0]["match"]["destination-address"]
    dest_ip = output_json["configuration"]["security"]["address-book"][0]["address"][40]
    applic = output_json["configuration"]["security"]["policies"]["global"]["policy"][29]["match"]["application"]
    from_zone = output_json["configuration"]["security"]["policies"]["global"]["policy"][29]["match"]["from-zone"]
    th = output_json["configuration"]["security"]["policies"]["global"]["policy"][29]["then"]
    th_min = (min(th, key=th.get))
    juniper = str(name["name"]), sour_addr[0], dest_ip["name"], dest_ip["ip-prefix"], applic[0], from_zone[0], "-", th_min
    out.write(', '.join(juniper))
    out.write('\n')
dest29 = [41, 25]
with open(path,'a') as out:
    for x in dest29:
        dest_ip = output_json["configuration"]["security"]["address-book"][0]["address"][x]
        juniper = "_", "_", dest_ip["name"], dest_ip["ip-prefix"], "-", "-", "-", "_"
        out.write(', '.join(juniper))
        out.write('\n')
with open(path,'a') as out:
    dest_name = output_json["configuration"]["security"]["address-book"][0]["address"][24]
    dest_ip = output_json["configuration"]["security"]["address-book"][0]["address"][24]["dns-name"][0]
    juniper = "_", "_", dest_name["name"], dest_ip["name"], "-", "-", "_", "_"
    out.write(', '.join(juniper))
    out.write('\n')
#policy30
with open(path,'a') as out:
    name = output_json["configuration"]["security"]["policies"]["global"]["policy"][30]
    sour_addr = output_json["configuration"]["security"]["policies"]["global"]["policy"][30]["match"]["source-address"]
    #dest_addr = output_json["configuration"]["security"]["policies"]["global"]["policy"][0]["match"]["destination-address"]
    dest_ip = output_json["configuration"]["security"]["address-book"][0]["address"][16]
    applic = output_json["configuration"]["security"]["policies"]["global"]["policy"][30]["match"]["application"]
    from_zone = output_json["configuration"]["security"]["policies"]["global"]["policy"][30]["match"]["from-zone"]
    th = output_json["configuration"]["security"]["policies"]["global"]["policy"][30]["then"]
    th_min = (min(th, key=th.get))
    juniper = str(name["name"]), sour_addr[0], dest_ip["name"], dest_ip["ip-prefix"], applic[0], from_zone[0], "-", th_min
    out.write(', '.join(juniper))
    out.write('\n')
dest30 = [17, 18, 49, 47]
with open(path,'a') as out:
    for x in dest30:
        dest_ip = output_json["configuration"]["security"]["address-book"][0]["address"][x]
        juniper = "_", "_", dest_ip["name"], dest_ip["ip-prefix"], "-", "-", "-", "_"
        out.write(', '.join(juniper))
        out.write('\n')
#policy31
with open(path,'a') as out:
    name = output_json["configuration"]["security"]["policies"]["global"]["policy"][31]
    sour_addr = output_json["configuration"]["security"]["policies"]["global"]["policy"][31]["match"]["source-address"]
    dest_name = output_json["configuration"]["security"]["address-book"][0]["address"][21]
    dest_ip = output_json["configuration"]["security"]["address-book"][0]["address"][21]["dns-name"][0]
    applic = output_json["configuration"]["security"]["policies"]["global"]["policy"][31]["match"]["application"]
    from_zone = output_json["configuration"]["security"]["policies"]["global"]["policy"][31]["match"]["from-zone"]
    th = output_json["configuration"]["security"]["policies"]["global"]["policy"][31]["then"]
    th_min = (min(th, key=th.get))
    juniper = str(name["name"]), sour_addr[0], dest_name["name"], dest_ip["name"], applic[0], from_zone[0], "-", th_min
    out.write(', '.join(juniper))
    out.write('\n')
from_zone28 = [1, 2]
with open(path,'a') as out:
    for x in from_zone28:
        from_zone = output_json["configuration"]["security"]["policies"]["global"]["policy"][31]["match"]["from-zone"]
        juniper = "_", "_", "_", "_", "_", from_zone[x], "-", "_"
        out.write(', '.join(juniper))
        out.write('\n')
#policy32
with open(path,'a') as out:
    name = output_json["configuration"]["security"]["policies"]["global"]["policy"][32]
    sour_addr = output_json["configuration"]["security"]["policies"]["global"]["policy"][32]["match"]["source-address"]
    dest_name = output_json["configuration"]["security"]["address-book"][0]["address"][52]
    dest_ip = output_json["configuration"]["security"]["address-book"][0]["address"][52]["dns-name"][0]
    applic = output_json["configuration"]["security"]["policies"]["global"]["policy"][32]["match"]["application"]
    from_zone = output_json["configuration"]["security"]["policies"]["global"]["policy"][32]["match"]["from-zone"]
    to_zone = output_json["configuration"]["security"]["policies"]["global"]["policy"][32]["match"]["to-zone"]
    th = output_json["configuration"]["security"]["policies"]["global"]["policy"][32]["then"]
    th_min = (min(th, key=th.get))
    juniper = str(name["name"]), sour_addr[0], dest_name["name"], dest_ip["name"], applic[0], from_zone[0], to_zone[0], th_min
    out.write(', '.join(juniper))
    out.write('\n')
with open(path,'a') as out:
    applic = output_json["configuration"]["security"]["policies"]["global"]["policy"][32]["match"]["application"]
    juniper = "_", "_", "_", "_", applic[1], "-", "_", "_"
    out.write(', '.join(juniper))
    out.write('\n')
#policy33
with open(path,'a') as out:
    name = output_json["configuration"]["security"]["policies"]["global"]["policy"][33]
    sour_addr = output_json["configuration"]["security"]["policies"]["global"]["policy"][33]["match"]["source-address"]
    dest_name = output_json["configuration"]["security"]["address-book"][0]["address"][50]
    dest_ip = output_json["configuration"]["security"]["address-book"][0]["address"][50]["dns-name"][0]
    applic = output_json["configuration"]["security"]["policies"]["global"]["policy"][33]["match"]["application"]
    from_zone = output_json["configuration"]["security"]["policies"]["global"]["policy"][33]["match"]["from-zone"]
    th = output_json["configuration"]["security"]["policies"]["global"]["policy"][33]["then"]
    th_min = (min(th, key=th.get))
    juniper = str(name["name"]), sour_addr[0], dest_name["name"], dest_ip["name"], applic[0], from_zone[0], "-", th_min
    out.write(', '.join(juniper))
    out.write('\n')
with open(path,'a') as out:
    from_zone = output_json["configuration"]["security"]["policies"]["global"]["policy"][33]["match"]["from-zone"]
    juniper = "_", "_", "_", "_", "_", from_zone[1], "_", "_"
    out.write(', '.join(juniper))
    out.write('\n')
#policy34
with open(path,'a') as out:
    name = output_json["configuration"]["security"]["policies"]["global"]["policy"][34]
    sour_addr = output_json["configuration"]["security"]["policies"]["global"]["policy"][34]["match"]["source-address"]
    #dest_addr = output_json["configuration"]["security"]["policies"]["global"]["policy"][0]["match"]["destination-address"]
    dest_ip = output_json["configuration"]["security"]["address-book"][0]["address"][7]
    applic = output_json["configuration"]["security"]["policies"]["global"]["policy"][34]["match"]["application"]
    to_zone = output_json["configuration"]["security"]["policies"]["global"]["policy"][34]["match"]["to-zone"]
    try:
        th = output_json["configuration"]["security"]["policies"]["global"]["policy"][34]["then"]
    except TypeError:
        th_min = (min(th, key=th.get))
    juniper = str(name["name"]), sour_addr[0], dest_ip["name"], dest_ip["ip-prefix"], applic[0], "-", to_zone[0], th_min
    out.write(', '.join(juniper))
    out.write('\n')
with open(path,'a') as out:
    dest_ip = output_json["configuration"]["security"]["address-book"][0]["address"][8]
    juniper = "_", "_", dest_ip["name"], dest_ip["ip-prefix"], "-", "-", "-", "_"
    out.write(', '.join(juniper))
    out.write('\n')
with open(path,'a') as out:
    dest_ip = output_json["configuration"]["security"]["address-book"][0]["address"][9]
    juniper = "_", "_", dest_ip["name"], dest_ip["ip-prefix"], "-", "-", "-", "_"
    out.write(', '.join(juniper))
    out.write('\n')
#policy35
with open(path,'a') as out:
    name = output_json["configuration"]["security"]["policies"]["global"]["policy"][35]
    sour_addr = output_json["configuration"]["security"]["policies"]["global"]["policy"][35]["match"]["source-address"]
    dest_addr = output_json["configuration"]["security"]["policies"]["global"]["policy"][35]["match"]["destination-address"]
    applic = output_json["configuration"]["security"]["policies"]["global"]["policy"][35]["match"]["application"]
    to_zone = output_json["configuration"]["security"]["policies"]["global"]["policy"][35]["match"]["to-zone"]
    th = output_json["configuration"]["security"]["policies"]["global"]["policy"][35]["then"]
    th_min = (min(th, key=th.get))
    juniper = str(name["name"]), sour_addr[0], dest_addr[0], dest_addr[0], applic[0], "-", to_zone[0], th_min
    out.write(', '.join(juniper))
    out.write('\n')


#Json_file
with open(path) as file:
    reader = csv.reader(file)
    lines = [[sub.strip() for sub in line] for line in reader]

json_ = []
for line in lines:
    #temp_key = line[5]
    new = {
        "name": line[0],
        "sours_addr": line[1],
        "dest_addr": line[2],
        "dest_ip": line[3],
        "application": line[4],
        "from_zone": line[5],
        "to_zone": line[6],
        "thin": line[7]
    }
    json_.append(new)

with open('/home/user/Документы/table_jun/result.json', 'wt') as file:
    json.dump(json_, file, indent=4)

data = open('/home/user/Документы/table_jun/result.json').read()
with open('/home/user/Документы/table_jun/table.html','wt') as out:
    print(json2html.convert(json = data), file=out)