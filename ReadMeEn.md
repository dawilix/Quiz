# Dubaluba: Voice-Based Word Translation Game

A Python mini-game to practice translating Russian words into English using voice input. The player speaks the translation, the system recognizes the speech, and gives instant feedback.

## 🎯 Goal

To support English language learning through active pronunciation and vocabulary practice. The game trains both knowledge of translations and the skill of saying words aloud, with immediate verification and scoring.

## ✨ Features

- **Three difficulty levels**: Easy, Medium, Hard (with dedicated word sets).
- **5 words per round**: a compact, focused practice session.
- **One attempt per word**: immediate feedback after each answer.
- **Voice input & recognition**: audio captured via microphone and processed with Google Speech API.
- **Automatic translation check**: uses `googletrans` to verify the correct English translation.
- **Scoring system**: 10 points for each correct answer.
- **Round statistics**: total score, number of correct answers, and a final performance summary.
- **User-friendly CLI interface**: clear prompts, emojis, input validation, and error handling.

## 🧠 How It Works

1. **Level selection**: the player chooses “Easy”, “Medium”, or “Hard”.
2. **Word display**: the system randomly picks a Russian word from the selected level.
3. **Voice recording**: the player speaks the English translation for 5 seconds.
4. **Speech recognition**: the recorded audio is processed via `speech_recognition`.
5. **Answer check**: the recognized text is compared to the correct translation (case and extra spaces are ignored).
6. **Feedback**: the system shows whether the answer is correct; if not, it displays the right translation.
7. **Next word**: the round continues until all 5 words are completed.
8. **Final results**: total score, percentage of correct answers, and a motivational message are shown.

## 🛠️ Technologies & Libraries

- `sounddevice` — audio recording from the microphone.
- `scipy.io.wavfile` — saving audio as WAV files.
- `speech_recognition` — speech-to-text via Google Speech API.
- `googletrans` — automatic translation for answer verification.
- `random` — random word selection.
- Standard Python — game logic, I/O, and error handling.

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher.
- An active internet connection (required for speech recognition and translation).
- A working microphone.

### Installation

1. Clone or download the repository.
2. Install the required dependencies:

   ```bash
   pip install sounddevice scipy speechrecognition googletrans
