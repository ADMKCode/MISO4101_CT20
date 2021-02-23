import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { DeportistasComponent} from './deportistas/deportistas.component'
import {DeportistasDetailComponent} from './deportistas-detail/deportistas-detail.component'

const routes: Routes = [
  { path: 'deportistas', component: DeportistasComponent},
  { path: 'deportistas/:id', component: DeportistasDetailComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
