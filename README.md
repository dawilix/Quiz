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


# Dubaluba: игра на перевод слов голосом

Мини‑игра на Python для тренировки перевода русских слов на английский с помощью голосового ввода. Игрок произносит перевод слова, система распознаёт речь и сразу даёт обратную связь — верно или нет.

## 🎯 Цель проекта

Помочь в изучении английского языка через активную практику произношения и запоминания слов. Игра тренирует не только знание переводов, но и навык произносить слова вслух, а также даёт мгновенную проверку и оценку результата.

## ✨ Возможности

- **Три уровня сложности**: Легко, Средне, Сложно (со своими наборами слов).
- **5 слов за раунд**: компактная и сфокусированная тренировка лексики.
- **Одна попытка на слово**: сразу после ответа — обратная связь.
- **Голосовой ввод и распознавание**: запись через микрофон, распознавание речи через Google Speech API.
- **Автоматическая проверка перевода**: для сверки ответа используется библиотека `googletrans`.
- **Система баллов**: за каждое верное слово начисляется 10 баллов.
- **Статистика по раунду**: общий счёт, количество правильных ответов, итоговая оценка результата.
- **Удобный интерфейс в консоли**: понятные подсказки, эмодзи, защита от некорректного ввода и обработка ошибок.

## 🧠 Как работает игра

1. **Выбор уровня**. Игрок выбирает «Легко», «Средне» или «Сложно».
2. **Слово раунда**. Система случайно выбирает русское слово из списка для выбранного уровня.
3. **Запись голоса**. В течение 5 секунд игрок произносит английский перевод слова.
4. **Распознавание речи**. Записанный аудиофайл обрабатывается библиотекой `speech_recognition`.
5. **Проверка ответа**. Распознанный текст сравнивается с правильным переводом (регистр и лишние пробелы не учитываются).
6. **Обратная связь**. Система показывает, верный ли ответ; если нет — выводит правильный вариант.
7. **Переход к следующему слову**. Раунд продолжается, пока не будут пройдены все 5 слов.
8. **Итоговые результаты**. В конце выводится общий счёт, процент правильных ответов и мотивационное сообщение.

## 🛠️ Технологии и библиотеки

- `sounddevice` — запись звука с микрофона.
- `scipy.io.wavfile` — сохранение аудио в формате WAV.
- `speech_recognition` — распознавание речи через Google Speech API.
- `googletrans` — автоматический перевод для проверки ответов.
- `random` — случайный выбор слова.
- Стандартный Python — логика игры, ввод/вывод, обработка ошибок.

## 🚀 Как начать

### Предварительные требования

- Python версии 3.8 или выше.
- Активное подключение к интернету (требуется для распознавания речи и перевода).
- Рабочий микрофон.

### Установка

1. Клонируйте или скачайте репозиторий.
2. Установите необходимые зависимости:

   ```bash
   pip install sounddevice scipy speechrecognition googletrans
