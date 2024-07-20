from typing import List

import mysql.connector
from mysql.connector import Error

from Patient import Patient
from PatientState import PatientState
from Test import Test
from Treatment import Treatment


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
        # Implement method to add patient to database
        pass

    def add_test(self, test: Test):
        # Implement method to add test to database
        pass

    def add_patient_state(self, patient_state: PatientState):
        # Implement method to add patient state to database
        pass

    def add_treatment(self, treatment: Treatment):
        # Implement method to add treatment to database
        pass

    def get_patient(self, patient_id: int) -> Patient:
        # Implement method to retrieve patient from database
        pass

    def get_tests(self, patient_id: int) -> List[Test]:
        # Implement method to retrieve tests for a patient
        pass

    def get_patient_state(self, test_id: int) -> PatientState:
        # Implement method to retrieve patient state for a test
        pass

    def get_recommended_treatment(self, patient_state: PatientState) -> Treatment:
        # Implement method to retrieve recommended treatment based on patient state
        pass
