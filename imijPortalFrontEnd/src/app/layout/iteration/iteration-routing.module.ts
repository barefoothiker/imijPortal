import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { IterationComponent } from './iteration.component';
import { MutationDetailsComponent } from './components/mutation-details/mutation-details.component';

const routes: Routes = [
    {
        path: '',
        component: IterationComponent,

//        children: [
//        { path: '/getIterationDetails', component: MutationDetailsComponent}
//        ]
       children: [
                  {path: 'getIterationDetails', component: MutationDetailsComponent},
                  ]
    }

];


@NgModule({
    imports: [RouterModule.forChild(routes)],
    exports: [RouterModule]
})
export class IterationRoutingModule {
}
