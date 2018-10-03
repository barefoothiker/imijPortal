from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.template import RequestContext
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.http import HttpResponse

from imijportalapp.models import *
from operator import itemgetter

import pandas as pd
import os
import sys
import json
import traceback

from django.conf import settings
import numpy as np
import seaborn as sns


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/registration/")
    else:
        form = UserCreationForm()
    return render(request, "registration/register.html", {
        'form': form,
    })

#@login_required
def landing(request):
    return render(request, "daphniFrontend/landing.html", {

    })

#@login_required
#@csrf_protect
def processLanding(request):

    ''' Function process landing page submit
    Input: params.request
    Output: Delegates task to corresponding handler
    '''
    daphniFrontendHomeButton = request.POST.get("daphniFrontendHomeButton","1" )

    if daphniFrontendHomeButton == "0":
        return submittedJobs ( request )
    elif daphniFrontendHomeButton == "1" :
        return listProjects( request )
    elif daphniFrontendHomeButton == "2" :
        return showEvidenceMatrix( request )
    elif daphniFrontendHomeButton == "3" :
        return listDatabases( request )


def listdirs(folder):
    return [d for d in os.listdir(folder) if os.path.isdir(os.path.join(folder, d))]

def listfiles(folder):
#      return [
#         d for d in (os.path.join(folder, d1) for d1 in os.listfile(folder))
#         if os.path.isfile(d)
#     ]
    return [d for d in os.listdir(folder) if os.path.isfile(os.path.join(folder, d))]



def listdirsfullpath(folder):
    return [
        d for d in (os.path.join(folder, d1) for d1 in os.listdir(folder))
        if os.path.isdir(d)
    ]

def listPatients(request):
    try:
        patients= Patient.objects.all();
        patients = [{"id":p.id,"daphniId":p.daphniId,"userStoryId":p.userStoryId ,"samples":sorted([{"id":s.id,"name":s.name,"iteration":s.iteration} for s in p.sample_set.all()], key=itemgetter('iteration'))} for p in patients]
        patientsJsonString = json.dumps(list(patients))
        print ( "patientsJsonString =  " + str(patientsJsonString))
    except:
        traceback.print_exc(file=sys.stdout)
    return HttpResponse(patientsJsonString, content_type="application/json")


def listProjectPatients(request):
    try:
        projectId = request.POST.get("projectId",0)
        print ( "listProjectPatients projectId =  " + str(projectId))

        dirList = listdirs(settings.BASE_DATA_FOLDER)
        dirListFilter =  [x for x in dirList if x in settings.TFS_PROJECTS]
        projectName = dirListFilter[int (projectId)]

        projectPath = settings.BASE_DATA_FOLDER+projectName
        print ("projectId="+str(projectId)+ "projectPath="+str(projectPath))
        patientObjList = []
        dirList = listdirs(projectPath)
        dirList.sort()
        print (dirList)

        dirListFilter =  [x for x in dirList if all(i.isdigit() for i in x)]
        listPatients = [{"id":i, "projectId":projectId,"userStoryId":x} for i,x in enumerate(dirListFilter)]
        print ( "list patients =  " + str(listPatients))
        projectPatientsJsonString = json.dumps(listPatients)
        print ( "projectPatientsJsonString =  " + str(projectPatientsJsonString))
    except:
        traceback.print_exc(file=sys.stdout)
    return HttpResponse(projectPatientsJsonString, content_type="application/json")


def listPatientIterations(request):
    try:
        userStoryId = request.POST.get("userStoryId",0)
        print ( "listPatientIterations  userStoryId = " +str(userStoryId))
        projectId = request.POST.get("projectId",0)
        print ( "listProjectPatients projectId =  " + str(projectId))

        dirList = listdirs(settings.BASE_DATA_FOLDER)
        dirListFilter =  [x for x in dirList if x in settings.TFS_PROJECTS]
        projectName = dirListFilter[int (projectId)]

        projectPath = settings.BASE_DATA_FOLDER+projectName
        path =projectPath+"/"+userStoryId
        print ("path = "+str(path))
        patientObjList = []
        dirList = listdirs(path)
        print (dirList)
        listIterations = [{"id":i, "iterationId":x, "userStoryId":userStoryId,"projectId":projectId} for i,x in enumerate(dirList)]
        iterationsJsonString = json.dumps(listIterations)
        print ( "listPatientIterations:iterationsJsonString =  " + str(iterationsJsonString))
    except:
        traceback.print_exc(file=sys.stdout)
    return HttpResponse(iterationsJsonString, content_type="application/json")

