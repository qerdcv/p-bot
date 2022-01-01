UPDATE p
SET
    modified_at=?,
    last_choice=?,
    user_id=?
WHERE
    chat_id=?
