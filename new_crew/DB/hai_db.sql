-- Users Table
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE
);

-- User Emails Table
CREATE TABLE IF NOT EXISTS user_emails (
    email_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL UNIQUE,
    email TEXT NOT NULL UNIQUE,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

-- Initial Interviews Table
CREATE TABLE IF NOT EXISTS initial_interviews (
    interview_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    overall_feeling TEXT,
    sleep_quality TEXT,
    exercise_routine TEXT,
    mental_health TEXT,
    stress_level INTEGER,
    health_goals TEXT,
    custom_condition TEXT,
    interview_date DATE NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

-- Daily Check-Ins Table
CREATE TABLE IF NOT EXISTS daily_check_ins (
    check_in_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    date DATE NOT NULL,
    sleep_duration REAL,
    exercise_duration REAL,
    mood TEXT CHECK(mood IN ('Happy', 'Sad', 'Depressed', 'Anxious', 'Neutral', 'Stressed', 'Excited')),
    stress_level INTEGER,
    additional_notes TEXT,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

-- Health Conditions Table
CREATE TABLE IF NOT EXISTS health_conditions (
    condition_id INTEGER PRIMARY KEY AUTOINCREMENT,
    condition_name TEXT NOT NULL,
    description TEXT
);

-- Common Foods Table
CREATE TABLE IF NOT EXISTS common_foods (
    food_id INTEGER PRIMARY KEY AUTOINCREMENT,
    food_name TEXT NOT NULL,
    category TEXT,
    nutritional_info TEXT
);

-- User Conditions Table
CREATE TABLE IF NOT EXISTS user_conditions (
    user_condition_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    condition_id INTEGER NOT NULL,
    notes TEXT,
    date_noted DATE,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (condition_id) REFERENCES health_conditions(condition_id)
);

-- User Food Intake Table
CREATE TABLE IF NOT EXISTS user_food_intake (
    food_intake_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    food_id INTEGER NOT NULL,
    meal_type TEXT CHECK(meal_type IN ('Breakfast', 'Lunch', 'Dinner', 'Snack')),
    intake_date DATE NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (food_id) REFERENCES common_foods(food_id)
);
