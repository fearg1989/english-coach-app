import { Component, OnInit, inject, signal, computed } from '@angular/core';
import { ActivatedRoute, RouterModule } from '@angular/router';
import { forkJoin } from 'rxjs';

import { Level } from '../../core/models/level.model';
import { Lesson, LessonType } from '../../core/models/lesson.model';
import { LevelService } from '../../core/services/level.service';
import { LessonService } from '../../core/services/lesson.service';

type FilterType = 'all' | LessonType;

@Component({
  selector: 'app-level',
  imports: [RouterModule],
  templateUrl: './level.html',
  styleUrl: './level.scss',
})
export class LevelComponent implements OnInit {
  private readonly route = inject(ActivatedRoute);
  private readonly levelService = inject(LevelService);
  private readonly lessonService = inject(LessonService);

  readonly level = signal<Level | null>(null);
  readonly lessons = signal<Lesson[]>([]);
  readonly isLoading = signal(true);
  readonly error = signal<string | null>(null);
  readonly activeFilter = signal<FilterType>('grammar');

  readonly filteredLessons = computed(() => {
    const filter = this.activeFilter();
    if (filter === 'all') return this.lessons();
    return this.lessons().filter((l) => l.type === filter);
  });

  ngOnInit(): void {
    const levelId = Number(this.route.snapshot.paramMap.get('levelId'));

    forkJoin({
      level: this.levelService.getLevel(levelId),
      lessons: this.lessonService.getLessonsByLevel(levelId),
    }).subscribe({
      next: ({ level, lessons }) => {
        this.level.set(level);
        this.lessons.set(lessons);
        this.isLoading.set(false);
      },
      error: () => {
        this.error.set('Error al cargar el nivel. Verifica que el backend esté activo.');
        this.isLoading.set(false);
      },
    });
  }

  setFilter(filter: FilterType): void {
    this.activeFilter.set(filter);
  }
}
