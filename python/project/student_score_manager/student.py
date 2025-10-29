from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Dict


@dataclass
class Student:
    name: str
    scores: List[float] = field(default_factory=list)

    # ---------- score ops ----------
    def add_score(self, value: float) -> None:
        self._validate_score(value)
        self.scores.append(value)

    def edit_score(self, index: int, new_value: float) -> None:
        if index < 0 or index >= len(self.scores):
            raise IndexError("Index nilai tidak valid")
        self._validate_score(new_value)
        self.scores[index] = new_value

    def delete_score(self, index: int) -> None:
        if index < 0 or index >= len(self.scores):
            raise IndexError("Index nilai tidak valid")
        self.scores.pop(index)

    # ---------- derived metrics ----------
    def average(self) -> float:
        return sum(self.scores) / len(self.scores) if self.scores else 0.0

    def grade(self) -> str:
        avg = self.average()
        if avg >= 85:
            return "A"
        elif avg >= 70:
            return "B"
        elif avg >= 60:
            return "C"
        elif avg >= 50:
            return "D"
        else:
            return "E"

    # ---------- utils ----------
    def info_line(self) -> str:
        scores_str = "[" + ", ".join(f"{s:.2f}" for s in self.scores) + "]"
        return f"{self.name} | scores={scores_str} | avg={self.average():.2f} | grade={self.grade()}"

    def to_dict(self) -> Dict:
        return {"name": self.name, "scores": self.scores}

    @staticmethod
    def from_dict(d: Dict) -> "Student":
        return Student(name=d["name"], scores=[float(x) for x in d.get("scores", [])])

    @staticmethod
    def _validate_score(value: float) -> None:
        try:
            v = float(value)
        except Exception as e:
            raise ValueError("Nilai harus berupa angka") from e
        if v < 0 or v > 100:
            raise ValueError("Score harus 0..100")