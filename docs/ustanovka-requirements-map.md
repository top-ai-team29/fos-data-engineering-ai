# Соответствие требованиям установочной / оценочной рамки ДПО

Документ закрывает критерий чек-листа v2.0: *«Репозиторий соответствует требованиям установочной сессии данного ДПО»*.

**Исходники требований, доступные команде:**
- чек-лист оценки Git-репозитория с ФОС, версия 2.0 (файл `Чек-лист-версия2.0`, шкала 1–10);
- книга КРМ 3.0 в репозитории: [data/krm-v3.0.xlsx](../data/krm-v3.0.xlsx);
- типовая структура ФОС (РПД → модель измерения → КИМ → МУ → ресурсы).

Файл презентации `task_st.pdf` в рабочей копии **не обнаружен**. При появлении оригинала его следует положить в [`other/task_st.pdf`](../other/) и дополнить колонку «Слайд / пункт task_st» ниже; до этого опора — чек-лист v2.0 как официальная оценочная рамка той же программы ДПО.

Карта навигации по Markdown: [navigation-map.md](navigation-map.md).

## 1. Обязательные элементы ФОС (структура репозитория)

| Требование рамки | Где в репозитории | Статус |
|---|---|---|
| Рабочая программа (паспорт, часы, РО, тематический план) | [docs/rpd.md](rpd.md) | Есть (144 ч / 4 ЗЕ) |
| Результаты обучения и связь с КИУ | [docs/outcomes-kim-map.md](outcomes-kim-map.md) | Есть |
| Привязка к КРМ без подмены названий | [docs/krm-traceability.md](krm-traceability.md), [data/README.md](../data/README.md) | Есть |
| Модель измерения в корневом README | [README.md](../README.md) §2 | Есть |
| Детализация модели / БРС / шкала | [measurement-model.md](measurement-model.md), [points-rating-system.md](points-rating-system.md), [final-grade-scale.md](final-grade-scale.md) | Есть |
| КИМ по модулям | [M01](../M01-module/README.md)–[M10](../M10-module/README.md) | Есть |
| Лабораторные работы + методички | [Project/](../Project/README.md), [methodical-guidelines ЛР](../Project/laboratories/methodical-guidelines/README.md) | Есть (68 ч) |
| Банки тестов / открытых / экзамена | [test-banks](../resources/test-banks/README.md), [problem-banks](../resources/problem-banks/README.md) | Есть |
| Разделение ключей student / teacher | [test-banks/teacher](../resources/test-banks/teacher/), [problem-banks/teacher](../resources/problem-banks/teacher/) | Есть |
| МУ для обучающихся | [methodical-guidelines/students](../methodical-guidelines/students/README.md) | Есть |
| МУ для преподавателей | [teachers-assessment](../methodical-guidelines/teachers-assessment/README.md), [teachers-resources](../methodical-guidelines/teachers-resources/README.md) | Есть |
| Ресурсы, лицензии, команда | [resources/](../resources/README.md), [LICENSE.md](../LICENSE.md), [team/](../team/README.md) | Есть |
| Воспроизводимый учебный код | [lr3_record_matching_template.py](../resources/software/python-libs/lr3_record_matching_template.py) | Есть |
| Реестр источников | [other/source-register.md](../other/source-register.md) | Есть |

## 2. Сопоставление с критериями чек-листа v2.0

| № | Критерий чек-листа | Доказательство в репозитории |
|---:|---|---|
| 1 | Оригинальность дисциплины | DE-for-AI: RAG, Feature Store, CRM matching, IoT Lake — [README](../README.md), [rpd](rpd.md) |
| 2 | Актуальность | Lakehouse/Mesh/облако/DataOps — модули M04–M10 |
| 3 | Релевантность ИИ/ML | РО-1…9, пререквизит ML, ИИ-потребители данных |
| 4 | Измеримость | [measurement-model](measurement-model.md), [krm-traceability](krm-traceability.md), уровни Б/С/П |
| 5 | Востребованность | Ядро Data Engineer, 09.03.03, блок BD КРМ |
| 6 | Ресурсоёмкость | Синтетика + опциональный PaaS; stdlib для ЛР-3 |
| 7 | Покрытие РО | [outcomes-kim-map](outcomes-kim-map.md) + банки с тегами РО/BD |
| 8 | Модель измерения | README §2 + docs |
| 9 | Разнообразие КИМ | тесты, открытые, рубеж, 4 ЛР, защита, экзамен |
| 10 | Тиражируемость | шаблон структуры ФОС, CC BY, поля «принимающая ОО» |
| 11 | Практико-ориентированность | ЛР с артефактами C4/BPMN/ETL/matching/Lake |
| 12 | Оригинальность данных | синтетические CRM/IoT в [datasets](../resources/datasets/README.md) |
| 13 | Оригинальность кода | шаблон ЛР-3 + [golden stdout](../resources/benchmarks/lr3_template_expected_stdout.txt) |
| 14 | Трудоёмкость подготовки | полный комплект ФОС (см. §1) |
| 15 | Навигация | [README](../README.md), [navigation-map](navigation-map.md) |
| 16 | Документированность КИМ/ресурсов | карточки ресурсов, банки, МУ |
| 17 | МУ преподавателям | assessment + resources + teacher-банки |
| 18 | МУ обучающимся | students + полные методички ЛР |
| 19 | Законченный продукт | LICENSE, team, CONTRIBUTING, runnable LR-3 |
| 20 | Соответствие установочной рамке | **этот документ** |
| 21 | Пригодность для внедрения | адаптационные поля РПД, CC BY 4.0 |

## 3. Как обновить при появлении `task_st.pdf`

1. Разместить файл: `other/task_st.pdf`.
2. Для каждого слайда/пункта презентации добавить строку в таблицу §1 или отдельную таблицу «Слайд → артефакт».
3. Указать дату сверки в этом файле.
