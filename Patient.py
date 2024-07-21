from dataclasses import dataclass
from typing import Optional

from enums.Gender import Gender


@dataclass
class Patient:
    patient_id: Optional[int]
    first_name: str
    last_name: str
    gender: Gender

    def __init__(self, first_name: str, last_name: str , gender: Gender):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender


