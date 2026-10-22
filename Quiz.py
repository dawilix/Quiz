import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import speech_recognition as sr
from googletrans import Translator
import random

# Словарь слов по уровням
words_by_level = {
    "easy": [
        "кот", "собака", "яблоко", "молоко", "солнце",
        "чай", "хлеб", "стул"
    ],
    "medium": [
        "банан", "школа", "друг", "окно", "жёлтый",
        "машина", "улица", "картина"
    ],
    "hard": [
        "технология", "университет", "информация", "произношение", "воображение",
        "исследование", "оборудование", "разработка"
    ]
}

def pipidastr(duration=5, sample_rate=44100, language='en-US', translate_to='en', words_count=5):
    print("=" * 50)
    print("🎮 Игра «Дубалуба»: переведи 5 слов на английский!")
    print("=" * 50)

    # Выбор уровня
    while True:
        wr = input("Выбери уровень сложности: Легко / Средне / Сложно: ").strip().lower()
        if wr in ["легко", "средне", "сложно"]:
            break
        print("⚠️ Неверный ввод. Попробуй ещё раз: Легко, Средне или Сложно.")

    level_map = {"легко": "easy", "средне": "medium", "сложно": "hard"}
    chosen_level = level_map[wr]

    total_score = 0
    correct_words = 0

    for word_num in range(1, words_count + 1):
        lv = random.choice(words_by_level[chosen_level])
        print(f"\n📜 Слово {word_num} из {words_count}: {lv}")

        # Получаем перевод
        translator = Translator()
        try:
            translation = translator.translate(lv, dest=translate_to)
            correct_answer = translation.text.lower().strip()
        except Exception as e:
            print(f"⚠️ Ошибка перевода слова: {e}")
            continue

        print("🎤 Говори перевод на английском (5 секунд)...")

        recording = sd.rec(
            int(duration * sample_rate),
            samplerate=sample_rate,
            channels=1,
            dtype="int16"
        )
        sd.wait()

        wav.write("output.wav", sample_rate, recording)

        recognizer = sr.Recognizer()
        with sr.AudioFile("output.wav") as source:
            audio = recognizer.record(source)

        try:
            text = recognizer.recognize_google(audio, language=language)
            print(f"🗣 Ты сказал: {text}")
            user_text = text.lower().strip()

            if user_text == correct_answer:
                total_score += 10
                correct_words += 1
                print("🎉 Правильно!")
            else:
                print(f"❌ Неверно. Правильный ответ: {correct_answer}")

        except sr.UnknownValueError:
            print("⚠️ Не удалось распознать речь (слишком тихо/шумно). Правильный ответ: " + correct_answer)
        except sr.RequestError as e:
            print(f"⚠️ Ошибка сервиса распознавания: {e}")
            return

        print(f"✅ Текущий счёт: {total_score} баллов, угадано слов: {correct_words}")

    print("\n" + "=" * 50)
    print(f"🏆 Итоговый счёт: {total_score} баллов")
    print(f"📊 Угадано слов: {correct_words} из {words_count}")
    if correct_words == words_count:
        print("🌟 Идеально! Отличный результат!")
    elif correct_words > 0:
        print("👍 Хорошая работа, продолжай тренироваться!")
    else:
        print("😔 Сегодня не получилось — потренируйся ещё, будет лучше!")
    print("=" * 50)

if __name__ == '__main__':
    pipidastr()
