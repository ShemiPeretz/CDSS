from enum import Enum


class AllergicState(Enum):
    NONE = "None"
    EDEMA = "Edema"
    BRONCHOSPASM = "Bronchospasm"
    SEVERE_BRONCHOSPASM = "Severe-Bronchospasm"
    ANAPHYLACTIC_SHOCK = "Anaphylactic-Shock"
