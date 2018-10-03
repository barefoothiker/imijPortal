from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.template import RequestContext
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.http import HttpResponse

from lymePortal.models import *
from lymePortal.lymePortalObjs import *
from lymePortal.lymePortalConstants import *

import pandas as pd
from pandas import DataFrame
import os
import sys
import traceback

import io
import re
import shutil

from django.conf import settings
import numpy
import itertools
import csv
import datetime
import os.path

from io import StringIO
import random
import csv
from collections import OrderedDict
from datetime import datetime
import time
from math import log

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
    return render(request, "lymePortal/landing.html", {

    })

#@login_required
#@csrf_protect
def processLanding(request):

    ''' Function process landing page submit
    Input: params.request
    Output: Delegates task to corresponding handler
    '''
    lymePortalHomeButton = request.POST.get("lymePortalHomeButton","1" )

    if lymePortalHomeButton == "0":
        return submittedJobs ( request )
    elif lymePortalHomeButton == "1" :
        return listProjects( request )
    elif lymePortalHomeButton == "2" :
        return showEvidenceMatrix( request )
    elif lymePortalHomeButton == "3" :
        return showPubMedData( request )

def submittedJobs(request):
    try:
        print ( " in submittted jobs ")
    except:
      traceback.print_exc(file=sys.stdout)
    return

def uploadData(request):
    try:
        print ( " in upload data ")
    except:
      traceback.print_exc(file=sys.stdout)
    return

def showEvidenceMatrix(request):
    try:
        eegData = loadmat('EEG181.mat')
    except:
      traceback.print_exc(file=sys.stdout)
    return

def showPubMedData(request):
    try:
        eegData = loadmat('EEG181.mat')
    except:
      traceback.print_exc(file=sys.stdout)
    return

def showPubMedDetails(request):
    try:
        eegData = loadmat('EEG181.mat')
    except:
      traceback.print_exc(file=sys.stdout)
    return

@login_required
def listProjects(request):

    projectObjList = []

    if request.user.is_superuser:
        projects = Project.objects.all()
    else:
        projects = Project.objects.filter(user = request.user)

    edfFileType = FileType.objects.filter(name = "edfFile")[0]

    for project in projects:

        projectObj = ProjectObj()

        projectObj.project = project

        dataFiles = Datafile.objects.filter ( project = project, fileType = edfFileType )

        projectObjList.append(projectObj)

    return render(request, 'lymePortal/listProjects.html', {
        "projectObjList":projectObjList,
    }, RequestContext(request))

@login_required
def addProject(request):

    try:

        projects = Project.objects.filter ( user = request.user)

    except:
        traceback.print_exc(file=sys.stdout)
        #messages.add_message(request, messages.ERROR, 'Error occurred while fetching details for sample detail id' + str(sampleDetailId) )

    return render(request, 'lymePortal/addProject.html', {

        "projects" : projects ,

    })

@login_required
def submitAddProject(request):

    messages = []

    try:

        projectName = request.POST.get("projectName","" )
        projectDescription = request.POST.get("projectDescription","" )

        project = Project ( name = projectName, user = request.user, description = projectDescription )
        project.save()

        edfFileType = FileType.objects.filter(name = "edfFile")[0]
        dataFiles = Datafile.objects.filter ( project = project, fileType = edfFileType )

    except:
        traceback.print_exc(file=sys.stdout)

    return render(request, 'chronux/listFiles.html', {
            "dataFiles":dataFiles,
            "project":project,
        })


