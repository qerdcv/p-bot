SELECT max(current_streak) AS best_streak
FROM p_stat as p
WHERE
      chat_id=? AND (
          user_id=? AND p.id<(select max(id) from p_stat)
          )
ORDER BY id DESC;
