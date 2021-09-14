select user_id, username, count(user_id) as count from p_stat
where chat_id=?
group by user_id ORDER BY count DESC LIMIT 10;
