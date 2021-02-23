import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule } from '@angular/forms';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { DeportistasComponent } from './deportistas/deportistas.component';
import { DeportistasDetailComponent } from './deportistas-detail/deportistas-detail.component';

@NgModule({
  declarations: [
    AppComponent,
    DeportistasComponent,
    DeportistasDetailComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
