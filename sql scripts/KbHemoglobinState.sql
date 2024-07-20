CREATE TABLE kb_hemoglobin_state (
    id INT PRIMARY KEY AUTO_INCREMENT,
    gender ENUM('Male', 'Female'),
    min_level FLOAT,
    max_level FLOAT,
    hemoglobin_state VARCHAR(50)
);

-- Insert data for females
INSERT INTO kb_hemoglobin_state (gender, min_level, max_level, hemoglobin_state) VALUES
('Female', 0, 8, 'Severe Anemia'),
('Female', 8, 10, 'Moderate Anemia'),
('Female', 10, 12, 'Mild Anemia'),
('Female', 12, 14, 'Normal Hemoglobin'),
('Female', 14, 999, 'Polycytemia');

-- Insert data for males
INSERT INTO kb_hemoglobin_statekb_hemoglobin_state (gender, min_level, max_level, hemoglobin_state) VALUES
('Male', 0, 9, 'Severe Anemia'),
('Male', 9, 11, 'Moderate Anemia'),
('Male', 11, 13, 'Mild Anemia'),
('Male', 13, 16, 'Normal Hemoglobin'),
('Male', 16, 999, 'Polyhemia');