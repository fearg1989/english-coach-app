import { Component, Input, signal, computed } from '@angular/core';
import { FormsModule } from '@angular/forms';

import { Exercise } from '../../../../core/models/lesson.model';

type AnswerState = 'idle' | 'correct' | 'incorrect';

@Component({
  selector: 'app-exercise-card',
  imports: [FormsModule],
  templateUrl: './exercise-card.html',
  styleUrl: './exercise-card.scss',
})
export class ExerciseCardComponent {
  @Input({ required: true }) exercise!: Exercise;

  readonly userAnswer = signal('');
  readonly answerState = signal<AnswerState>('idle');

  readonly optionEntries = computed<[string, string][]>(() => {
    if (!this.exercise.options) return [];
    return Object.entries(this.exercise.options) as [string, string][];
  });

  checkAnswer(): void {
    const correct =
      this.userAnswer().trim().toLowerCase() ===
      this.exercise.correct_answer.trim().toLowerCase();
    this.answerState.set(correct ? 'correct' : 'incorrect');
  }

  reset(): void {
    this.userAnswer.set('');
    this.answerState.set('idle');
  }

  /** Phase 4: Azure Speech Services + GPT-4o-mini pronunciation assessment. */
  onRecordAnswer(): void {
    // TODO Phase 4 — enviar grabación a /api/v1/exercises/:id/validate
    console.info('[Phase 4] Validación de pronunciación no implementada aún.');
  }
}
