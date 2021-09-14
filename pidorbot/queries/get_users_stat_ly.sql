select user_id, username, count(user_id) as count from p_stat
where chat_id=?
  and cast(strftime('%Y', choice_date) as integer) < DATE()
  and cast(strftime('%Y', choice_date) as integer) > DATE() - 2
group by user_id ORDER BY count DESC LIMIT 10;
