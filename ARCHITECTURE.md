# NeuroSmallTalk-bot
NeuroSmallTalk-Bot/
├── src/
│   ├── run_experiment.py
│   ├── prompt_templates.py
│   ├── schemas.py
│   ├── utils.py
│   └── gigachat_client.py
├── prompts/                # Шаблоны промптов
│   ├── prompt_v1.txt
│   ├── prompt_v2.txt
│   └── prompt_v3.txt
├── experiments/            # Конфигурация экспериментов
│   ├── test_cases.json
│   └── analysis.md
├── outputs/                # СЫРЫЕ ответы модели (НЕ коммитить в Git!)
│   ├── raw_responses/
│   │   ├── case_001_v1.txt
│   │   ├── case_001_v2.txt
│   │   └── ...
│   └── summaries/
│       └── results.csv
├── README.md
├── requirements.txt
├── .env.example
└── .gitignore