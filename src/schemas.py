from dataclasses import dataclass
from typing import List

@dataclass
class TestCase:
    gender: str
    age: int
    personal_topics: List[str]
    forbidden_topics: List[str]
    topic_count: int
    questions_per_topic: int
