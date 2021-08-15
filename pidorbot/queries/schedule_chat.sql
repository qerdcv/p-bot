UPDATE p
SET scheduled = NOT scheduled
WHERE chat_id=?;
