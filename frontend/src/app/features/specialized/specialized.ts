import { Component, OnInit, inject, signal } from '@angular/core';
import { ActivatedRoute, RouterModule } from '@angular/router';

import { Lesson } from '../../core/models/lesson.model';
import { LessonService } from '../../core/services/lesson.service';

interface SpecializedTopic {
  id: string;
  title: string;
  description: string;
  icon: string;
}

const SPECIALIZED_TOPICS: SpecializedTopic[] = [
  {
    id: 'verb_tenses',
    title: 'Verb Tenses Matrix',
    description: 'Explora y compara tiempos verbales clave con un enfoque visual.',
    icon: '🧭',
  },
  {
    id: 'phrasal_verbs',
    title: 'Phrasal Verbs',
    description: 'Descubre verbos compuestos frecuentes usados en inglés conversacional.',
    icon: '🔗',
  },
  {
    id: 'modal_verbs',
    title: 'Modal Verbs',
    description: 'Aprende a usar must, should, can y otros verbos modales.',
    icon: '⚖️',
  },
  {
    id: 'prepositions',
    title: 'Prepositions',
    description: 'Aprende las preposiciones esenciales y sus usos en contexto técnico.',
    icon: '📍',
  },
  {
    id: 'irregular_verbs',
    title: 'Irregular Verbs Library',
    description: 'Accede a la colección de lecciones dedicadas a verbos irregulares.',
    icon: '⚡',
  },
  {
    id: 'verb_patterns',
    title: 'Verb Patterns',
    description: 'Gerundios e infinitivos: cuándo usar avoid doing vs. decide to do.',
    icon: '🔀',
  },
  {
    id: 'conditionals',
    title: 'Conditionals & Hypotheticals',
    description: 'Condicionales 1º, 2º y Mixed para analizar escenarios y trade-offs.',
    icon: '🔀',
  },
  {
    id: 'passive_voice',
    title: 'Passive Voice',
    description: 'Voz pasiva en todos los tiempos para documentación técnica objetiva.',
    icon: '💬',
  },
  {
    id: 'reported_speech',
    title: 'Reported Speech',
    description: 'Transmite información de terceros con precisión y backshift correcto.',
    icon: '📝',
  },
  {
    id: 'connectors',
    title: 'Connectors & Discourse Markers',
    description: 'Enlaza ideas con however, furthermore y consequently.',
    icon: '🤝',
  },
  {
    id: 'collocations',
    title: 'Collocations',
    description: 'Combinaciones naturales: deploy code, handle errors, breaking change.',
    icon: '🎯',
  },
];

@Component({
  selector: 'app-specialized',
  imports: [RouterModule],
  templateUrl: './specialized.html',
  styleUrl: './specialized.scss',
})
export class SpecializedComponent implements OnInit {
  private readonly route = inject(ActivatedRoute);
  private readonly lessonService = inject(LessonService);

  readonly topic = signal<SpecializedTopic | null>(null);
  readonly lessons = signal<Lesson[]>([]);
  readonly isLoading = signal(true);
  readonly error = signal<string | null>(null);

  ngOnInit(): void {
    const topicId = this.route.snapshot.paramMap.get('topicId');
    const selected = SPECIALIZED_TOPICS.find((topic) => topic.id === topicId) ?? null;
    this.topic.set(selected);

    if (!selected) {
      this.error.set('Tema especializado no encontrado.');
      this.isLoading.set(false);
      return;
    }

    this.lessonService.getLessonsByCategory(selected.id).subscribe({
      next: (data) => {
        this.lessons.set(data);
        this.isLoading.set(false);
      },
      error: () => {
        this.error.set('Error al cargar las lecciones de este tema.');
        this.isLoading.set(false);
      },
    });
  }
}
