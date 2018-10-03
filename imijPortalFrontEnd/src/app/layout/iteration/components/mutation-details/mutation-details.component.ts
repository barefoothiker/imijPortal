import { Router } from '@angular/router';


import { MutationDetails } from '../../../../models/MutationDetails';
import { Iteration } from '../../../../models/iteration';
import { ProjectService } from '../../../../services/project.service';


import { Component, Input, OnInit } from '@angular/core';
import { ActivatedRoute, Params } from '@angular/router';
import { Location } from '@angular/common';
import 'rxjs/add/operator/switchMap';


@Component({
  selector: 'app-mutationDetails',
  templateUrl: './mutation-details.component.html',
  styleUrls: ['./mutation-details.component.css'],
  providers: [ProjectService]
})



export class MutationDetailsComponent implements OnInit {
  @Input()
  mutationDetails: MutationDetails[];
  variantClass: string;
  
  constructor(
    private projectService: ProjectService,
    private route: ActivatedRoute,
    private location: Location
  ) { }

  ngOnInit() {
  }
  
  getIterationDetails(){
      debugger; 
      this.route.params.switchMap((params: Params) =>
      this.projectService.listMutationDetails(+params['variantClass'])).subscribe(mutationDetails => this.mutationDetails = mutationDetails);
      
  }

}