#the json file format is list of repeated elements [{"Gene":"NCOA1","Zscore":4.1942},{"Gene":"BRF1","Zscore":3.5696}....
#the function will take the keys for each json file and put it in a map "columns" and values in "values"
#this map will reside in another map as "flowData"  and it associated with json file name  id.
#return list of maps of flowData and file name
def patientIterationDetails0(request):
    try:
        iterationId = request.POST.get("iterationId",0)
        userStoryId = request.POST.get("userStoryId",0)
        projectId = request.POST.get("projectId",0)
        print ("patientIterationDetails:iterationId = "+str(iterationId))

        dirList = listdirs(settings.BASE_DATA_FOLDER)
        dirListFilter =  [x for x in dirList if x in settings.TFS_PROJECTS]
        projectName = dirListFilter[int (projectId)]

        projectPath = settings.BASE_DATA_FOLDER+projectName
        path =projectPath+"/"+userStoryId+"/"+iterationId+"/report/Patient_report_html/"
        print ("patientIterationDetails:path = "+str(path))
        jsonFileList = [pos_json for pos_json in listfiles(path) if pos_json.endswith('.json')]
        pngPathwayFileList = [pos_json for pos_json in listfiles(path) if pos_json.endswith('.png') and pos_json.startswith('pathway')]
        pngOutlierFileList = [pos_json for pos_json in listfiles(path) if pos_json.endswith('.png') and pos_json.startswith('outlier')]
        jsonDataMapList = []

        objMap={}
        for index, jsonFileName in enumerate (jsonFileList):
            #print("loading: "+path+jsonFileName);
            data = json.load(open(path+jsonFileName,"r"))
            dataMap=collections.OrderedDict()
            dataMap["id"] = index
            dataMap["columns"] = list(data[0]["data"][0].keys())
            dataMap["values"] = [list(x.values()) for x in data[0]["data"]]
            #print (dataMap)
            jsonDataMap = collections.OrderedDict()
            jsonDataMap["id"] = index
            jsonDataMap["fileName"] = jsonFileName
            jsonDataMap["flowData"] = dataMap
            jsonDataMap["order"] = data[0]["info"]["order"]
            jsonDataMap["caption"] = data[0]["info"]["caption"]
            jsonDataMapList.append(jsonDataMap)

#         print ("jsonDataMapList: " +str(jsonDataMapList))
        objMap["iterationDetailList"] = jsonDataMapList;
        objMap["iterationPathwayImages"] = pngPathwayFileList;
        objMap["iterationOutlierImages"] = pngOutlierFileList;
        objMap["basePath"]=path;
        print ("objMap: " +str(json.dumps(objMap)))
    except:
        traceback.print_exc(file=sys.stdout)
    return HttpResponse(json.dumps(objMap), content_type="application/json")

def getPatient(request):
    try:
        projectId = request.POST.get("userStoryId",0)
        print ( "getPatient userStoryId =  " + str(userStoryId))


        patientPath = settings.BASE_DATA_FOLDER+setting.CURRENT_PROJECT+ str(userStoryId)
        print ("patientPath="+str(patientPath))
        patientIterations = []
        dirList = listdirs(patientPath)
        print (dirList)


        listIterations = [{"id":i, "iteration":x} for i,x in enumerate(dirList)]

        print ( "listIterations =  " + str(listIterations))
        patientIterationJsonString = json.dumps(listIterations)
        print ( "patientIterationJsonString =  " + str(patientIterationJsonString))
    except:
        traceback.print_exc(file=sys.stdout)
    return HttpResponse(patientIterationJsonString, content_type="application/json")













#the json file format is list of repeated elements [{"Gene":"NCOA1","Zscore":4.1942},{"Gene":"BRF1","Zscore":3.5696}....
#the function will take the keys from one big json file already in map "columns" and values format
#this map will reside in another map as "flowData"  and it associated with json file name  id.