# logging.basicConfig()
# logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)
#
# def page_range(page, last, span=5):
#     window = range(max(min(page - (span - 1) // 2, last - span + 1), 1),
#                  min(max(page + span // 2, span), last) + 1)
#     pre =[1,2,3]
#     if last <= 3:
#       pre = []
#     elif window[0] - pre[-1] > 1 :
#       pre = pre + ['...']
#
#     for p in pre :
#       if p in window:
#         window.remove(p)
#
#     post = [last - 2, last- 1, last]
#     if last > 3:
#       for p in post:
#         if p in window:
#           window.remove(p)
#       if len(window) > 0 and (post[0] - window[-1] > 1):
#         post = ['...'] + post
#     else :
#       post = []
#
#     if len(window) == 0 :
#       for p in pre :
#         if p in post:
#           post.remove(p)
#     pages = pre + window + post
#     return pages
#
# #@app.context_processor
# def utility_processor():
#   def create_dbid_url(dbid_type, dbid):
#     if dbid and dbid_type:
#       dbid_type = dbid_type.lower()
#       dbid = str(dbid)
#       if dbid_type == 'entrez':
#         url = "http://www.ncbi.nlm.nih.gov/gene/%s"
#       if dbid_type  == 'gene_symbol':
#         url = "http://www.genecards.org/cgi-bin/carddisp.pl?gene=%s"
#       if dbid_type == 'mesh':
#         url = "https://id.nlm.nih.gov/mesh/%s.html"
#       if dbid_type == 'chebi':
#         url = "https://www.ebi.ac.uk/chebi/searchId.do;?chebiId=CHEBI\%3A%s"
#       if dbid_type == 'uniprot':
#         url = "http://www.uniprot.org/uniprot/%s"
#       if dbid_type == 'chembl':
#         url = "https://www.ebi.ac.uk/chembl/compound/inspect/%s"
#       if dbid_type == 'drugbank':
#         url = "http://www.drugbank.ca/drugs/%s"
#       if dbid_type == 'snp':
#         dbid = dbid[0:2] + "=" + dbid[2:]
#         url = "http://www.ncbi.nlm.nih.gov/projects/SNP/snp_ref.cgi?%s"
#       try:
#         return url % (dbid)
#       except Exception as e:
#         return ""
#     else:
#       return ""
#   return dict(create_dbid_url=create_dbid_url)
#
# #@app.context_processor
# def utility_processor():
#   def sorting(order_by, field, current_order):
#     if order_by == field :
#       if current_order == 'asc' :
#         qs = "&order_by=%s&order=%s" % (field, 'desc')
#       elif current_order == 'desc' :
#         qs = '' # remove sort
#       else :
#         qs = "&order_by=%s&order=%s" % (field, 'asc')
#     else :
#       qs = "&order_by=%s&order=%s" % (field, 'asc')
#     return qs
#   return dict(sorting=sorting)
#
# #@app.context_processor
# #def utility_processor():
#   def qs_state(qs, name=None, remove=None):
#     """
#     cleans up the querystring to maintain state when adding values to querystring
#     """
#     strip_querystring = qs.split("?")
#     if len(strip_querystring) <= 1:
#       return len(strip_querystring)
#     else :
#       querystrings = strip_querystring[1].split("&")
#       out_qs = []
#       for qs in querystrings :
#         kv = qs.split("=")
#         if len(kv) <= 1:
#           continue
#         else :
#           key = qs.split("=")[0]
#           value = qs.split("=")[1]
#           if remove and key in remove:
#             continue
#           if (name is None) or (key == name):
#             value = [v for v in value.split(",") if v != 'None' and v != '']
#             value = list(OrderedDict.fromkeys(value))
#             pair = key + "=" + (",").join(value)
#             out_qs.append(pair)
#       return ('&').join(out_qs)
#   return dict(qs_state=qs_state)
#
# #@app.context_processor
# #def utility_processor():
#   def remove_dupes(qs):
#     """
#     removes duplicate values from querystring
#     """
#     if qs :
#       value = list(OrderedDict.fromkeys(qs.split(",")))
#       value = [v for v in value if v not in ['None','']]
#       value = (",").join(value)
#       return value
#   return dict(remove_dupes=remove_dupes)
#
#
# #@app.context_processor
# #def utility_processor():
#   def remove_filter(qs, field, remove):
#     """
#     drops a search, sort, or order by variable from the querystring.
#     """
#     qs = qs.split("&")
#     qs_out = []
#     for q in qs :
#       q = q.split("=")
#       if q[0] == field :
#         q[1] = ",".join([x for x in q[1].split(",") if x != remove])
#         line = q[0] + "=" + q[1]
#         if len(q[1]) > 0 :
#           qs_out.append(line)
#       else :
#         qs_out.append("=".join(q))
#     return "&".join(qs_out)
#   return dict(remove_filter=remove_filter)
#
# ###############################################
# ###  OMNI MATRIX
# ###############################################
# #@omni.route('/', strict_slashes=False)
# #@omni.route('/omni/', strict_slashes=False)
# #@omni.route('/omni/<int:page>', strict_slashes=False)
# def get_omni(page=1) :
#   layout = {'layout' : [
#               {'title' : 'Chemical NLP',
#                'field' : 'chemical_nlp_p',
#                'table' : 'lyme_omni_nlp_c',
#                'head_wrap' : True,
#                'type' : 'indicator',
#                'link' : True},
#               {'title' : 'Disease NLP',
#                'field' : 'disease_nlp_p',
#                'table' : 'lyme_omni_nlp_d',
#                'head_wrap' : True,
#                'type' : 'indicator',
#                'link' : True},
#                {'title' : 'Gene NLP',
#                'field' : 'gene_nlp_p',
#                'table' : 'lyme_omni_nlp_g',
#                'type' : 'indicator',
#                'head_wrap' : True,
#                'link' : True},
#               {'title' : 'SEA',
#                'field' : 'sea_p',
#                'table' : 'lyme_omni_sea_targets',
#                'type' : 'indicator',
#                'head_wrap' : False,
#                'link' : True},
#               {'title' : 'Drug Bank',
#                'field' : 'drugbank_p',
#                'table' : 'lyme_omni_drugbank_targets',
#                'type' : 'indicator',
#                'head_wrap' : False,
#                'link' : True},
#               {'title' : 'Meta P',
#                'field' : 'meta_p',
#                'table' : 'lyme_omni_meta_lyme_casevsctrl_v2',
#                'type' : 'val',
#                'head_wrap' : False,
#                'link' : True},
#               {'title' : 'Skin P',
#               'head_wrap' : False,
#                'field' : 'skin_p',
#                'table' : 'lyme_omni_eqtls',
#                'type' : 'val',
#                'link' : True},
#               {'title' : 'LCL P',
#                'field' : 'lcl_p',
#                'table' : 'lyme_omni_eqtls',
#                'type' : 'val',
#                'head_wrap' : False,
#                'link' : True},
#               {'title' : 'Fat P',
#                'field' : 'fat_p',
#                'head_wrap' : False,
#                'table' : 'lyme_omni_eqtls',
#                'type' : 'val',
#                'link' : True},
#               {'title' : 'Proteomic',
#                'field' : 'proteomics_p',
#                'table' : 'lyme_omni_proteomics',
#                'type' : 'val',
#                'head_wrap' : False,
#                'link' : True},
#               {'title' : 'V1',
#                'field' : 'v1_p',
#                'table' : 'lyme_omni_listofv1_ingenuity_uniq_eid',
#                'type' : 'indicator',
#                'head_wrap' : False,
#                'link' : False},
#               {'title' : 'V2',
#                'field' : 'v2_p',
#                'table' : 'lyme_omni_listofv2_ingenuity_uniq_eid',
#                'head_wrap' : False,
#                'type' : 'indicator',
#                'link' : False},
#               {'title' : 'V5',
#                'field' : 'v5_p',
#                'table' : 'lyme_omni_listofv5_ingenuity_uniq_eid',
#                'head_wrap' : False,
#                'type' : 'indicator',
#                'link' : False}
#             #   {'title' : 'Combined P: Meta & Skin & Proteomic',
#             #    'field' : 'combined_p_meta_skin_prot',
#             #    'head_wrap' : True,
#             #    'type' : 'val',
#             #    'link' : False},
#             #   {'title' : 'Combined P: Meta & Skin',
#             #    'field' : 'combined_p_meta_skin',
#             #    'head_wrap' : True,
#             #    'type' : 'val',
#             #    'link' : False},
#             #   {'title' : 'Combined P: >=2 {Meta | Skin | Proteomic}',
#             #    'field' : 'combined_p_meta_skin_prot_wildcard',
#             #    'head_wrap' : True,
#             #    'type' : 'val',
#             #    'link' : False}
#             ]
#           }
#   layout = OrderedDict(layout)
#   search = request.args.get('search')
#   download = request.args.get('download')
#   filter_by = request.args.get('filter_by')
#   order_by = request.args.get('order_by')
#   order = request.args.get("order")
#   per_page = request.args.get('per_page')
#   if per_page :
#     per_page = int(per_page)
#   else :
#     per_page = 15
#
#   omni_matrix = Omni.query
#
#   if search :
#     omni_matrix = omni_matrix.filter(Omni.gene_symbol.like('%' + search + '%') | \
#                                    Omni.entrez_gene_id.like('%' + search + '%'))
#
#   if order_by and order:
#     if order == "asc":
#       omni_matrix = omni_matrix.order_by(text('-' + order_by + ' desc'))
#     elif order == "desc":
#       omni_matrix = omni_matrix.order_by(text(order_by + ' desc'))
#   else :
#     omni_matrix = omni_matrix.order_by(text('-meta_p desc'))
#
#   if filter_by :
#     filters = filter_by.split(",")
#     filters = [filter for filter in filters if filter != 'None']
#     for f in filters :
#       omni_matrix = omni_matrix.filter( text(f + u' is not null') )
#
#   ## Data export
#   if download == 'csv' :
#     si = StringIO()
#     cw = csv.writer(si)
#     output_matrix = []
#     output_matrix.append(['Lyme ID','Entrez Gene Id','Gene Symbol','SEA','Drugbank',
#                      'Meta','Chemical NLP','Disease NLP','Gene NLP','eQTLs Skin',
#                      'eQTLs LCL','eQTLs Fat','Proteomics','V1','V2','V5', 'Combined P: Meta & Skin & Proteomic',
#                      'Combined P: Meta & Skin', 'Combined P: Meta Skin | Proteomic'])
#     for om in omni_matrix :
#       output_matrix.append([om.table_id, om.entrez_gene_id, om.gene_symbol, om.sea_p,
#                             om.drugbank_p, om.meta_p, om.chemical_nlp_p, om.disease_nlp_p,
#                             om.gene_nlp_p, om.skin_p, om.lcl_p, om.fat_p, om.proteomics_p,
#                             om.v1_p, om.v2_p, om.v5_p, om.combined_p_meta_skin_prot,
#                             om.combined_p_meta_skin, om.combined_p_meta_skin_prot_wildcard])
#     cw.writerows(output_matrix)
#     output = make_response(si.getvalue())
#     filename = "lyme_omni_nlp_" + str(datetime.now()).replace("-", "")[0:8] + ".csv"
#     output.headers["Content-Disposition"] = "attachment; filename=" + filename
#     output.headers["Content-type"] = "text/csv"
#     return output
#   ## end Data export
#
#   omni_matrix = omni_matrix.paginate(page, per_page, False)
#   omni_matrix_items = omni_matrix.items
#
#   pages = omni_matrix.pages
#   prev = 1
#   if page != 1 :
#     prev = page - 1
#
#   next = page
#   if page != pages :
#     next = page + 1
#
#   page_display = page_range(page, pages, span=10)
#
#   # records showing on page
#   max_records = per_page * page
#   if max_records > omni_matrix.total:
#     max_records = omni_matrix.total
#
#   showing = [per_page * page - per_page + 1, max_records]
#
#   meta = {
#     "total" : omni_matrix.total,
#     "pages" : pages,
#     "page_display" : page_display,
#     "page" : omni_matrix.page,
#     "next" : next,
#     "prev" : prev,
#     "has_next" : omni_matrix.has_next,
#     "order_by" : order_by,
#     "showing" : showing
#   }
#   return render_template('omni.html', omni_matrix=omni_matrix_items, meta=meta, layout=layout)
#
#
# ###############################################
# ###  OMNI MATRIX DETAIL
# ###############################################
# @app.route('/omni_detail/<source_table>/<int:entrez_gene_id>')
# def get_omni_detail(source_table, entrez_gene_id):
#   download = request.args.get('download')
#   if 'nlp' in source_table:
#     if source_table == 'lyme_omni_nlp_g':
#       nlp_type = 'gene'
#     elif source_table == 'lyme_omni_nlp_c':
#       nlp_type = 'chemical'
#     elif source_table == 'lyme_omni_nlp_d':
#       nlp_type = 'disease'
#     sql = """select distinct dbid_1, dbid_1_type, term_1, dbid_2, dbid_2_type, term_2, adjpvalue, coocurrence_count, relation, pvalue
#              from lyme_omni_nlp_meta
#              where lower(dbid_1_type) = 'entrez'
#              and dbid_1 = '%d'
#              and lower(term_2_type) = '%s'
#              and dbid_1 <> dbid_2
#              order by adjpvalue asc, pvalue asc, term_2 asc;""" % (entrez_gene_id, nlp_type)
#   else:
#     sql = """select * from %s where entrez_gene_id = %d;""" % (source_table, entrez_gene_id)
#
#   data = db.engine.execute(sql)
#   if download == 'csv' :
#     si = StringIO()
#     cw = csv.writer(si)
#     output_omni_detail = []
#     for dat in data :
#       line = []
#       for d in dat:
#         line.append(d)
#       output_omni_detail.append(line)
#     cw.writerows(output_omni_detail)
#     output = make_response(si.getvalue())
#     filename = "lyme_omni_detail_" + str(datetime.now()).replace("-", "")[0:8] + ".csv"
#     output.headers["Content-Disposition"] = "attachment; filename=" + filename
#     output.headers["Content-type"] = "text/csv"
#     return output
#   return render_template('omni_detail.html', data=data, source_table=source_table)
#
#
# ###############################################
# ###  NLP Omni
# ###############################################
# @omni.route('/pubmed/', strict_slashes=False)
# @omni.route('/pubmed/<int:page>', strict_slashes=False)
# def get_nlp(page=1, order_by='adjpvalue') :
#   primary = request.args.get('primary')
#   secondary = request.args.get('secondary')
#   search_primary = request.args.get('search-primary')
#   search_secondary = request.args.get('search-secondary')
#   download = request.args.get('download')
#   order_by = request.args.get('order_by')
#   order = request.args.get('order')
#   view = request.args.get('view')
#   per_page = 15
#
#   base_query = Omni_NLP.query
#   if view == 'secondary':
#     base_query = base_query.filter(Omni_NLP.dbid_1 != 'D008193').filter(Omni_NLP.secondary_score_chi > 0)
#   else :
#     base_query = base_query.filter(Omni_NLP.dbid_1 == 'D008193').filter(Omni_NLP.secondary_score_chi == 0)
#
#   if secondary and secondary.lower() in ['chemical', 'gene', 'disease'] :
#     base_query = base_query.filter(Omni_NLP.term_2_type==secondary)
#   elif secondary and secondary.lower() in ['lyme'] :
#     base_query = base_query.filter(Omni_NLP.dbid_2=='D008193')
#
#
#   if search_primary :
#     base_query = base_query.filter(Omni_NLP.term_1.like('%' + search_primary + '%') | \
#                                    Omni_NLP.dbid_1.like('%' + search_primary + '%'))
#
#   if search_secondary :
#     base_query = base_query.filter(Omni_NLP.term_2.like('%' + search_secondary + '%') | \
#                                    Omni_NLP.dbid_2.like('%' + search_secondary + '%'))
#
#   if order_by and order:
#     if order_by in ['adjpvalue','secondary_score_chi','secondary_score_jaccard']:
#       if order == 'asc' :
#         base_query = base_query.order_by(text('-' + order_by + ' desc'))
#       elif order == 'desc':
#         base_query = base_query.order_by(text(order_by + ' desc'))
#     else:
#       if order == 'asc':
#         base_query = base_query.order_by(text('isnull(' + order_by + '), ' + order_by + ' asc'))
#       elif order == 'desc' :
#         base_query = base_query.order_by(text('isnull(' + order_by + '), ' + order_by + ' desc'))
#   else :
#     base_query = base_query.order_by(text('-adjpvalue desc'))
#
#   omni_nlp = base_query
#
# ## Data export
#   if download == 'csv' :
#     si = StringIO()
#     cw = csv.writer(si)
#     output_omni_nlp = []
#     output_omni_nlp.append(['Lyme NLP ID','Term 1','Term 1 Type','DBID 1', 'DBID 1 Type', 'Term 2',
#                      'Term 2 Type','DBID 2','DBID 2 Type','Relationship','Adjusted P Value',
#                      'Secondary Score - Chi', 'PMID List Link'])
#     for on in omni_nlp :
#       output_omni_nlp.append([on.table_id, on.term_1, on.term_1_type, on.dbid_1, on.dbid_1_type,
#                               on.term_2, on.term_2_type, on.dbid_2, on.dbid_2_type, on.relation,
#                               on.adjpvalue, on.secondary_score_chi, 'http://ec2-54-163-140-249.compute-1.amazonaws.com:5000/pmids/' + str(on.id1) + "/" + str(on.id2)])
#     cw.writerows(output_omni_nlp)
#     output = make_response(si.getvalue())
#     filename = "lyme_omni_nlp_" + str(datetime.now()).replace("-", "")[0:8] + ".csv"
#     output.headers["Content-Disposition"] = "attachment; filename=" + filename
#     output.headers["Content-type"] = "text/csv"
#     return output
# ## end Data export
#
#   omni_nlp = omni_nlp.paginate(page, per_page, False)
#   omni_nlp_items = omni_nlp.items
#   pages = omni_nlp.pages
#
#   prev = 1
#   if page != 1 :
#     prev = page - 1
#
#   next = page
#   if page !=  pages:
#     next = page + 1
#
#   page_display = page_range(page, pages, span=10)
#
#   # records showing on page
#   max_records = per_page * page
#   if max_records > omni_nlp.total:
#     max_records = omni_nlp.total
#
#   showing = [per_page * page - per_page + 1, max_records]
#
#   meta = {
#     "total" : omni_nlp.total,
#     "pages" : pages,
#     "page_display" : page_display,
#     "page" : omni_nlp.page,
#     "next" : next,
#     "prev" : prev,
#     "has_next" : omni_nlp.has_next,
#     "order_by" : order_by,
#     "showing" : showing
#   }
#
#   return render_template('index.html', omni_nlp=omni_nlp_items, meta=meta)
#
# ###############################################
# ###  NLP OMNI PMID LIST
# ###############################################
# @app.route('/pmids/<int:id1>/<int:id2>', strict_slashes=False)
# def get_pmids(id1,id2):
#   download = request.args.get('download')
#   terms = request.args.get('terms')
#
#   sql = """select pmid.journal, pmid.title, pmid.submission_date, pmid.impact_factor,
#     ipm1.pmid as pmid, ipm1.term_id as id1, ipm2.term_id as id2, (ipm1.tf_idf+ipm2.tf_idf) as relevance_score from
#     lyme.lyme_omni_nlp_id_to_pmid_map ipm1
#     inner join lyme.lyme_omni_nlp_id_to_pmid_map ipm2 on ipm1.pmid = ipm2.pmid
#     inner join lyme.lyme_omni_nlp_pmid_data pmid on pmid.pmid = ipm1.pmid
#     where ipm1.term_id = %d and ipm2.term_id = %d
#     ;""" % (id1, id2)
#
#   data = db.engine.execute(sql)
#
#   try:
#     terms = terms.split(',')
#     term_1 = terms[0]
#     term_2 = terms[1]
#     display = {'term_1': term_2, 'term_2': term_1, 'id1' : id1, 'id2' : id2}
#   except:
#     display = {'term_1': '', 'term_2': '', 'id1' : id1, 'id2' : id2}
#     term_1 = 'No term provided'
#     term_2 = 'No term provided'
#   print term_1, term_2
#
#   if download == 'csv' :
#     si = StringIO()
#     cw = csv.writer(si)
#     output_journal = []
#     output_journal.append(['Term 1', 'Term 2', 'Journal Name', 'Title', 'Submission Date', 'Impact Factor', 'Relevance Score', 'Pubmed Link'])
#     for d in data :
#       clean_record = []
#       record = [term_1, term_2, d.journal, d.title, d.submission_date, d.impact_factor, d.relevance_score, 'http://www.ncbi.nlm.nih.gov/pubmed/%s' % (d.pmid)]
#       record = [x.encode('ascii').strip() for x in record if type(x) is str]
#
#       output_journal.append([term_1, term_2, d.journal, d.title, d.submission_date, d.impact_factor, d.relevance_score, 'http://www.ncbi.nlm.nih.gov/pubmed/%s' % (d.pmid)])
#     cw.writerows(output_journal)
#     output = make_response(si.getvalue())
#     filename = "lyme_omni_nlp_journal_" + str(id1) + "_" + str(id2) + "_" + str(datetime.now()).replace("-", "")[0:8] + ".csv"
#     output.headers["Content-Disposition"] = "attachment; filename=" + filename
#     output.headers["Content-type"] = "text/csv"
#     return output
#
#   return render_template('detail.html', data=data, display=display)
#
#
# @app.route('/feedback', strict_slashes=False)
# def get_feedback():
#   return render_template('feedback.html')
