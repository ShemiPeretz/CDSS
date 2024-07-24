import mysql.connector
from mysql.connector import Error

from LoincManager import LOINCManager
from PatientState import PatientState
from enums import SystemicToxicity
from enums.AllergicState import AllergicState
from enums.Chills import Chills
from enums.HematologicalState import HematologicalState
from enums.HemoglobinState import HemoglobinState
from enums.SkinLook import SkinLook


class Database:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
        self.cursor = None

        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )

            if self.connection.is_connected():
                print("Successfully connected to the database")
                self.cursor = self.connection.cursor()
            else:
                print("Failed to connect to the database")

        except Error as e:
            print(f"Error connecting to the database: {e}")

    def __del__(self):
        if self.connection and self.connection.is_connected():
            self.cursor.close()
            self.connection.close()
            print("Database connection closed")

    def execute_query(self, query, params=None):
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            self.connection.commit()
            print("Query executed successfully")
        except Error as e:
            print(f"Error executing query: {e}")

    def fetch_all(self, query, params=None):
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            return self.cursor.fetchall()
        except Error as e:
            print(f"Error fetching data: {e}")
            return None

    def fetch_one(self, query, params=None):
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            return self.cursor.fetchone()
        except Error as e:
            print(f"Error fetching data: {e}")
            return None

    # Patients table methods ###########################################################################################
    def add_patient(self, patient):
        query = "INSERT INTO patients (first_name, last_name, gender) VALUES (%s, %s, %s)"
        params = (patient.first_name, patient.last_name, patient.gender.value)
        return self.execute_query(query, params)

    def get_patient_by_id(self, patient_id):
        query = "SELECT * FROM patients WHERE patient_id = %s"
        return self.fetch_one(query, (patient_id,))

    def get_patient_by_name(self, first_name, last_name):
        query = "SELECT * FROM patients WHERE first_name = %s AND last_name = %s"
        params = (first_name, last_name)
        return self.fetch_one(query, params)

    def delete_patient(self, patient_id):
        query = "DELETE FROM patients WHERE patient_id = %s"
        return self.execute_query(query, (patient_id,))

    # Tests_to_loinc_num table methods #################################################################################
    def add_test_to_loinc(self, loinc_num):
        test_type = LOINCManager.search_test_by_loinc_code(loinc_num)
        query = "INSERT INTO tests_to_loinc_num (test_type, LOINC_NUM) VALUES (%s, %s)"
        params = (test_type, loinc_num)
        return self.execute_query(query, params)

    def get_loinc_num_by_test_type(self, test_type):
        query = "SELECT LOINC_NUM FROM tests_to_loinc_num WHERE test_type = %s"
        return self.fetch_one(query, (test_type,))

    def get_test_type_by_loinc(self, loinc_num):
        query = "SELECT test_type FROM tests_to_loinc_num WHERE LOINC_NUM = %s"
        return self.fetch_one(query, (loinc_num,))

    # Tests table methods ##############################################################################################
    def add_test(self, test):
        query = """
        INSERT INTO tests (patient_id, transaction_time, valid_start_time, 
        LOINC_NUM, hemoglobin_level, wbc_level, fever, chills, skin_look, allergic_state) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        params = (test.patient_id, test.transaction_time, test.valid_start_time,
                  test.LOINC_NUM, test.hemoglobin_level, test.wbc_level, test.fever, test.chills.value,
                  test.skin_look.value, test.allergic_state.value)
        return self.execute_query(query, params)

    def get_test_by_id(self, test_id):
        query = "SELECT * FROM tests WHERE test_id = %s"
        return self.fetch_one(query, (test_id,))
    
    def get_tests_by_patient_id(self, patient_id):
        query = "SELECT * FROM tests WHERE patient_id = %s"
        return self.fetch_all(query, (patient_id,))

    def delete_test(self, test_id):
        query = "DELETE FROM tests WHERE test_id = %s"
        return self.execute_query(query, (test_id,))

    # Patient_states table methods #####################################################################################
    def add_patient_state(self, patient_state):
        query = """
        INSERT INTO patient_states (test_id, patient_id, last_state_id, hemoglobin_state, 
        hematological_state, systemic_toxicity) 
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        params = (patient_state.test_id, patient_state.patient_id, patient_state.last_state_id,
                  patient_state.hemoglobin_state.value, patient_state.hematological_state.value,
                  patient_state.systemic_toxicity.value)
        return self.execute_query(query, params)

    def get_latest_patient_state_by_patient_id(self, patient_id):
        query = """
        SELECT * FROM patient_states 
        WHERE patient_id = %s 
        ORDER BY valid_start_time DESC, state_id DESC 
        LIMIT 1
        """
        return self.fetch_one(query, (patient_id,))

    def get_all_patient_states_by_patient_id(self, patient_id):
        query = "SELECT * FROM patient_states WHERE patient_id = %s"
        return self.fetch_all(query, (patient_id,))

    def delete_patient_state(self, state_id):
        query = "DELETE FROM patient_states WHERE state_id = %s"
        return self.execute_query(query, (state_id,))

    # Treatments table methods #########################################################################################
    def add_treatment(self, treatment):
        query = """
        INSERT INTO treatments (hemoglobin_state, hematological_state, systemic_toxicity, recommended_treatment) 
        VALUES (%s, %s, %s, %s)
        """
        params = (treatment.hemoglobin_state.value, treatment.hematological_state.value,
                  treatment.systemic_toxicity.value, treatment.recommended_treatment)
        return self.execute_query(query, params)

    def get_treatment(self, treatment_id):
        query = "SELECT * FROM treatments WHERE treatment_id = %s"
        return self.fetch_one(query, (treatment_id,))

    def get_treatment_by_states(self, hemoglobin_state: HemoglobinState, hematological_state: HematologicalState,
                                systemic_toxicity: SystemicToxicity):
        query = "SELECT * FROM treatments WHERE hemoglobin_state = %s AND hematological_state = %s AND systemic_toxicity = %s"
        return self.fetch_one(query, (hemoglobin_state.value, hematological_state.value, systemic_toxicity.value))

    def delete_treatment(self, treatment_id):
        query = "DELETE FROM treatments WHERE treatment_id = %s"
        return self.execute_query(query, (treatment_id,))

    # KB RELATED METHODS ###############################################################################################
    def get_hemoglobin_state(self, hemoglobin_level: float, gender: str) -> HemoglobinState:
        query = """
        SELECT hemoglobin_state 
        FROM kb_hemoglobin_state 
        WHERE gender = %s AND %s BETWEEN min_level AND max_level
        """
        result = self.fetch_one(query, (gender, hemoglobin_level))
        return result[0] if result else None

    def get_hematological_state(self, hemoglobin_level: float, wbc_level: float, gender: str) -> HematologicalState:
        query = """
        SELECT hematological_state 
        FROM kb_hematological_state 
        WHERE gender = %s 
        AND %s BETWEEN min_hemoglobin AND max_hemoglobin
        AND %s BETWEEN min_wbc AND max_wbc
        """
        result = self.fetch_one(query, (gender, hemoglobin_level, wbc_level))
        return result[0] if result else None

    def get_systemic_toxicity(self, fever: float, chills: Chills, skin_look: SkinLook, allergic_state: AllergicState,
                              ) -> SystemicToxicity:
        query = """
        SELECT systemic_toxicity
        FROM kb_systemic_toxicity 
        WHERE %s BETWEEN min_fever AND max_fever
        AND chills = %s
        AND skin_look = %s
        AND allergic_state = %s
        """
        result = self.fetch_one(query, (fever, chills.value, skin_look.value, allergic_state.value))
        return result[0] if result else None

    def get_recommended_treatment(self, patient_state: PatientState):
        return self.get_treatment_by_states(patient_state.hemoglobin_state, patient_state.hematological_state,
                                     patient_state.systematic_toxicity)
