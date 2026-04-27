#!/usr/bin/env python3
"""
Основной скрипт для запуска экспериментов по prompt engineering с GigaChat.
"""
import os
from datetime import datetime
from dotenv import load_dotenv
from prompt_templates import PROMPT_V1
from schemas import TestCase
from utils import save_raw_response, count_questions, save_summary_csv, build_prompt
from gigachat_client import get_client

load_dotenv()

# Тестовые кейсы
test_cases = [
    TestCase(
        case_id="001",
        gender="ж",
        age=21,
        personal_topics=["музыка", "фильмы", "спорт", "друзья", "семья"],
        forbidden_topics=["политика", "войны", "экономика"],
        topic_count=5,
        questions_per_topic=4,
    ),
    TestCase(
        case_id="002",
        gender="м",
        age=45,
        personal_topics=["рыбалка", "автомобили", "работа", "дом", "путешествия"],
        forbidden_topics=["болезни", "конфликты", "финансы"],
        topic_count=5,
        questions_per_topic=4,
    ),
]

rows = []
prompt_version = "1"

with get_client() as giga:
    print("Запуск экспериментов...")
    for tc in test_cases:
        print(f"Обработка кейса {tc.case_id}...")

        prompt = build_prompt(tc, PROMPT_V1)

        response = giga.chat(prompt)
        output = response.choices[0].message.content

        # Сохраняем сырой ответ
        raw_path = save_raw_response(tc.case_id, prompt_version, output)

        # Подсчитываем метрики
        questions_count = count_questions(output)

        row = {
            "case_id": tc.case_id,
            "raw_file": raw_path,
            "gender": tc.gender,
            "age": tc.age,
            "topic_count": tc.topic_count,
            "questions_per_topic": tc.questions_per_topic,
            "output_questions_count": questions_count,
            "timestamp": datetime.now().isoformat(),
        }
        rows.append(row)

        print(f"Кейс {tc.case_id}: {questions_count} вопросов сохранено в {raw_path}")

# Сохраняем сводку
summary_path = save_summary_csv(rows)
print(f"\nЭксперимент завершён!")
print(f"Сырые ответы: outputs/raw_responses/")
print(f"Сводка: {summary_path}")
