from KnowledgeBase import KnowledgeBase
from Test import Test
from Treatment import Treatment


class DSSEngine:
    def __init__(self, knowledge_base: KnowledgeBase):
        self.knowledge_base = knowledge_base

    def process_test(self, test: Test) -> Treatment:
        patient_state = self.knowledge_base.determine_patient_state(test)
        return self.knowledge_base.recommend_treatment(patient_state)
