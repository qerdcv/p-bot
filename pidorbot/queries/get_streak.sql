SELECT username, max(streak) AS max_streak, (
    SELECT streak FROM p_stat WHERE user_id=:user_id ORDER BY id DESC
) as current_streak
FROM p_stat
WHERE chat_id=:chat_id AND user_id=:user_id;
