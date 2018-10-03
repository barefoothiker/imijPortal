import { Component, Input, OnInit } from '@angular/core';
import { ActivatedRoute, Params } from '@angular/router';
import { Location } from '@angular/common';
import 'rxjs/add/operator/switchMap';

import { ProjectService } from '../../../../services/project.service';
import { Patient } from '../../../../models/patient';

@Component({
  selector: 'app-timeline',
  templateUrl: './timeline.component.html',
  styleUrls: ['./timeline.component.scss']
})
export class TimelineComponent implements OnInit {

    @Input()
    patients: Patient[];
    constructor(
      private projectService: ProjectService,
      private route: ActivatedRoute,
      private location: Location
    ) { }

        ngOnInit() {
            this.projectService.getPatients().then(patients => this.patients = patients);
        
        }
}
