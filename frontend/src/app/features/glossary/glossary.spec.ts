import { ComponentFixture, TestBed } from '@angular/core/testing';
import { provideRouter } from '@angular/router';
import { of, throwError } from 'rxjs';

import { GlossaryComponent } from './glossary';
import { GlossaryService } from '../../core/services/glossary.service';
import { GlossaryEntry } from '../../core/models/glossary.model';

const MOCK_PHRASAL: GlossaryEntry = {
  id: 1,
  type: 'phrasal_verb',
  term: 'spin up',
  meaning: 'Inicializar / levantar un servicio',
  form_past: null,
  form_participle: null,
  order_index: 1,
  created_at: '2026-01-01T00:00:00',
  updated_at: '2026-01-01T00:00:00',
};

const MOCK_IRREGULAR: GlossaryEntry = {
  id: 2,
  type: 'irregular_verb',
  term: 'go',
  meaning: 'ir',
  form_past: 'went',
  form_participle: 'gone',
  order_index: 24,
  created_at: '2026-01-01T00:00:00',
  updated_at: '2026-01-01T00:00:00',
};

describe('GlossaryComponent', () => {
  let fixture: ComponentFixture<GlossaryComponent>;
  let component: GlossaryComponent;
  let glossaryServiceSpy: jasmine.SpyObj<GlossaryService>;

  beforeEach(async () => {
    glossaryServiceSpy = jasmine.createSpyObj<GlossaryService>('GlossaryService', [
      'getEntries',
    ]);
    glossaryServiceSpy.getEntries.and.callFake((type) =>
      type === 'phrasal_verb' ? of([MOCK_PHRASAL]) : of([MOCK_IRREGULAR])
    );

    await TestBed.configureTestingModule({
      imports: [GlossaryComponent],
      providers: [
        provideRouter([]),
        { provide: GlossaryService, useValue: glossaryServiceSpy },
      ],
    }).compileComponents();

    fixture = TestBed.createComponent(GlossaryComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });

  it('should load both types on init', () => {
    expect(glossaryServiceSpy.getEntries).toHaveBeenCalledWith('phrasal_verb');
    expect(glossaryServiceSpy.getEntries).toHaveBeenCalledWith('irregular_verb');
  });

  it('should default to phrasal_verb tab', () => {
    expect(component.activeTab()).toBe('phrasal_verb');
  });

  it('should render phrasal verb pill with term', () => {
    const pill = fixture.nativeElement.querySelector('.phrasal-pill__term');
    expect(pill?.textContent?.trim()).toBe('spin up');
  });

  it('should render phrasal verb meaning', () => {
    const meaning = fixture.nativeElement.querySelector('.phrasal-pill__meaning');
    expect(meaning?.textContent).toContain('Inicializar');
  });

  it('setTab should switch to irregular_verb tab', () => {
    component.setTab('irregular_verb');
    fixture.detectChanges();
    expect(component.activeTab()).toBe('irregular_verb');
  });

  it('should render irregular verb table when tab is irregular_verb', () => {
    component.setTab('irregular_verb');
    fixture.detectChanges();
    const table = fixture.nativeElement.querySelector('.irregular-table');
    expect(table).toBeTruthy();
  });

  it('should render base form cell for irregular verb', () => {
    component.setTab('irregular_verb');
    fixture.detectChanges();
    const baseCell = fixture.nativeElement.querySelector('.irregular-table__base');
    expect(baseCell?.textContent?.trim()).toBe('go');
  });

  it('should show error message on phrasal verb fetch failure', async () => {
    glossaryServiceSpy.getEntries.and.callFake((type) =>
      type === 'phrasal_verb' ? throwError(() => new Error('Network error')) : of([MOCK_IRREGULAR])
    );
    fixture = TestBed.createComponent(GlossaryComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
    await fixture.whenStable();
    fixture.detectChanges();
    expect(component.error()).not.toBeNull();
  });
});
