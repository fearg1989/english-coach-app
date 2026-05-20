import { TestBed } from '@angular/core/testing';
import { SpeechService } from './speech.service';

describe('SpeechService', () => {
  let service: SpeechService;
  let mockSpeechSynthesis: jasmine.SpyObj<SpeechSynthesis>;

  beforeEach(() => {
    mockSpeechSynthesis = jasmine.createSpyObj<SpeechSynthesis>(
      'SpeechSynthesis',
      ['speak', 'cancel', 'getVoices'],
      { speaking: false }
    );

    mockSpeechSynthesis.getVoices.and.returnValue([]);

    // Patch window.speechSynthesis before service creation
    Object.defineProperty(window, 'speechSynthesis', {
      value: mockSpeechSynthesis,
      configurable: true,
      writable: true,
    });

    TestBed.configureTestingModule({});
    service = TestBed.inject(SpeechService);
  });

  afterEach(() => {
    service?.stop();
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });

  it('should report isSupported() true when window.speechSynthesis exists', () => {
    expect(service.isSupported()).toBeTrue();
  });

  it('should report isSupported() false when window.speechSynthesis is absent', () => {
    Object.defineProperty(window, 'speechSynthesis', {
      value: undefined,
      configurable: true,
      writable: true,
    });
    // Create a fresh instance (not the cached singleton) in an injection context
    let unsupportedService!: SpeechService;
    TestBed.runInInjectionContext(() => {
      unsupportedService = new SpeechService();
    });
    expect(unsupportedService.isSupported()).toBeFalse();
    // Restore for other tests
    Object.defineProperty(window, 'speechSynthesis', {
      value: mockSpeechSynthesis,
      configurable: true,
      writable: true,
    });
  });

  it('should have isSpeaking signal initialized to false', () => {
    expect(service.isSpeaking()).toBeFalse();
  });

  it('should call speechSynthesis.speak() when speak() is called', () => {
    service.speak('Hello world');
    expect(mockSpeechSynthesis.speak).toHaveBeenCalled();
  });

  it('should NOT call speak() with empty string', () => {
    service.speak('   ');
    expect(mockSpeechSynthesis.speak).not.toHaveBeenCalled();
  });

  it('should call cancel() before a new utterance to stop previous speech', () => {
    service.speak('First sentence');
    service.speak('Second sentence');
    expect(mockSpeechSynthesis.cancel).toHaveBeenCalled();
  });

  it('stop() should call cancel() on speechSynthesis', () => {
    service.stop();
    expect(mockSpeechSynthesis.cancel).toHaveBeenCalled();
  });

  it('stop() should set isSpeaking signal to false', () => {
    service.stop();
    expect(service.isSpeaking()).toBeFalse();
  });

  it('should strip intonation arrow symbols before speaking', () => {
    service.speak("I didn't say the deploy was READY. ↘");
    const utterance: SpeechSynthesisUtterance =
      (mockSpeechSynthesis.speak as jasmine.Spy).calls.mostRecent().args[0];
    expect(utterance.text).not.toContain('↘');
    expect(utterance.text).toBe("I didn't say the deploy was READY.");
  });

  it('should strip fall-rise intonation markers (↘↗) before speaking', () => {
    service.speak("I didn't SAY the deploy was ready. ↘↗");
    const utterance: SpeechSynthesisUtterance =
      (mockSpeechSynthesis.speak as jasmine.Spy).calls.mostRecent().args[0];
    expect(utterance.text).toBe("I didn't SAY the deploy was ready.");
  });

  it('should strip rise intonation marker (↗) before speaking', () => {
    service.speak("I didn't say THE deploy was ready. ↗");
    const utterance: SpeechSynthesisUtterance =
      (mockSpeechSynthesis.speak as jasmine.Spy).calls.mostRecent().args[0];
    expect(utterance.text).toBe("I didn't say THE deploy was ready.");
  });

  // ─── Intonation approximation (pitch/rate) ──────────────────────────────

  it('should apply low pitch for falling tone (↘)', () => {
    service.speak("The deploy is READY. ↘");
    const utterance: SpeechSynthesisUtterance =
      (mockSpeechSynthesis.speak as jasmine.Spy).calls.mostRecent().args[0];
    expect(utterance.pitch).toBeLessThan(1.0);
  });

  it('should apply high pitch for rising tone (↗)', () => {
    service.speak("Is the deploy ready? ↗");
    const utterance: SpeechSynthesisUtterance =
      (mockSpeechSynthesis.speak as jasmine.Spy).calls.mostRecent().args[0];
    expect(utterance.pitch).toBeGreaterThan(1.0);
  });

  it('should apply mid-high pitch for fall-rise tone (↘↗)', () => {
    service.speak("I didn't SAY the deploy was ready. ↘↗");
    const utterance: SpeechSynthesisUtterance =
      (mockSpeechSynthesis.speak as jasmine.Spy).calls.mostRecent().args[0];
    // Fall-rise is between neutral and high — pitch = 1.1
    expect(utterance.pitch).toBeGreaterThan(1.0);
    expect(utterance.pitch).toBeLessThan(1.3);
  });

  it('should apply neutral pitch for phrases without intonation markers', () => {
    service.speak("She works every day.");
    const utterance: SpeechSynthesisUtterance =
      (mockSpeechSynthesis.speak as jasmine.Spy).calls.mostRecent().args[0];
    expect(utterance.pitch).toBe(1.0);
  });

  it('should handle speak() gracefully when speechSynthesis is unavailable', () => {
    let unsupportedService!: SpeechService;
    TestBed.runInInjectionContext(() => {
      Object.defineProperty(window, 'speechSynthesis', {
        value: undefined,
        configurable: true,
        writable: true,
      });
      unsupportedService = new SpeechService();
    });
    expect(() => unsupportedService.speak('Test')).not.toThrow();
    // Restore
    Object.defineProperty(window, 'speechSynthesis', {
      value: mockSpeechSynthesis,
      configurable: true,
      writable: true,
    });
  });
});
