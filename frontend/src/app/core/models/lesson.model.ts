export type LessonType = 'grammar' | 'phonetics';
export type LessonCategory = 'verb_tenses' | 'phrasal_verbs' | 'prepositions' | 'irregular_verbs';
export type ExerciseType = 'multiple_choice' | 'fill_blank' | 'pronunciation';

export interface Example {
  id: number;
  lesson_id: number;
  phrase: string;
  translation: string;
  ipa_notation: string | null;
  audio_url: string | null; // Phase 2: populated by TTS service
  order_index: number;
  created_at: string;
  updated_at: string;
}

export interface Exercise {
  id: number;
  lesson_id: number;
  type: ExerciseType;
  question: string;
  correct_answer: string;
  options: Record<string, string> | null;
  order_index: number;
  created_at: string;
  updated_at: string;
}

export interface Lesson {
  id: number;
  level_id: number;
  title: string;
  type: LessonType;
  category: LessonCategory;
  description: string | null;
  order_index: number;
  is_published: boolean;
  created_at: string;
  updated_at: string;
}

export interface LessonDetail extends Lesson {
  examples: Example[];
  exercises: Exercise[];
}
