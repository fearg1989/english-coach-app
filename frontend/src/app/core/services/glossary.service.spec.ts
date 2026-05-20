import { TestBed } from '@angular/core/testing';
import { provideHttpClient } from '@angular/common/http';
import {
  HttpTestingController,
  provideHttpClientTesting,
} from '@angular/common/http/testing';

import { GlossaryService } from './glossary.service';
import { GlossaryEntry } from '../models/glossary.model';

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

describe('GlossaryService', () => {
  let service: GlossaryService;
  let httpMock: HttpTestingController;

  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [GlossaryService, provideHttpClient(), provideHttpClientTesting()],
    });
    service = TestBed.inject(GlossaryService);
    httpMock = TestBed.inject(HttpTestingController);
  });

  afterEach(() => httpMock.verify());

  it('should be created', () => {
    expect(service).toBeTruthy();
  });

  // ── getEntries('phrasal_verb') ─────────────────────────────────────────────

  describe("getEntries('phrasal_verb')", () => {
    it('should perform GET to /glossary/ with type=phrasal_verb', () => {
      service.getEntries('phrasal_verb').subscribe();
      const req = httpMock.expectOne((r) =>
        r.url.includes('/glossary/') && r.params.get('type') === 'phrasal_verb'
      );
      expect(req.request.method).toBe('GET');
      req.flush([MOCK_PHRASAL]);
    });

    it('should return the list emitted by the API', (done) => {
      service.getEntries('phrasal_verb').subscribe((entries) => {
        expect(entries.length).toBe(1);
        expect(entries[0].term).toBe('spin up');
        done();
      });
      const req = httpMock.expectOne((r) => r.url.includes('/glossary/'));
      req.flush([MOCK_PHRASAL]);
    });
  });

  // ── getEntries('irregular_verb') ──────────────────────────────────────────

  describe("getEntries('irregular_verb')", () => {
    it('should perform GET to /glossary/ with type=irregular_verb', () => {
      service.getEntries('irregular_verb').subscribe();
      const req = httpMock.expectOne((r) =>
        r.url.includes('/glossary/') && r.params.get('type') === 'irregular_verb'
      );
      expect(req.request.method).toBe('GET');
      req.flush([MOCK_IRREGULAR]);
    });

    it('irregular entry should include form_past and form_participle', (done) => {
      service.getEntries('irregular_verb').subscribe((entries) => {
        expect(entries[0].form_past).toBe('went');
        expect(entries[0].form_participle).toBe('gone');
        done();
      });
      const req = httpMock.expectOne((r) => r.url.includes('/glossary/'));
      req.flush([MOCK_IRREGULAR]);
    });
  });
});
