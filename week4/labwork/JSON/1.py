import json

jsondata = open('c:/Users/User/Desktop/pp2_homework/PP2_Homework-8/week4/labwork/JSON/sample-data.json').read()

json_object = json.loads(jsondata)
print(
    "=======================================================================================" "\n"
    "DN                                                 Description           Speed    MTU" "\n" 
    "-------------------------------------------------- --------------------  ------  ------")
imdata = json_object["imdata"]
for i in imdata:
        dn = i["l1PhysIf"]["attributes"]["dn"]
        descr = i["l1PhysIf"]["attributes"]["descr"]
        speed = i["l1PhysIf"]["attributes"]["speed"]
        mtu = i["l1PhysIf"]["attributes"]["mtu"]
        # print fields formatted in columns
        print("{0:50} {1:20} {2:7} {3:6}".format(dn,descr,speed,mtu))