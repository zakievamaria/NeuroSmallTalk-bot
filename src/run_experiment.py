#!/usr/bin/env python3
"""
Основной скрипт для запуска экспериментов по prompt engineering с GigaChat.
"""

from datetime import datetime

import json
from dotenv import load_dotenv
from prompt_templates import PROMPT_V1
from schemas import TestCase
from utils import build_prompt, count_questions, EXPERIMENTS_PATH, save_raw_response, save_summary_csv
from gigachat_client import get_client

load_dotenv()

with open(EXPERIMENTS_PATH / "test_cases.json", "r", encoding='utf-8') as file_to_read:
    cases = json.load(file_to_read)

test_cases = [
    TestCase(**cases["case_1"]),
    TestCase(**cases["case_2"]),
    TestCase(**cases["case_3"]),
    TestCase(**cases["case_4"]),
    TestCase(**cases["case_5"]),
    TestCase(**cases["case_6"]),
    TestCase(**cases["case_7"])
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

        raw_path = save_raw_response(tc.case_id, prompt_version, output)

        questions_count = count_questions(output)

        row = {
            "case_id": tc.case_id,
            "raw_file": raw_path,
            "gender": tc.gender,
            "age": tc.age,
            "topic_count": tc.topic_count,
            "questions_per_topic": tc.questions_per_topic,
            "output_questions_count": questions_count,
            "timestamp": datetime.now().isoformat()
        }
        rows.append(row)

        print(f"Кейс {tc.case_id}: {questions_count} вопросов сохранено в {raw_path}")

# Сохраняем сводку
summary_path = save_summary_csv(rows)
