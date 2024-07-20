from dataclasses import dataclass
from datetime import date
from typing import Optional

from enums.AllergicState import AllergicState
from enums.SkinLook import SkinLook


@dataclass
class Test:
    test_id: Optional[int]
    patient_id: int
    test_date: date
    hemoglobin_level: float
    wbc_level: float
    fever: bool
    chills: bool
    skin_look: SkinLook
    allergic_state: AllergicState