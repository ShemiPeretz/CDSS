from dataclasses import dataclass
from datetime import date
from typing import Optional

from enums.AllergicState import AllergicState
from enums.Chills import Chills
from enums.SkinLook import SkinLook


@dataclass
class Test:
    test_id: Optional[int]
    patient_id: int
    transaction_time: date
    valid_start_time: date
    loinc_num: str
    hemoglobin_level: float
    wbc_level: float
    fever: float
    chills: Chills
    skin_look: SkinLook
    allergic_state: AllergicState
