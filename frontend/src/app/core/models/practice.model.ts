export interface PracticeExercise {
  id: number;
  type: 'fill_in_the_blank' | 'roleplay_response' | 'multiple_choice' | 'translation' | 'open_writing';
  prompt: string;
  correct_answer: string;
  hint: string;
  options?: string[] | null;  // Only present for multiple_choice
}

export interface PracticeSession {
  session_id: string;
  theme: string;
  grammar_focus: string;
  exercises: PracticeExercise[];
}

export interface PracticeEvaluationResult {
  transcribed_text: string;
  accuracy_score: number;
  words: Array<{
    word: string;
    status: 'correct' | 'unclear' | 'incorrect';
    accuracy_score: number;
    transcribed_as: string | null;
  }>;
}
