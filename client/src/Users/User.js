import React from "react"
import PropTypes from "prop-types"
import styles from "./user.module.css"

function User({user, idx}) {
  return (
    <li className={styles.userItem}>
      <div>
        <strong>{idx + 1}. </strong>
          <a className={styles.userLink} href={`https://t.me/${user.username.slice(1)}`}>
            {user.username}
          </a> - {user.selected_count} раз(а)
      </div>
      <img className={styles.userAvatar} src={`http://localhost:4444/media/${user.user_id}.jpg`} alt="avatar"></img>
    </li>
  )
}

User.propTypes = {
  user: PropTypes.object.isRequired,
  idx: PropTypes.number
}

export default User
