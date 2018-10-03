from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from daphniFrontendPatientDB.views import *

admin.autodiscover()

urlpatterns = [

    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', landing, name = 'landing'),

    url(r'^daphniFrontendPatientDB/$', landing, name = 'landing'),

    url(r'^daphniFrontendPatientDB/processLanding/$', processLanding, name = 'processLanding'),
    
    url(r'^daphniFrontendPatientDB/listPatients/', listPatients, name = 'listPatients'),
    url(r'^daphniFrontendPatientDB/getMutations/', getMutations, name = 'getMutations'),
    url(r'^daphniFrontendPatientDB/listMutationDetails/', listMutationDetails, name = 'listMutationDetails'),

    
#     url(r'^daphniFrontendPatientDB/listProjects/$', listProjects, name = 'listProjects'),
#     url(r'^daphniFrontendPatientDB/listProjectPatients/', listProjectPatients, name = 'listProjectPatients'),
    url(r'^daphniFrontendPatientDB/listPatientIterations/', listPatientIterations, name = 'listPatientIterations'),
    url(r'^daphniFrontendPatientDB/patientIterationDetails/', patientIterationDetails, name = 'patientIterationDetails'),
    url(r'^daphniFrontendPatientDB/comparePatientIterations/', comparePatientIterations, name = 'comparePatientIterations'),
    
    url(r'^daphniFrontendPatientDB/register/', register, name = 'register'),
    url(r'^accounts/', include('registration.urls'))

]

urlpatterns += staticfiles_urlpatterns()

#print str(urlpatterns)
