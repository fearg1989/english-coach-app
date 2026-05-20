import { TestBed } from '@angular/core/testing';
import { provideHttpClient } from '@angular/common/http';
import {
  HttpTestingController,
  provideHttpClientTesting,
} from '@angular/common/http/testing';

import { LevelService } from './level.service';
import { Level } from '../models/level.model';

const MOCK_LEVELS: Level[] = [
  {
    id: 1,
    code: 'A1',
    name: 'Beginner',
    description: 'Basic phrases.',
    order_index: 1,
    created_at: '2026-01-01T00:00:00',
    updated_at: '2026-01-01T00:00:00',
  },
  {
    id: 2,
    code: 'B1',
    name: 'Intermediate',
    description: 'Travel situations.',
    order_index: 3,
    created_at: '2026-01-01T00:00:00',
    updated_at: '2026-01-01T00:00:00',
  },
];

describe('LevelService', () => {
  let service: LevelService;
  let httpMock: HttpTestingController;

  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [LevelService, provideHttpClient(), provideHttpClientTesting()],
    });
    service = TestBed.inject(LevelService);
    httpMock = TestBed.inject(HttpTestingController);
  });

  afterEach(() => httpMock.verify());

  it('should be created', () => {
    expect(service).toBeTruthy();
  });

  // ── getLevels() ────────────────────────────────────────────────────────────

  describe('getLevels()', () => {
    it('should perform GET to /levels/', () => {
      service.getLevels().subscribe();
      const req = httpMock.expectOne((r) => r.url.includes('/levels/'));
      expect(req.request.method).toBe('GET');
      req.flush(MOCK_LEVELS);
    });

    it('should return an array of Level objects', (done) => {
      service.getLevels().subscribe((levels) => {
        expect(levels).toEqual(MOCK_LEVELS);
        expect(levels.length).toBe(2);
        done();
      });
      httpMock.expectOne((r) => r.url.includes('/levels/')).flush(MOCK_LEVELS);
    });

    it('should return an empty array when API responds with []', (done) => {
      service.getLevels().subscribe((levels) => {
        expect(levels).toEqual([]);
        done();
      });
      httpMock.expectOne((r) => r.url.includes('/levels/')).flush([]);
    });

    it('should map the code field correctly', (done) => {
      service.getLevels().subscribe((levels) => {
        expect(levels[0].code).toBe('A1');
        expect(levels[1].code).toBe('B1');
        done();
      });
      httpMock.expectOne((r) => r.url.includes('/levels/')).flush(MOCK_LEVELS);
    });
  });

  // ── getLevel(id) ───────────────────────────────────────────────────────────

  describe('getLevel(id)', () => {
    it('should perform GET to /levels/:id', () => {
      service.getLevel(1).subscribe();
      const req = httpMock.expectOne((r) => r.url.endsWith('/levels/1'));
      expect(req.request.method).toBe('GET');
      req.flush(MOCK_LEVELS[0]);
    });

    it('should return the correct Level object', (done) => {
      service.getLevel(1).subscribe((level) => {
        expect(level.id).toBe(1);
        expect(level.code).toBe('A1');
        expect(level.name).toBe('Beginner');
        done();
      });
      httpMock.expectOne((r) => r.url.endsWith('/levels/1')).flush(MOCK_LEVELS[0]);
    });

    it('should use the provided id in the URL', () => {
      service.getLevel(42).subscribe();
      const req = httpMock.expectOne((r) => r.url.endsWith('/levels/42'));
      expect(req).toBeTruthy();
      req.flush(MOCK_LEVELS[0]);
    });
  });
});
