import random
import csv
from collections import OrderedDict
from datetime import datetime
import time
from math import log
import json
import seaborn as sns
import numbers
import argparse
import builtins
from distutils import filelist
import os
import collections



parser=argparse.ArgumentParser(
    description=''' Generates single Json from multiple ''')
parser.add_argument('-d', dest = 'Json_dir' , help='directory of report json files ',required=True)
parser.add_argument('-o', dest = 'output_json' , help='output file of .json file',required=True)

args=parser.parse_args()


path = args.Json_dir

def listfiles(folder):
#      return [
#         d for d in (os.path.join(folder, d1) for d1 in os.listfile(folder))
#         if os.path.isfile(d)
#     ]
    return [d for d in os.listdir(folder) if os.path.isfile(os.path.join(folder, d))]

jsonFileList = [pos_json for pos_json in listfiles(path) if pos_json.endswith('.json')]
#pngPathwayFileList = [pos_json for pos_json in listfiles(path) if pos_json.endswith('.png') and pos_json.startswith('pathway')]
#pngOutlierFileList = [pos_json for pos_json in listfiles(path) if pos_json.endswith('.png') and pos_json.startswith('outlier')]
jsonDataMapList = []
       
#objMap={}
for index, jsonFileName in enumerate (jsonFileList):    
    print("loading: "+path+jsonFileName);
    data = json.load(open(path+jsonFileName,"r"), object_pairs_hook=OrderedDict)
    if data[0]["info"]["type"] == "table":
        dataMap= collections.OrderedDict()
        infoMap= collections.OrderedDict()
        infoMap["id"] = index
        infoMap["fileName"] = jsonFileName
        infoMap["order"] = data[0]["info"]["order"]
        infoMap["caption"] = data[0]["info"]["caption"]
        infoMap["type"] =  data[0]["info"]["type"]
       
        dataMap["id"] = index
        dataMap["columns"] = list(data[0]["data"][0].keys())
        dataMap["values"] = [list(x.values()) for x in data[0]["data"]]

        jsonDataMap = collections.OrderedDict()
        jsonDataMap["id"] = index
        jsonDataMap["flowInfo"] = infoMap        
        jsonDataMap["flowData"] = dataMap

        jsonDataMapList.append(jsonDataMap)
    elif data[0]["info"]["type"] == "image":
        dataMap= collections.OrderedDict()
        infoMap= collections.OrderedDict()
        infoMap["id"] = index
        infoMap["fileName"] = jsonFileName
        infoMap["order"] = data[0]["info"]["order"]
        infoMap["caption"] = data[0]["info"]["caption"]
        infoMap["type"] =  data[0]["info"]["type"]
       
        dataMap["id"] = index
        dataMap["columns"] = data[0]["data"].keys()
        dataMap["values"] = data[0]["data"]["image"]
   
        jsonDataMap = collections.OrderedDict()
        jsonDataMap["id"] = index
        jsonDataMap["flowInfo"] = infoMap        
        jsonDataMap["flowData"] = dataMap
   
    elif data[0]["info"]["type"] == "metrics":
        dataMap= collections.OrderedDict()
        infoMap= collections.OrderedDict()
        infoMap["id"] = index
        infoMap["fileName"] = jsonFileName
        infoMap["order"] = data[0]["info"]["order"]
        infoMap["caption"] = data[0]["info"]["caption"]
        infoMap["type"] =  data[0]["info"]["type"]
       
        dataMap["id"] = index
        dataMap["columns"] = list(data[0]["data"][0].keys())
        dataMap["values"] = [list(x.values()) for x in data[0]["data"]]
   
        jsonDataMap = collections.OrderedDict()
        jsonDataMap["id"] = index
        jsonDataMap["flowInfo"] = infoMap        
        jsonDataMap["flowData"] = dataMap
    
#         print ("jsonDataMapList: " +str(jsonDataMapList))
#objMap["iterationDetailList"] = jsonDataMapList;
#objMap["iterationPathwayImages"] = pngPathwayFileList;
#objMap["iterationOutlierImages"] = pngOutlierFileList;
#objMap["basePath"]=path;
print (json.dumps(jsonDataMapList))

with open(args.output_json, 'w') as outfile:
    json.dump(jsonDataMapList, outfile)
