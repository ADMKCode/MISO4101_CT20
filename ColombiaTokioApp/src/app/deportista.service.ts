import { Injectable } from '@angular/core';
import { Deportista } from './deportista';
import { DEPORTISTAS } from './mock-deportistas';
import { Observable, of } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class DeportistaService {

  constructor() { }

  getDeportistas(): Observable<Deportista[]>{
    return of(DEPORTISTAS);
  }

  getDeportista(id: number): Observable<Deportista> {
    return of(DEPORTISTAS.find(deportista => deportista.id === id));  	
  }
  
}
