import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { NgbCarouselModule, NgbAlertModule } from '@ng-bootstrap/ng-bootstrap';

import { IterationRoutingModule } from './iteration-routing.module';
import { IterationComponent } from './iteration.component';
import {
    MutationDetailsComponent 

} from './components';
import { StatModule } from '../../shared';

@NgModule({
    imports: [
        CommonModule,
        NgbCarouselModule.forRoot(),
        NgbAlertModule.forRoot(),
        IterationRoutingModule,
        StatModule
    ],
    declarations: [
        IterationComponent,
        MutationDetailsComponent
    ]
})
export class IterationdModule {}
