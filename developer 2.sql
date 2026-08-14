USE examination;


-- =========================================
-- 1. QUESTIONS
-- =========================================

CREATE TABLE IF NOT EXISTS questions (
    id INT AUTO_INCREMENT PRIMARY KEY,

    question TEXT NOT NULL,

    option_a VARCHAR(500) NOT NULL,
    option_b VARCHAR(500) NOT NULL,
    option_c VARCHAR(500) NOT NULL,
    option_d VARCHAR(500) NOT NULL,

    correct_answer CHAR(1) NOT NULL,

    explanation TEXT,

    difficulty VARCHAR(20) NOT NULL,

    question_type VARCHAR(50) DEFAULT 'MCQ',

    source_file VARCHAR(500),

    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);


-- =========================================
-- 2. TESTS
-- =========================================

CREATE TABLE IF NOT EXISTS tests (
    id INT AUTO_INCREMENT PRIMARY KEY,

    test_name VARCHAR(255) NOT NULL,

    student_email VARCHAR(100),

    number_of_questions INT NOT NULL,

    difficulty VARCHAR(20),

    question_type VARCHAR(50) DEFAULT 'MCQ',

    time_limit INT,

    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);


-- =========================================
-- 3. TEST QUESTIONS
-- =========================================

CREATE TABLE IF NOT EXISTS test_questions (
    id INT AUTO_INCREMENT PRIMARY KEY,

    test_id INT NOT NULL,

    question_id INT NOT NULL,

    question_order INT NOT NULL,

    FOREIGN KEY (test_id)
        REFERENCES tests(id)
        ON DELETE CASCADE,

    FOREIGN KEY (question_id)
        REFERENCES questions(id)
        ON DELETE CASCADE,

    UNIQUE (test_id, question_id)
);


-- =========================================
-- 4. STUDENT ANSWERS
-- =========================================

CREATE TABLE IF NOT EXISTS student_answers (
    id INT AUTO_INCREMENT PRIMARY KEY,

    test_id INT NOT NULL,

    question_id INT NOT NULL,

    student_email VARCHAR(100),

    selected_answer CHAR(1),

    is_correct BOOLEAN,

    answered_at DATETIME DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (test_id)
        REFERENCES tests(id)
        ON DELETE CASCADE,

    FOREIGN KEY (question_id)
        REFERENCES questions(id)
        ON DELETE CASCADE
);


-- =========================================
-- 5. RESULTS
-- =========================================

CREATE TABLE IF NOT EXISTS results (
    id INT AUTO_INCREMENT PRIMARY KEY,

    test_id INT NOT NULL,

    student_email VARCHAR(100),

    total_questions INT NOT NULL,

    correct_answers INT NOT NULL,

    incorrect_answers INT NOT NULL,

    unattempted INT NOT NULL,

    score INT NOT NULL,

    percentage DECIMAL(5,2) NOT NULL,

    completed_at DATETIME DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (test_id)
        REFERENCES tests(id)
        ON DELETE CASCADE
);


-- =========================================
-- CHECK ALL TABLES
-- =========================================

SHOW TABLES;