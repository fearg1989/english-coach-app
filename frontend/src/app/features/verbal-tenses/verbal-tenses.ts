import { Component, signal, computed } from '@angular/core';
import { RouterModule } from '@angular/router';
import { CommonModule } from '@angular/common';

interface TenseStructure {
  affirmative: string;
  negative: string;
  interrogative: string;
}

interface VerbalTense {
  id: string;
  name: string;
  level: string;
  structure: TenseStructure;
}

@Component({
  selector: 'app-verbal-tenses',
  standalone: true,
  imports: [RouterModule, CommonModule],
  templateUrl: './verbal-tenses.html',
  styleUrl: './verbal-tenses.scss',
})
export class VerbalTensesComponent {
  readonly activeTenseId = signal<string | null>(null);
  readonly sortBy = signal<'default' | 'time' | 'level'>('level');

  readonly sortedTenses = computed(() => {
    const tenses = this.tenses();
    const sort = this.sortBy();

    if (sort === 'level') {
      const levelOrder = ['A1', 'A2', 'B1', 'B2', 'C1', 'C2'];
      return [...tenses].sort((a, b) => {
        return levelOrder.indexOf(a.level) - levelOrder.indexOf(b.level);
      });
    }

    if (sort === 'time') {
      const timeOrder = ['Past', 'Present', 'Future'];
      return [...tenses].sort((a, b) => {
        const getTime = (name: string) => {
          if (name.includes('Past')) return 'Past';
          if (name.includes('Present')) return 'Present';
          if (name.includes('Future')) return 'Future';
          return '';
        };
        return timeOrder.indexOf(getTime(a.name)) - timeOrder.indexOf(getTime(b.name));
      });
    }

    return tenses;
  });

  setSort(sort: 'default' | 'time' | 'level'): void {
    this.sortBy.set(sort);
  }

  readonly tenses = signal<VerbalTense[]>([
    {
      id: 'present-simple',
      name: 'Present Simple',
      level: 'A1',
      structure: {
        affirmative: 'Subject + base verb (add -s/-es for 3rd-person singular)',
        negative: 'Subject + do/does + not + base verb',
        interrogative: 'Do/Does + Subject + base verb?',
      },
    },
    {
      id: 'present-continuous',
      name: 'Present Continuous',
      level: 'A1',
      structure: {
        affirmative: 'Subject + am/is/are + verb-ing',
        negative: 'Subject + am/is/are + not + verb-ing',
        interrogative: 'Am/Is/Are + Subject + verb-ing?',
      },
    },
    {
      id: 'present-perfect',
      name: 'Present Perfect',
      level: 'B1',
      structure: {
        affirmative: 'Subject + have/has + past participle',
        negative: 'Subject + have/has + not + past participle',
        interrogative: 'Have/Has + Subject + past participle?',
      },
    },
    {
      id: 'present-perfect-continuous',
      name: 'Present Perfect Continuous',
      level: 'B1',
      structure: {
        affirmative: 'Subject + have/has + been + verb-ing',
        negative: 'Subject + have/has + not + been + verb-ing',
        interrogative: 'Have/Has + Subject + been + verb-ing?',
      },
    },
    {
      id: 'past-simple',
      name: 'Past Simple',
      level: 'A2',
      structure: {
        affirmative: 'Subject + past verb (regular: +ed, irregular: 2nd column)',
        negative: 'Subject + did + not + base verb',
        interrogative: 'Did + Subject + base verb?',
      },
    },
    {
      id: 'past-continuous',
      name: 'Past Continuous',
      level: 'A2',
      structure: {
        affirmative: 'Subject + was/were + verb-ing',
        negative: 'Subject + was/were + not + verb-ing',
        interrogative: 'Was/Were + Subject + verb-ing?',
      },
    },
    {
      id: 'past-perfect',
      name: 'Past Perfect',
      level: 'B1',
      structure: {
        affirmative: 'Subject + had + past participle',
        negative: 'Subject + had + not + past participle',
        interrogative: 'Had + Subject + past participle?',
      },
    },
    {
      id: 'past-perfect-continuous',
      name: 'Past Perfect Continuous',
      level: 'B2',
      structure: {
        affirmative: 'Subject + had + been + verb-ing',
        negative: 'Subject + had + not + been + verb-ing',
        interrogative: 'Had + Subject + been + verb-ing?',
      },
    },
    {
      id: 'future-simple',
      name: 'Future Simple',
      level: 'A2',
      structure: {
        affirmative: 'Subject + will + base verb',
        negative: 'Subject + will + not + base verb',
        interrogative: 'Will + Subject + base verb?',
      },
    },
    {
      id: 'future-continuous',
      name: 'Future Continuous',
      level: 'B2',
      structure: {
        affirmative: 'Subject + will + be + verb-ing',
        negative: 'Subject + will + not + be + verb-ing',
        interrogative: 'Will + Subject + be + verb-ing?',
      },
    },
    {
      id: 'future-perfect',
      name: 'Future Perfect',
      level: 'C1',
      structure: {
        affirmative: 'Subject + will + have + past participle',
        negative: 'Subject + will + not + have + past participle',
        interrogative: 'Will + Subject + have + past participle?',
      },
    },
    {
      id: 'future-perfect-continuous',
      name: 'Future Perfect Continuous',
      level: 'C2',
      structure: {
        affirmative: 'Subject + will + have + been + verb-ing',
        negative: 'Subject + will + not + have + been + verb-ing',
        interrogative: 'Will + Subject + have + been + verb-ing?',
      },
    },
  ]);

  toggleTense(id: string): void {
    if (this.activeTenseId() === id) {
      this.activeTenseId.set(null);
    } else {
      this.activeTenseId.set(id);
    }
  }
}
