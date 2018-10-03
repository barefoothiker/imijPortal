from django.db import models
from django.contrib.auth.models import User


class Patient(models.Model):
    daphniId = models.IntegerField(unique=True)
    userStoryId = models.IntegerField(unique=True)
    def __str__(self):
         return str(self.daphniId)+"_"+str(self.userStoryId)

class Sample(models.Model):
    dateCreated = models.DateTimeField( blank = True, null = True)
    name = models.CharField(max_length=255, blank = True, null = True)
    iteration = models.IntegerField()
    patient = models.ForeignKey(Patient)
    def __str__(self):
        return str(self.iteration)

class FlowTool(models.Model):
    name = models.CharField(max_length=512)
    version = models.CharField(max_length=512)
    source = models.CharField(max_length=512, blank = True, null = True)
    def __str__(self):
        return str(self.name)+"_"+str(self.version)
    
class FlowOutcome(models.Model):
    outputFileName= models.CharField(max_length=512, blank = True, null = True)
    commandFlowId = models.IntegerField(blank = True, null = True)
    dateCreated = models.DateTimeField(blank = True, null = True)
    flowName= models.CharField(max_length=512, blank = True, null = True)
    isActive=models.NullBooleanField(blank = True, null = True)
                                                                                                           
    sample = models.ForeignKey(Sample)
    flowTool = models.ForeignKey(FlowTool)
    def __str__(self):
        return str(self.flowName)+"_"+str(self.dateCreated)





class Gene(models.Model):
    sChromosome= models.CharField(max_length=512)
    sHugo_Symbol = models.CharField(unique=True, max_length=255)
    sEntrez_Gene_Id = models.CharField(max_length=255, blank = True, null = True)
    sEnsembleID = models.CharField(max_length=255, blank = True, null = True)
    def __str__(self):
        return str(self.sHugo_Symbol)

class MutationDetails(models.Model):
    sStart_position    =    models.CharField(max_length=512, blank = True, null = True)
    sEnd_position    =    models.CharField(max_length=512, blank = True, null = True)
    sReference_Allele    =    models.CharField(max_length=512, blank = True, null = True)
    sTumor_Seq_Allele2    =    models.CharField(max_length=512, blank = True, null = True)
    stotal_reads    =    models.CharField(max_length=512, blank = True, null = True)
    stumor_f    =    models.CharField(max_length=512, blank = True, null = True)
    sdbSNP_RS    =    models.CharField(max_length=512, blank = True, null = True)
    sVariant_Classification    =    models.CharField(max_length=512, blank = True, null = True)
    sVariant_Type    =    models.CharField(max_length=512, blank = True, null = True)
    sGenome_Change    =    models.CharField(max_length=512, blank = True, null = True)
    scDNA_Change    =    models.CharField(max_length=512, blank = True, null = True)
    sCodon_Change    =    models.CharField(max_length=512, blank = True, null = True)
    sProtein_Change    =    models.CharField(max_length=512, blank = True, null = True)
    sdbNSFP_LR_score    =    models.CharField(max_length=512, blank = True, null = True)
    sCOSMIC_overlapping_mutations    =    models.CharField(max_length=512, blank = True, null = True)
    sCOSMIC_tissue_types_affected    =    models.CharField(max_length=512, blank = True, null = True)
    sCOSMIC_total_alterations_in_gene    =    models.CharField(max_length=512, blank = True, null = True)
    sCOSMIC_n_overlapping_mutations    =    models.CharField(max_length=512, blank = True, null = True)
    sCOSMIC_overlapping_mutation_descriptions    =    models.CharField(max_length=512, blank = True, null = True)
    sCOSMIC_overlapping_primary_sites    =    models.CharField(max_length=512, blank = True, null = True)
    sClinVar_SYM    =    models.CharField(max_length=512, blank = True, null = True)
    sClinVar_TYPE    =    models.CharField(max_length=512, blank = True, null = True)
    sClinVar_rs    =    models.CharField(max_length=512, blank = True, null = True)
    sdbNSFP_LR_pred    =    models.CharField(max_length=512, blank = True, null = True)
    
    rnaExpression = models.NullBooleanField(blank = True, null = True) #Gene expressed in RNA yes/no/null
    cloneID = models.IntegerField(blank = True)
    
    
    flowOutcome = models.ForeignKey(FlowOutcome)
    gene = models.ForeignKey(Gene)
    def __str__(self):
        return str(self.sVariant_Type)

