from typing import List

import mysql.connector
from mysql.connector import Error

from Patient import Patient
from PatientState import PatientState
from Test import Test
from Treatment import Treatment
from enums import SystemicToxicity
from enums.Gender import Gender
from enums.HematologicalState import HematologicalState
from enums.HemoglobinState import HemoglobinState


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

    def add_patient(self, patient: Patient):
        query = """INSERT INTO patients (first_name, last_name, gender) 
                   VALUES (%s, %s, %s)"""
        params = (patient.first_name, patient.last_name, patient.gender.value)
        self.execute_query(query, params)


    def add_test(self, test: Test):
        # Implement method to add test to database
        pass

    def add_patient_state(self, patient_state: PatientState):
        query = """INSERT INTO patient_states (test_id, last_state_id, patient_id, hemoglobin_state,
         hematological_state, systemic_toxicity) 
                   VALUES (%s, %s, %s, %s, %s, %s)"""
        params = (patient_state.test_id, patient_state.last_state_id, patient_state.patient_id,
                  patient_state.hemoglobin_state, patient_state.hematological_state, patient_state.systematic_toxicity)
        self.execute_query(query, params)

    def add_treatment(self, treatment: Treatment):
        # Implement method to add treatment to database
        pass

    def get_patient(self, patient_id: int) -> Patient:
        query = "SELECT * FROM patients WHERE patient_id = %s"
        result = self.fetch_one(query, (patient_id,))
        if result:
            return Patient(
                patient_id=result[0],
                name=result[1],
                date_of_birth=result[2],
                gender=Gender(result[3])
            )
        return None

    def get_test(self, patient_id: int) -> List[Test]:
        query = "SELECT * FROM patients WHERE patient_id = %s"
        result = self.fetch_one(query, (patient_id,))
        if result:
            return Patient(
                patient_id=result[0],
                name=result[1],
                date_of_birth=result[2],
                gender=Gender(result[3])
            )
        return None

    def get_patient_state(self, patient_id: int) -> PatientState:
        query = "SELECT * FROM patient_states WHERE patient_id = %s"
        result = self.fetch_one(query, (patient_id,))
        if result:
            return PatientState(
                state_id = result[0],
                test_id = result[1],
                patient_id = result[2],
                last_state_id = result[3],
                hemoglobin_state = result[4],
                hematological_state = result[5],
                systematic_toxicity = result[6]
            )
        return None

    def get_recommended_treatment(self, patient_state: PatientState) -> Treatment:
        # Implement method to retrieve recommended treatment based on patient state
        pass

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

    def get_systemic_toxicity(self) -> SystemicToxicity:
        pass
