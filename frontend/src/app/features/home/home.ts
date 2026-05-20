import { Component, OnInit, inject, signal } from '@angular/core';
import { ActivatedRoute, RouterModule } from '@angular/router';

import { Level } from '../../core/models/level.model';
import { LevelService } from '../../core/services/level.service';

interface TopicCard {
  id: string;
  title: string;
  description: string;
  icon: string;
  route: string | string[];
}

const CORE_MECHANICS_TOPICS: TopicCard[] = [
  {
    id: 'verb_tenses',
    title: 'Verb Tenses',
    description: 'Domina los 12 tiempos verbales del inglés con ejemplos técnicos y contexto real.',
    icon: '',
    route: ['/verbal-tenses'],
  },
  {
    id: 'modal_verbs',
    title: 'Modal Verbs',
    description: 'Aprende a expresar obligación, posibilidad y deducción con must, should, can y más.',
    icon: '',
    route: ['/specialized', 'modal_verbs'],
  },
  {
    id: 'prepositions',
    title: 'Prepositions',
    description: 'Domina las preposiciones esenciales y sus usos en contexto técnico.',
    icon: '',
    route: ['/specialized', 'prepositions'],
  },
  {
    id: 'phrasal_verbs',
    title: 'Phrasal Verbs',
    description: 'Aprende los verbos compuestos más útiles: spin up, roll back, figure out y más.',
    icon: '',
    route: ['/glossary'],
  },
];

const ADVANCED_FLOW_TOPICS: TopicCard[] = [
  {
    id: 'verb_patterns',
    title: 'Verb Patterns',
    description: 'Gerundios e infinitivos: cuándo usar avoid doing vs. decide to do en contexto IT.',
    icon: '',
    route: ['/specialized', 'verb_patterns'],
  },
  {
    id: 'conditionals',
    title: 'Conditionals & Hypotheticals',
    description: 'Analiza trade-offs técnicos con los condicionales 1º, 2º y Mixed.',
    icon: '',
    route: ['/specialized', 'conditionals'],
  },
  {
    id: 'passive_voice',
    title: 'Passive Voice',
    description: 'Redacta documentación técnica objetiva con voz pasiva en todos los tiempos.',
    icon: '',
    route: ['/specialized', 'passive_voice'],
  },
  {
    id: 'reported_speech',
    title: 'Reported Speech',
    description: 'Transmite lo que dijo el equipo, el cliente o el manager con precisión.',
    icon: '',
    route: ['/specialized', 'reported_speech'],
  },
  {
    id: 'connectors',
    title: 'Connectors & Discourse Markers',
    description: 'Enlaza ideas con however, furthermore, consequently en code reviews y docs.',
    icon: '',
    route: ['/specialized', 'connectors'],
  },
  {
    id: 'collocations',
    title: 'Collocations',
    description: 'Combina palabras de forma natural: deploy code, handle errors, breaking change.',
    icon: '',
    route: ['/specialized', 'collocations'],
  },
];

@Component({
  selector: 'app-home',
  imports: [RouterModule],
  templateUrl: './home.html',
  styleUrl: './home.scss',
})
export class HomeComponent implements OnInit {
  private readonly levelService = inject(LevelService);
  private readonly route = inject(ActivatedRoute);

  readonly levels = signal<Level[]>([]);
  readonly isLoading = signal(true);
  readonly error = signal<string | null>(null);
  readonly activeView = signal<'levels' | 'specialized'>('levels');

  readonly coreTopics = signal<TopicCard[]>(CORE_MECHANICS_TOPICS);
  readonly advancedTopics = signal<TopicCard[]>(ADVANCED_FLOW_TOPICS);

  ngOnInit(): void {
    const view = this.route.snapshot.queryParamMap.get('view');
    if (view === 'specialized') {
      this.activeView.set('specialized');
    }

    this.levelService.getLevels().subscribe({
      next: (data) => {
        this.levels.set(data);
        this.isLoading.set(false);
      },
      error: () => {
        this.error.set('Error al cargar los niveles. Verifica que el backend esté activo.');
        this.isLoading.set(false);
      },
    });
  }
}
