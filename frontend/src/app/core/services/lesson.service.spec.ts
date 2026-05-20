import { TestBed } from '@angular/core/testing';
import { provideHttpClient } from '@angular/common/http';
import {
  HttpTestingController,
  provideHttpClientTesting,
} from '@angular/common/http/testing';

import { LessonService } from './lesson.service';
import { Lesson, LessonDetail } from '../models/lesson.model';

const MOCK_LESSON: Lesson = {
  id: 1,
  level_id: 1,
  title: 'The /θ/ Sound',
  type: 'phonetics',
  category: 'verb_tenses',
  description: 'Voiceless TH.',
  order_index: 1,
  is_published: true,
  created_at: '2026-01-01T00:00:00',
  updated_at: '2026-01-01T00:00:00',
};

const MOCK_LESSON_DETAIL: LessonDetail = {
  ...MOCK_LESSON,
  examples: [
    {
      id: 1,
      lesson_id: 1,
      phrase: 'Think about it.',
      translation: 'Piénsalo.',
      ipa_notation: '/θɪŋk əˈbaʊt ɪt/',
      audio_url: null,
      order_index: 1,
      created_at: '2026-01-01T00:00:00',
      updated_at: '2026-01-01T00:00:00',
    },
  ],
  exercises: [
    {
      id: 1,
      lesson_id: 1,
      type: 'multiple_choice',
      question: 'Which word has the /θ/ sound?',
      correct_answer: 'tooth',
      options: { a: 'this', b: 'tooth' },
      order_index: 1,
      created_at: '2026-01-01T00:00:00',
      updated_at: '2026-01-01T00:00:00',
    },
  ],
};

describe('LessonService', () => {
  let service: LessonService;
  let httpMock: HttpTestingController;

  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [LessonService, provideHttpClient(), provideHttpClientTesting()],
    });
    service = TestBed.inject(LessonService);
    httpMock = TestBed.inject(HttpTestingController);
  });

  afterEach(() => httpMock.verify());

  it('should be created', () => {
    expect(service).toBeTruthy();
  });

  // ── getLessonsByLevel(levelId) ─────────────────────────────────────────────

  describe('getLessonsByLevel(levelId)', () => {
    it('should perform GET to /lessons/level/:id', () => {
      service.getLessonsByLevel(1).subscribe();
      const req = httpMock.expectOne((r) => r.url.includes('/lessons/level/1'));
      expect(req.request.method).toBe('GET');
      req.flush([MOCK_LESSON]);
    });

    it('should return a list of Lesson objects', (done) => {
      service.getLessonsByLevel(1).subscribe((lessons) => {
        expect(lessons.length).toBe(1);
        expect(lessons[0].type).toBe('phonetics');
        done();
      });
      httpMock.expectOne((r) => r.url.includes('/lessons/level/1')).flush([MOCK_LESSON]);
    });

    it('should return an empty array when there are no lessons', (done) => {
      service.getLessonsByLevel(99).subscribe((lessons) => {
        expect(lessons).toEqual([]);
        done();
      });
      httpMock.expectOne((r) => r.url.includes('/lessons/level/99')).flush([]);
    });
  });

  // ── getLessonsByType(levelId, type) ────────────────────────────────────────

  describe('getLessonsByType(levelId, type)', () => {
    it('should include the type query param in the request', () => {
      service.getLessonsByType(1, 'grammar').subscribe();
      const req = httpMock.expectOne(
        (r) => r.url.includes('/lessons/level/1') && r.params.get('type') === 'grammar',
      );
      expect(req.request.method).toBe('GET');
      req.flush([]);
    });

    it('should send type=phonetics when filtering by phonetics', () => {
      service.getLessonsByType(1, 'phonetics').subscribe();
      const req = httpMock.expectOne(
        (r) => r.url.includes('/lessons/level/1') && r.params.get('type') === 'phonetics',
      );
      expect(req).toBeTruthy();
      req.flush([MOCK_LESSON]);
    });
  });

  // ── getLessonsByCategory(category) ─────────────────────────────────────────

  describe('getLessonsByCategory(category)', () => {
    it('should perform GET to /lessons/category/:category', () => {
      service.getLessonsByCategory('irregular_verbs').subscribe();
      const req = httpMock.expectOne((r) => r.url.includes('/lessons/category/irregular_verbs'));
      expect(req.request.method).toBe('GET');
      req.flush([MOCK_LESSON]);
    });

    it('should return a list of lesson objects for the requested category', (done) => {
      service.getLessonsByCategory('irregular_verbs').subscribe((lessons) => {
        expect(lessons.length).toBe(1);
        expect(lessons[0].category).toBe('verb_tenses');
        done();
      });
      httpMock.expectOne((r) => r.url.includes('/lessons/category/irregular_verbs')).flush([MOCK_LESSON]);
    });
  });

  // ── getLesson(id) ──────────────────────────────────────────────────────────

  describe('getLesson(id)', () => {
    it('should perform GET to /lessons/:id', () => {
      service.getLesson(1).subscribe();
      const req = httpMock.expectOne((r) => r.url.endsWith('/lessons/1'));
      expect(req.request.method).toBe('GET');
      req.flush(MOCK_LESSON_DETAIL);
    });

    it('should return LessonDetail with examples array', (done) => {
      service.getLesson(1).subscribe((detail) => {
        expect(detail.examples.length).toBe(1);
        expect(detail.examples[0].ipa_notation).toBe('/θɪŋk əˈbaʊt ɪt/');
        done();
      });
      httpMock.expectOne((r) => r.url.endsWith('/lessons/1')).flush(MOCK_LESSON_DETAIL);
    });

    it('should return LessonDetail with exercises array', (done) => {
      service.getLesson(1).subscribe((detail) => {
        expect(detail.exercises.length).toBe(1);
        expect(detail.exercises[0].correct_answer).toBe('tooth');
        done();
      });
      httpMock.expectOne((r) => r.url.endsWith('/lessons/1')).flush(MOCK_LESSON_DETAIL);
    });

    it('should map audio_url as null (Phase 2 placeholder)', (done) => {
      service.getLesson(1).subscribe((detail) => {
        expect(detail.examples[0].audio_url).toBeNull();
        done();
      });
      httpMock.expectOne((r) => r.url.endsWith('/lessons/1')).flush(MOCK_LESSON_DETAIL);
    });
  });
});
