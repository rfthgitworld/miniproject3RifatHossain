DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS category;
DROP TABLE IF EXISTS transactions;

CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
);

CREATE TABLE category (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    user_id INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES user (id)
);

CREATE TABLE transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    amount REAL NOT NULL,
    type TEXT CHECK(type IN ('income','expense')) NOT NULL,
    category_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    created_at TEXT NOT NULL DEFAULT (datetime('now')),
    note TEXT,
    FOREIGN KEY (category_id) REFERENCES category (id),
    FOREIGN KEY (user_id) REFERENCES user (id)
);

INSERT INTO category (name, user_id) VALUES
('Housing & Utilities', 1),
('Transportation', 1),
('Food & Dining', 1),
('Health & Wellness', 1),
('Personal & Lifestyle', 1),
('Education & Development', 1),
('Finance & Debt', 1),
('Work & Professional', 1),
('Travel & Vacation', 1),
('Miscellaneous / Other', 1);

