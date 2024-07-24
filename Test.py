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
    test_type: str
    unit: str
    test_value: str
    hemoglobin_level: Optional[float]
    wbc_level: Optional[float]
    fever: Optional[float]
    chills: Optional[Chills]
    skin_look: Optional[SkinLook]
    allergic_state: Optional[AllergicState]
