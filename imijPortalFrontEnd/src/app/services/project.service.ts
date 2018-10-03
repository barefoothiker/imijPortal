import { Injectable } from '@angular/core';
import { Http,RequestOptions, Headers, URLSearchParams, QueryEncoder,Response } from '@angular/http';
import 'rxjs/add/operator/toPromise';

import { Observable } from 'rxjs/Observable';
import { Patient} from './../models/patient';

import { MutationDetails} from './../models/MutationDetails';



@Injectable()
export class ProjectService {
  BASE_URL='http://localhost:8000';
  private headers = new Headers({ 'Content-Type': 'application/json' });
  private uploadFilesUrl = this.BASE_URL+'/imijportalapp/listPatients/';
  private listFilesUrl = this.BASE_URL+'/imijportalapp/sampleDetails/';
  private mutationsUrl = this.BASE_URL+'/imijportalapp/mutationDetails/';

  public patients: Patient[];

  public  constructor(private http: Http) { }


//  get projects directories (TFS user story id usid) from folder structure
   getPatients(): Promise<Patient[]> {
    return this.http.get(this.patientsUrl)
      .toPromise()
      .then(response => response.json() as Patient[])
      .catch(this.handleError);
  }

//   getMutations(mutId:any): Promise<MutationDetails[]> {
//       return this.http.get(this.mutationsUrl + '?mutId=' +mutId)
//       .toPromise()
//       .then(response => response.json() as Patient[])
//       .catch(this.handleError);
//   }

   getMutations(mutId: any): Promise<MutationDetails[]> {

       let searchParams = new URLSearchParams()

       searchParams.set('mutId', mutId);

       let requestOptions = new RequestOptions();
       requestOptions.search = searchParams;
       return this.http.post(this.mutationsUrl, requestOptions)
       .toPromise()
       .then(response => response.json() as MutationDetails[])
       .catch(this.handleError);
     }



  private handleError(error: any): Promise<any> {
    console.error('An error occurred', error); // for demo purposes only
    return Promise.reject(error.message || error);
  }

  listMutationDetails(variantClass: any): Promise<MutationDetails[]> {

      let searchParams = new URLSearchParams()

      searchParams.set('variantClass', variantClass);

      let requestOptions = new RequestOptions();
      requestOptions.search = searchParams;
      return this.http.post(this.mutationDetailsUrl, requestOptions)
      .toPromise()
      .then(response => response.json() as MutationDetails[])
      .catch(this.handleError);
    }
}