def patientIterationDetails(request):
    try:
        iterationId = request.POST.get("iterationId",0)
        userStoryId = request.POST.get("userStoryId",0)
        projectId = request.POST.get("projectId",0)
        print ("itai patientIterationDetails:iterationId = "+str(iterationId))

        dirList = listdirs(settings.BASE_DATA_FOLDER)
        dirListFilter =  [x for x in dirList if x in settings.TFS_PROJECTS]
        projectName = dirListFilter[int (projectId)]

        projectPath = settings.BASE_DATA_FOLDER+projectName
        path =projectPath+"/"+userStoryId+"/"+iterationId+"/report/Patient_html_v2/"
        print ("patientIterationDetails:path = "+str(path))
        jsonFileList = [pos_json for pos_json in listfiles(path) if pos_json.endswith('big.json')]
        IterationDetailsList = []

        for index, jsonFileName in enumerate (jsonFileList):
            print("loading: "+path+jsonFileName);
            data = json.load(open(path+jsonFileName,"r", encoding="ISO-8859-1"))
            print("data: " +str(data))
            IterationDetails = collections.OrderedDict()
            IterationDetails["id"] = index
            IterationDetails["fileName"] = jsonFileName
            IterationDetails["iterationData"] = data

            IterationDetailsList.append(IterationDetails)

#         print ("IterationDetailsList: " +str(json.dumps(IterationDetailsList)))
    except:
        traceback.print_exc(file=sys.stdout)
    return HttpResponse(json.dumps(data), content_type="application/json")


def comparePatientIterations(request):
    try:
        iterationId = request.POST.get("iterationId",0)
        userStoryId = request.POST.get("userStoryId",0)
        projectId = request.POST.get("projectId",0)
        print ("itai patientIterationDetails:iterationId = "+str(iterationId))

        dirList = listdirs(settings.BASE_DATA_FOLDER)
        dirListFilter =  [x for x in dirList if x in settings.TFS_PROJECTS]
        projectName = dirListFilter[int (projectId)]

        projectPath = settings.BASE_DATA_FOLDER+projectName
        path =projectPath+"/"+userStoryId+"/"+iterationId+"/report/Patient_html_v2/"
        print ("patientIterationDetails:path = "+str(path))
        jsonFileList = [pos_json for pos_json in listfiles(path) if pos_json.endswith('big.json')]
        IterationDetailsList = []

        for index, jsonFileName in enumerate (jsonFileList):
            print("loading: "+path+jsonFileName);
            data = json.load(open(path+jsonFileName,"r", encoding="ISO-8859-1"))
            print("data: " +str(data))
            IterationDetails = collections.OrderedDict()
            IterationDetails["id"] = index
            IterationDetails["fileName"] = jsonFileName
            IterationDetails["iterationData"] = data

            IterationDetailsList.append(IterationDetails)

#         print ("IterationDetailsList: " +str(json.dumps(IterationDetailsList)))
    except:
        traceback.print_exc(file=sys.stdout)
    return HttpResponse(json.dumps(data), content_type="application/json")




def getMutations(request):
    try:
        mutId = request.POST.get("mutId",0)
        print ( "getMutations mutId =  " + str(mutId))


        patientPath = settings.BASE_DATA_FOLDER+setting.CURRENT_PROJECT+ str(userStoryId)
        print ("patientPath="+str(patientPath))
        patientIterations = []
        dirList = listdirs(patientPath)
        print (dirList)


        listIterations = [{"id":i, "iteration":x} for i,x in enumerate(dirList)]

        print ( "listIterations =  " + str(listIterations))
        patientIterationJsonString = json.dumps(listIterations)
        print ( "patientIterationJsonString =  " + str(patientIterationJsonString))
    except:
        traceback.print_exc(file=sys.stdout)
    return HttpResponse(patientIterationJsonString, content_type="application/json")



def listMutationDetails(request):
    try:
        vc = request.GET.get("variantClass",'')
        print('vc='+str(vc))
        data = list(MutationDetails.objects.filter(variantClass=vc).values())
        print('data='+str(data))
#         print([str(x.start)+":"+x.cDNAChange + ":" + str(x.sample.patient.daphniId) for x in qs])
    except:
        traceback.print_exc(file=sys.stdout)

    return HttpResponse(json.dumps(data), content_type="application/json")
