CREATE TABLE kb_hemoglobin_state (
    id INT PRIMARY KEY AUTO_INCREMENT,
    gender ENUM('Male', 'Female'),
    min_level FLOAT,
    max_level FLOAT,
    hemoglobin_state ENUM("Severe-Anemia", "Moderate-Anemia", "Mild-Anemia", "Normal-Hemoglobin", "Polyhemia", "Polycytemia")
);

-- Insert data for females
INSERT INTO kb_hemoglobin_state (gender, min_level, max_level, hemoglobin_state) VALUES
('Female', 0, 7, 'Severe-Anemia'),
('Female', 8, 9, 'Moderate-Anemia'),
('Female', 10, 11, 'Mild-Anemia'),
('Female', 12, 13, 'Normal-Hemoglobin'),
('Female', 14, 999, 'Polycytemia');

-- Insert data for males
INSERT INTO kb_hemoglobin_state (gender, min_level, max_level, hemoglobin_state) VALUES
('Male', 0, 8, 'Severe-Anemia'),
('Male', 9, 10, 'Moderate-Anemia'),
('Male', 11, 12, 'Mild-Anemia'),
('Male', 13, 15, 'Normal-Hemoglobin'),
('Male', 16, 999, 'Polyhemia');