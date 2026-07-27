#!/usr/bin/env python3
"""
Учебный шаблон для ЛР-3: канонизация ФИО и простое сопоставление записей двух CRM.

Не является эталонным промышленным решением. Студент обязан:
- расширить правила под своё ТЗ;
- обработать «серую зону» (ручная проверка);
- объяснить выбор порогов на защите.

Запуск из корня репозитория:
  python resources/software/python-libs/lr3_record_matching_template.py
"""

from __future__ import annotations

import csv
import re
import unicodedata
from dataclasses import dataclass
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[2] / "datasets"
CRM_A = DATA_DIR / "crm_a_sample.csv"
CRM_B = DATA_DIR / "crm_b_sample.csv"


def canonicalize_name(value: str) -> str:
    """Грубая канонизация: нижний регистр, ё→е, убрать лишние пробелы и точки инициалов."""
    if not value:
        return ""
    text = unicodedata.normalize("NFKC", value).lower().replace("ё", "е")
    text = text.replace(".", " ")
    text = re.sub(r"[^a-zа-я0-9\s-]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def normalize_phone(value: str) -> str:
    digits = re.sub(r"\D", "", value or "")
    if digits.startswith("8") and len(digits) == 11:
        digits = "7" + digits[1:]
    return digits


@dataclass
class Record:
    source: str
    record_id: str
    name: str
    phone: str
    email: str

    @property
    def name_key(self) -> str:
        return canonicalize_name(self.name)

    @property
    def phone_key(self) -> str:
        return normalize_phone(self.phone)

    @property
    def email_key(self) -> str:
        return (self.email or "").strip().lower()


def load_crm_a(path: Path) -> list[Record]:
    rows: list[Record] = []
    with path.open(encoding="utf-8") as f:
        for row in csv.DictReader(f):
            rows.append(
                Record(
                    source="A",
                    record_id=row["crm_id"],
                    name=row["full_name"],
                    phone=row.get("phone", ""),
                    email=row.get("email", ""),
                )
            )
    return rows


def load_crm_b(path: Path) -> list[Record]:
    """Поля CRM B намеренно отличаются от CRM A (учебный schema mismatch)."""
    rows: list[Record] = []
    with path.open(encoding="utf-8") as f:
        for row in csv.DictReader(f):
            rows.append(
                Record(
                    source="B",
                    record_id=row["crm_id"],
                    name=row["client_name"],
                    phone=row.get("mobile", ""),
                    email=row.get("mail", ""),
                )
            )
    return rows


def match_score(left: Record, right: Record) -> float:
    """Простая эвристика: телефон / email / имя. Студент заменяет на свои правила."""
    score = 0.0
    if left.phone_key and left.phone_key == right.phone_key:
        score += 0.5
    if left.email_key and left.email_key == right.email_key:
        score += 0.3
    if left.name_key and left.name_key == right.name_key:
        score += 0.2
    elif left.name_key and right.name_key and (
        left.name_key in right.name_key or right.name_key in left.name_key
    ):
        score += 0.1
    return score


def main() -> None:
    left = load_crm_a(CRM_A)
    right = load_crm_b(CRM_B)

    print("canonical name examples:")
    for sample in ("Иванов И. И.", "Иванов Иван Иванович", "John Smith"):
        print(f"  {sample!r} -> {canonicalize_name(sample)!r}")

    print("\ncandidate matches (score >= 0.4):")
    for a in left:
        for b in right:
            s = match_score(a, b)
            if s >= 0.4:
                zone = "auto" if s >= 0.7 else "manual-review"
                print(f"  {a.record_id} ↔ {b.record_id}  score={s:.2f}  zone={zone}")


if __name__ == "__main__":
    main()
