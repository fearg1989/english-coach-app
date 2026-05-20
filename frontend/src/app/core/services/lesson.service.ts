import { Injectable, inject } from '@angular/core';
import { HttpParams } from '@angular/common/http';
import { Observable } from 'rxjs';

import { Lesson, LessonDetail, LessonType } from '../models/lesson.model';
import { ApiService } from './api.service';

@Injectable({ providedIn: 'root' })
export class LessonService {
  private readonly api = inject(ApiService);

  getLessonsByLevel(levelId: number): Observable<Lesson[]> {
    return this.api.get<Lesson[]>(`/lessons/level/${levelId}`);
  }

  getLessonsByType(levelId: number, type: LessonType): Observable<Lesson[]> {
    const params = new HttpParams().set('type', type);
    return this.api.get<Lesson[]>(`/lessons/level/${levelId}`, params);
  }

  getLessonsByCategory(category: string): Observable<Lesson[]> {
    return this.api.get<Lesson[]>(`/lessons/category/${category}`);
  }

  getLesson(id: number): Observable<LessonDetail> {
    return this.api.get<LessonDetail>(`/lessons/${id}`);
  }
}
