import { Component, OnInit, inject, signal, computed } from '@angular/core';
import { ActivatedRoute, RouterModule } from '@angular/router';

import { GlossaryEntry, GlossaryType } from '../../core/models/glossary.model';
import { GlossaryService } from '../../core/services/glossary.service';

type ActiveTab = GlossaryType;

@Component({
  selector: 'app-glossary',
  imports: [RouterModule],
  templateUrl: './glossary.html',
  styleUrl: './glossary.scss',
})
export class GlossaryComponent implements OnInit {
  private readonly glossaryService = inject(GlossaryService);
  private readonly route = inject(ActivatedRoute);

  readonly activeTab = signal<ActiveTab>('phrasal_verb');
  readonly from = signal<string | null>(null);
  readonly phrasalVerbs = signal<GlossaryEntry[]>([]);
  readonly irregularVerbs = signal<GlossaryEntry[]>([]);
  readonly isLoadingPhraSal = signal(true);
  readonly isLoadingIrregular = signal(true);
  readonly error = signal<string | null>(null);

  readonly currentEntries = computed<GlossaryEntry[]>(() =>
    this.activeTab() === 'phrasal_verb' ? this.phrasalVerbs() : this.irregularVerbs()
  );

  readonly isLoading = computed(() =>
    this.activeTab() === 'phrasal_verb' ? this.isLoadingPhraSal() : this.isLoadingIrregular()
  );

  ngOnInit(): void {
    this.from.set(this.route.snapshot.queryParamMap.get('from'));
    this.loadPhrasalVerbs();
    this.loadIrregularVerbs();
  }

  setTab(tab: ActiveTab): void {
    this.activeTab.set(tab);
  }

  private loadPhrasalVerbs(): void {
    this.glossaryService.getEntries('phrasal_verb').subscribe({
      next: (data) => {
        const sorted = [...data].sort((a, b) => a.term.localeCompare(b.term));
        this.phrasalVerbs.set(sorted);
        this.isLoadingPhraSal.set(false);
      },
      error: () => {
        this.error.set('No se pudieron cargar los phrasal verbs.');
        this.isLoadingPhraSal.set(false);
      },
    });
  }

  private loadIrregularVerbs(): void {
    this.glossaryService.getEntries('irregular_verb').subscribe({
      next: (data) => {
        const sorted = [...data].sort((a, b) => a.term.localeCompare(b.term));
        this.irregularVerbs.set(sorted);
        this.isLoadingIrregular.set(false);
      },
      error: () => {
        this.error.set('No se pudieron cargar los verbos irregulares.');
        this.isLoadingIrregular.set(false);
      },
    });
  }
}
