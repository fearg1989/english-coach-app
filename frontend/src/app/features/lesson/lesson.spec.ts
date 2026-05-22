import { ComponentFixture, TestBed } from '@angular/core/testing';
import { ActivatedRoute } from '@angular/router';
import { provideRouter } from '@angular/router';
import { of, throwError } from 'rxjs';

import { LessonComponent } from './lesson';
import { LessonService } from '../../core/services/lesson.service';
import { LessonDetail } from '../../core/models/lesson.model';

const MOCK_DETAIL: LessonDetail = {
  id: 1,
  level_id: 1,
  title: 'The /θ/ Sound',
  type: 'phonetics',
  category: 'verb_tenses',
  description: "Voiceless TH sound.",
  explanation: null,
  order_index: 1,
  is_published: true,
  created_at: '2026-01-01T00:00:00',
  updated_at: '2026-01-01T00:00:00',
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
  exercises: [],
};

describe('LessonComponent', () => {
  let fixture: ComponentFixture<LessonComponent>;
  let component: LessonComponent;
  let lessonServiceSpy: jasmine.SpyObj<LessonService>;

  beforeEach(async () => {
    lessonServiceSpy = jasmine.createSpyObj<LessonService>('LessonService', [
      'getLesson',
    ]);

    await TestBed.configureTestingModule({
      imports: [LessonComponent],
      providers: [
        provideRouter([]),
        { provide: LessonService, useValue: lessonServiceSpy },
        {
          provide: ActivatedRoute,
          useValue: {
            snapshot: {
              paramMap: { get: () => '1' },
              queryParamMap: { get: () => null },
            },
          },
        },
      ],
    }).compileComponents();

    fixture = TestBed.createComponent(LessonComponent);
    component = fixture.componentInstance;
  });

  // ── Component lifecycle ───────────────────────────────────────────────────

  it('should create the component', () => {
    lessonServiceSpy.getLesson.and.returnValue(of(MOCK_DETAIL));
    fixture.detectChanges();
    expect(component).toBeTruthy();
  });

  it('should call getLesson with the numeric ID from the route param', () => {
    lessonServiceSpy.getLesson.and.returnValue(of(MOCK_DETAIL));
    fixture.detectChanges();
    expect(lessonServiceSpy.getLesson).toHaveBeenCalledOnceWith(1);
  });

  // ── Signal state — happy path ─────────────────────────────────────────────

  it('should set lesson() signal with the returned data', () => {
    lessonServiceSpy.getLesson.and.returnValue(of(MOCK_DETAIL));
    fixture.detectChanges();
    expect(component.lesson()).toEqual(MOCK_DETAIL);
  });

  it('should set isLoading() to false after successful fetch', () => {
    lessonServiceSpy.getLesson.and.returnValue(of(MOCK_DETAIL));
    fixture.detectChanges();
    expect(component.isLoading()).toBeFalse();
  });

  it('should keep error() as null on success', () => {
    lessonServiceSpy.getLesson.and.returnValue(of(MOCK_DETAIL));
    fixture.detectChanges();
    expect(component.error()).toBeNull();
  });

  // ── Signal state — error path ─────────────────────────────────────────────

  it('should set error() signal on API failure', () => {
    lessonServiceSpy.getLesson.and.returnValue(throwError(() => new Error('500')));
    fixture.detectChanges();
    expect(component.error()).toBeTruthy();
  });

  it('should set isLoading() to false after a failed fetch', () => {
    lessonServiceSpy.getLesson.and.returnValue(throwError(() => new Error('500')));
    fixture.detectChanges();
    expect(component.isLoading()).toBeFalse();
  });

  it('should leave lesson() as null on error', () => {
    lessonServiceSpy.getLesson.and.returnValue(throwError(() => new Error('500')));
    fixture.detectChanges();
    expect(component.lesson()).toBeNull();
  });

  // ── DOM rendering ─────────────────────────────────────────────────────────

  it('should render the lesson title in the DOM', () => {
    lessonServiceSpy.getLesson.and.returnValue(of(MOCK_DETAIL));
    fixture.detectChanges();
    const el: HTMLElement = fixture.nativeElement;
    expect(el.textContent).toContain('The /θ/ Sound');
  });

  it('should render the grammar structure panel when description contains Structure rows', () => {
    const detailWithStructure = {
      ...MOCK_DETAIL,
      description: 'Learn the pattern.\nStructure (+): Subject + verb.\nStructure (-): Subject + do not + verb.',
    };
    lessonServiceSpy.getLesson.and.returnValue(of(detailWithStructure));
    fixture.detectChanges();

    const panel = fixture.nativeElement.querySelector('.grammar-structure');
    expect(panel).toBeTruthy();
    expect(panel.textContent).toContain('Affirmative');
    expect(panel.textContent).toContain('Negative');
  });

  it('should render one app-example-card per example', () => {
    lessonServiceSpy.getLesson.and.returnValue(of(MOCK_DETAIL));
    fixture.detectChanges();
    const cards = fixture.nativeElement.querySelectorAll('app-example-card');
    expect(cards.length).toBe(MOCK_DETAIL.examples.length);
  });

  it('should not render exercise cards when exercises list is empty', () => {
    lessonServiceSpy.getLesson.and.returnValue(of(MOCK_DETAIL));
    fixture.detectChanges();
    const cards = fixture.nativeElement.querySelectorAll('app-exercise-card');
    expect(cards.length).toBe(0);
  });
});
