CREATE TABLE IF NOT EXISTS p_users (
    id INTEGER PRIMARY KEY,
    chat_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    username VARCHAR(20) NOT NULL,
    modified_at DATETIME,
    CONSTRAINT unq UNIQUE (chat_id, user_id)
);
CREATE TABLE IF NOT EXISTS p_stat (
  id INTEGER PRIMARY KEY,
  chat_id INTEGER NOT NULL,
  user_id INTEGER NOT NULL,
  username VARCHAR(20) NOT NULL,
  choice_date DATETIME NOT NULL
);
CREATE TABLE  IF NOT EXISTS p
(
    id INTEGER PRIMARY KEY,
    chat_id INTEGER NOT NULL UNIQUE,
    last_choice VARCHAR(20),
    scheduled BOOLEAN NOT NULL DEFAULT FALSE,
    modified_at DATETIME
);