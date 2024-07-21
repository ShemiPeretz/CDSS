from dataclasses import dataclass
from typing import Optional

from enums.HematologicalState import HematologicalState
from enums.HemoglobinState import HemoglobinState
from enums.SystemicToxicity import SystematicToxicity


@dataclass
class PatientState:
    state_id: Optional[int]
    test_id: int
    patient_id: int
    last_state_id: int
    hemoglobin_state: HemoglobinState
    hematological_state: HematologicalState
    systematic_toxicity: SystematicToxicity
