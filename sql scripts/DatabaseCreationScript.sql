CREATE DATABASE clinical_dss;

USE clinical_dss;

CREATE TABLE patients (
    patient_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    date_of_birth DATE,
    gender ENUM('Male', 'Female', 'Other')
);

CREATE TABLE tests (
    test_id INT PRIMARY KEY AUTO_INCREMENT,
    patient_id INT,
    test_date DATE,
    hemoglobin_level FLOAT,
    wbc_level FLOAT,
    fever BOOLEAN,
    chills BOOLEAN,
    skin_look ENUM('Normal', 'Pale', 'Flushed', 'Jaundiced'),
    allergic_state ENUM('None', 'Mild', 'Moderate', 'Severe'),
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id)
);

CREATE TABLE patient_states (
    state_id INT PRIMARY KEY AUTO_INCREMENT,
    test_id INT,
    hemoglobin_state ENUM('Low', 'Normal', 'High'),
    hematological_state ENUM('Normal', 'Abnormal'),
    systematic_toxicity ENUM('None', 'Mild', 'Moderate', 'Severe'),
    FOREIGN KEY (test_id) REFERENCES tests(test_id)
);

CREATE TABLE treatments (
    treatment_id INT PRIMARY KEY AUTO_INCREMENT,
    hemoglobin_state ENUM('Low', 'Normal', 'High'),
    hematological_state ENUM('Normal', 'Abnormal'),
    systematic_toxicity ENUM('None', 'Mild', 'Moderate', 'Severe'),
    recommended_treatment TEXT
);
