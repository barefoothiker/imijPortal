import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { IterationComponent } from './iteration.component';

describe('DashboardComponent', () => {
  let component: IterationComponent;
  let fixture: ComponentFixture<IterationComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ IterationComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(IterationComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
