# Python-библиотеки и программные средства

Инструментальная база практических заданий. Формат карточки: [resource-card-template.md](../../resource-card-template.md).

## Учебный код в репозитории

| Файл | Назначение |
|---|---|
| [lr3_record_matching_template.py](lr3_record_matching_template.py) | шаблон канонизации ФИО и сопоставления записей для ЛР-3; читает `crm_a_sample.csv` / `crm_b_sample.csv` (разные имена столбцов — учебный schema mismatch) |
| [../../benchmarks/lr3_template_expected_stdout.txt](../../benchmarks/lr3_template_expected_stdout.txt) | пример stdout при запуске шаблона на учебных CSV |

Зависимости: **только стандартная библиотека Python 3** (отдельный `requirements.txt` не нужен).

Запуск из корня репозитория:

```bash
python3 resources/software/python-libs/lr3_record_matching_template.py
```

## Рекомендуемый стек

| Средство | Назначение | Связь с КИМ |
|---|---|---|
| Python, Jupyter / VS Code | прототипы, ЛР-3 | ЛР-1—ЛР-4 |
| PostgreSQL | реляционные витрины | модули 3, 7–9, ЛР-1, ЛР-3 |
| Apache Spark / Airflow / dbt (по выбору) | обработка и оркестрация | модули 7, 9, ЛР-2 |
| Векторные БД (например Milvus / Qdrant / Weaviate) | векторный поиск | модуль 6, ЛР-1 |
| Docker | локальный запуск сервисов | ЛР-1, ЛР-4 |
| draw.io / C4 / Camunda Modeler | архитектура и BPMN | ЛР-1, ЛР-3, ЛР-4 |
| Облачные PaaS (учебный грант) | Data Lake | модуль 10, ЛР-4 |
