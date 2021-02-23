import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DeportistasDetailComponent } from './deportistas-detail.component';

describe('DeportistasDetailComponent', () => {
  let component: DeportistasDetailComponent;
  let fixture: ComponentFixture<DeportistasDetailComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ DeportistasDetailComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(DeportistasDetailComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
