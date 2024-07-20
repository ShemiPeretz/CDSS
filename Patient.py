from dataclasses import dataclass
from typing import Optional

from enums.Gender import Gender


@dataclass
class Patient:
    patient_id: Optional[int]
    name: str
    age: int
    gender: Gender
