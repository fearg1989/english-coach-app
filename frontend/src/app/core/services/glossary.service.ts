import { Injectable, inject } from '@angular/core';
import { HttpParams } from '@angular/common/http';
import { Observable } from 'rxjs';

import { GlossaryEntry, GlossaryType } from '../models/glossary.model';
import { ApiService } from './api.service';

@Injectable({ providedIn: 'root' })
export class GlossaryService {
  private readonly api = inject(ApiService);

  getEntries(type: GlossaryType): Observable<GlossaryEntry[]> {
    const params = new HttpParams().set('type', type);
    return this.api.get<GlossaryEntry[]>('/glossary/', params);
  }
}
