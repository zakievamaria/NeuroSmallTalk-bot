import re
import csv
from pathlib import Path
from datetime import datetime
from typing import List, Dict

def save_raw_response(case_id: str, prompt_version: str, text: str) -> str:
    """Сохраняет сырой ответ модели в outputs/raw_responses/"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{case_id}_v{prompt_version}_{timestamp}.txt"
    path = Path("outputs/raw_responses") / filename
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    return str(path)

def count_questions(text: str) -> int:
    """Подсчитывает количество вопросов в ответе модели"""
    return len(re.findall(r"^\s*\d+\)", text, flags=re.M))

def save_summary_csv(rows: List[Dict]) -> str:
    """Сохраняет агрегированные результаты в CSV"""
    path = Path("outputs/summaries/results.csv")
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        if rows:
            writer = csv.DictWriter(f, fieldnames=rows[0].keys())
            writer.writeheader()
            writer.writerows(rows)
    return str(path)

def build_prompt(tc: TestCase, prompt_template: str) -> str:
    """Формирует полный промпт из шаблона и параметров теста"""
    return prompt_template.format(
        gender=tc.gender,
        age=tc.age,
        personal_topics=", ".join(tc.personal_topics),
        forbidden_topics=", ".join(tc.forbidden_topics),
        topic_count=tc.topic_count,
        questions_per_topic=tc.questions_per_topic,
    )