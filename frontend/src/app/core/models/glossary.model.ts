export type GlossaryType = 'phrasal_verb' | 'irregular_verb';

export interface GlossaryEntry {
  id: number;
  type: GlossaryType;
  term: string;
  meaning: string;
  form_past: string | null;
  form_participle: string | null;
  order_index: number;
  created_at: string;
  updated_at: string;
}
