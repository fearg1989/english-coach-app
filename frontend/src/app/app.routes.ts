import { Routes } from '@angular/router';

export const routes: Routes = [
  {
    path: '',
    loadComponent: () => import('./features/home/home').then((m) => m.HomeComponent),
    title: 'English Coach — Aprende inglés A1–C2',
  },
  {
    path: 'level/:levelId',
    loadComponent: () => import('./features/level/level').then((m) => m.LevelComponent),
    title: 'English Coach — Nivel',
  },
  {
    path: 'lesson/:lessonId',
    loadComponent: () => import('./features/lesson/lesson').then((m) => m.LessonComponent),
    title: 'English Coach — Lección',
  },
  {
    path: 'specialized/:topicId',
    loadComponent: () => import('./features/specialized/specialized').then((m) => m.SpecializedComponent),
    title: 'English Coach — Specialized Topic',
  },
  {
    path: 'glossary',
    loadComponent: () => import('./features/glossary/glossary').then((m) => m.GlossaryComponent),
    title: 'English Coach — Glosario',
  },
  {
    path: 'verbal-tenses',
    loadComponent: () => import('./features/verbal-tenses/verbal-tenses').then((m) => m.VerbalTensesComponent),
    title: 'English Coach — Verbal Tenses',
  },
  {
    path: '**',
    redirectTo: '',
  },
];
