CREATE TABLE kb_systemic_toxicity (
    id INT PRIMARY KEY AUTO_INCREMENT,
    min_fever FLOAT,
    max_fever FLOAT,
    chills ENUM("None", "Rigor", "Shaking"),
    skin_look ENUM("Erythema", "Vesiculation", "Desquamation", "Exfoliation"),
    allergic_state ENUM("Edema", "Bronchospasm", "Severe-Bronchospasm", "Anaphylactic-Shock"),
    systemic_toxicity ENUM("Grade 1", "Grade 2", "Grade 3", "Grade 4")
);

-- Insert data for males (as before)
INSERT INTO kb_systemic_toxicity  
(min_fever, max_fever, chills, skin_look, allergic_state, systemic_toxicity) VALUES
(0, 38.4, "None", "Erythema", 'Edema', "Grade 1"),
(38.5, 39.9, "Shaking", "Vesiculation", 'Bronchospasm', "Grade 2"),
(40.0, 40.9, "Rigor", "Exfoliation", 'Anaphylactic-Shock', "Grade 4"),
(41.0, 999, "Rigor", "Desquamation", 'Severe-Bronchospasm', "Grade 3");