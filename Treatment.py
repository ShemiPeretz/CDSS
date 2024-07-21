from dataclasses import dataclass
from typing import Optional

from enums.HematologicalState import HematologicalState
from enums.HemoglobinState import HemoglobinState
from enums.SystemicToxicity import SystematicToxicity


@dataclass
class Treatment:
    treatment_id: Optional[int]
    hemoglobin_state: HemoglobinState
    hematological_state: HematologicalState
    systematic_toxicity: SystematicToxicity
    recommended_treatment: str