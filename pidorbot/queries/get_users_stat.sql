SELECT user_id, username, count(user_id) AS count
FROM p_stat
WHERE CASE 
	WHEN 'year'==:filter_ THEN 
		chat_id=:chat_id AND cast(strftime('%Y', choice_date) AS INTEGER) > DATE() - 1
	WHEN 'last_year'==:filter_ THEN 
		chat_id=:chat_id AND cast(strftime('%Y', choice_date) AS INTEGER) == DATE() - 1
	ELSE
		chat_id=:chat_id
END
GROUP BY user_id ORDER BY count DESC LIMIT 10;
