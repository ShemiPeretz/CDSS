CREATE TABLE kb_hematological_state (
    id INT PRIMARY KEY AUTO_INCREMENT,
    gender ENUM('Male', 'Female'),
    min_hemoglobin FLOAT,
    max_hemoglobin FLOAT,
    min_wbc FLOAT,
    max_wbc FLOAT,
    hematological_state VARCHAR(50)
);

-- Insert data for males (as before)
INSERT INTO kb_hematological_state  
(gender, min_hemoglobin, max_hemoglobin, min_wbc, max_wbc, hematological_state) VALUES
('Male', 0, 13, 0, 4000, 'Pancytopenia'),
('Male', 13, 16, 0, 4000, 'Leukopenia'),
('Male', 16, 999, 0, 4000, 'Suspected Polycytemia Vera'),
('Male', 0, 13, 4000, 10000, 'Anemia'),
('Male', 13, 16, 4000, 10000, 'Normal'),
('Male', 16, 999, 4000, 10000, 'Polyhemia'),
('Male', 0, 13, 10000, 999999, 'Suspected Leukemia'),
('Male', 13, 16, 10000, 999999, 'Leukemoid reaction'),
('Male', 16, 999, 10000, 999999, 'Suspected Polycytemia Vera');

-- Insert data for females (based on the new table)
INSERT INTO kb_hematological_state  
(gender, min_hemoglobin, max_hemoglobin, min_wbc, max_wbc, hematological_state) VALUES
('Female', 0, 12, 0, 4000, 'Pancytopenia'),
('Female', 12, 14, 0, 4000, 'Leukopenia'),
('Female', 14, 999, 0, 4000, 'Suspected Polycytemia Vera'),
('Female', 0, 12, 4000, 10000, 'Anemia'),
('Female', 12, 14, 4000, 10000, 'Normal'),
('Female', 14, 999, 4000, 10000, 'Polyhemia'),
('Female', 0, 12, 10000, 999999, 'Suspected Leukemia'),
('Female', 12, 14, 10000, 999999, 'Leukemoid reaction'),
('Female', 14, 999, 10000, 999999, 'Suspected Polycytemia Vera');