import { Sample } from './../models/sample';
import { Gene } from './../models/gene';

export class MutationDetails {
    id: number;

    tumorFreq : number;
    normalFreq : number;
    rnaExpression : string; //models.NullBooleanField(blank True, null True) #Gene expressed in RNA yes/no/null
    cloneID  : number;
    start   : number;
    stop   : number;
    chromosome    : string
    oncotatorFile  : string;
    variantClass  : string;
    impact  : string;
    cDNAChange  : string;
    proteinChange  : string;
//#     applicationTools models.ManyToManyField(ApplicationTools, blank True, null True)
    sample : Sample;
    gene : Gene;
}
