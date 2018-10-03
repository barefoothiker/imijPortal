import { Component, OnInit } from '@angular/core';
import { routerTransition } from '../../router.animations';

@Component({
    selector: 'app-iteration',
    templateUrl: './iteration.component.html',
    styleUrls: ['./iteration.component.scss'],
    animations: [routerTransition()]
})
export class IterationComponent implements OnInit {


    constructor() {



    }

    ngOnInit() {}
}
