CREATE DATABASE clinical_dss;

USE clinical_dss;

CREATE TABLE patients (
    patient_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    gender ENUM('Male', 'Female')
);

CREATE TABLE tests_to_lionc_num (
	test_type TEXT,
    LIONC_NUM TEXT
);

CREATE TABLE tests (
    test_id INT PRIMARY KEY AUTO_INCREMENT,
    patient_id INT,
    transaction_time DATE,
    valid_start_time DATE,
    valid_end_time DATE,
    LOINC_NUM TEXT,
    hemoglobin_level FLOAT,
    wbc_level FLOAT,
    fever FLOAT,
    chills ENUM("None", "Rigor", "Shaking"),
    skin_look ENUM("Erythema", "Vesiculation", "Desquamation", "Exfoliation"),
    allergic_state ENUM("Edema", "Bronchospasm", "Severe-Bronchospasm", "Anaphylactic-Shock"),
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id)
);

CREATE TABLE patient_states (
    state_id INT PRIMARY KEY AUTO_INCREMENT,
    test_id INT,
    patient_id INT,
    last_state_id INT,
    hemoglobin_state ENUM("Severe-Anemia", "Moderate-Anemia", "Mild-Anemia", "Normal-Hemoglobin", "Polyhemia", "Polycytemia"),
    hematological_state ENUM("Normal", "Polyhemia", "Pancytopenia", "Anemia", "Suspected-Leukemia", "Leukemoid-reaction", "Suspected-Polycytemia-Vera", "Leukopenia"),
    systemic_toxicity ENUM("Grade 1", "Grade 2", "Grade 3", "Grade 4"),
    FOREIGN KEY (test_id) REFERENCES tests(test_id)
);

CREATE TABLE treatments (
    treatment_id INT PRIMARY KEY AUTO_INCREMENT,
    hemoglobin_state ENUM("Severe-Anemia", "Moderate-Anemia", "Mild-Anemia", "Normal-Hemoglobin", "Polyhemia", "Polycytemia"),
    hematological_state ENUM("Normal", "Polyhemia", "Pancytopenia", "Anemia", "Suspected-Leukemia", "Leukemoid-reaction", "Suspected-Polycytemia-Vera", "Leukopenia"),
    systemic_toxicity ENUM("Grade 1", "Grade 2", "Grade 3", "Grade 4"),
    recommended_treatment TEXT
);
