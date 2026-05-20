import { Injectable, inject } from '@angular/core';
import { Observable } from 'rxjs';

import { Level } from '../models/level.model';
import { ApiService } from './api.service';

@Injectable({ providedIn: 'root' })
export class LevelService {
  private readonly api = inject(ApiService);

  getLevels(): Observable<Level[]> {
    return this.api.get<Level[]>('/levels/');
  }

  getLevel(id: number): Observable<Level> {
    return this.api.get<Level>(`/levels/${id}`);
  }
}
