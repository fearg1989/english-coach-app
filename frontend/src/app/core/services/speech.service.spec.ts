import { TestBed } from '@angular/core/testing';
import { SpeechService } from './speech.service';

describe('SpeechService', () => {
  let service: SpeechService;
  let mockSpeechSynthesis: jasmine.SpyObj<SpeechSynthesis>;
  let mockUtterance: jasmine.SpyObj<SpeechSynthesisUtterance>;

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

  it('should not throw when speak() is called in unsupported browser', () => {
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
