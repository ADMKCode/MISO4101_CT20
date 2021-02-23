import { Component, OnInit, Input } from '@angular/core';
import { Deportista } from '../deportista';
import { ActivatedRoute } from '@angular/router';
import { Location } from '@angular/common';

import {DeportistaService} from '../deportista.service';


@Component({
  selector: 'app-deportistas-detail',
  templateUrl: './deportistas-detail.component.html',
  styleUrls: ['./deportistas-detail.component.css']
})
export class DeportistasDetailComponent implements OnInit {

  @Input() deportista: Deportista;

  constructor(
    private route: ActivatedRoute,
  private deportistaService: DeportistaService,
  private location: Location

  ) { }

  ngOnInit(): void {
    this.getDeportista();
  }

  getDeportista(): void {
    const id = +this.route.snapshot.paramMap.get('id');
    this.deportistaService.getDeportista(id)
      .subscribe(deportista => this.deportista = deportista);
  }

  goBack(): void {
    this.location.back();
 }
 
  
}
