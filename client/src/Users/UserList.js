import React from "react"

import PropTypes  from "prop-types"

import User from "./User"
import styles from "./userList.module.css"

function UserList(props) {
  return (
    <ul className={styles.users}>
      { props.users.map((user, idx) => {
        return <User user={user} idx={idx} key={idx}></User>
      }) }
    </ul>
  )
}

UserList.propTypes = {
  users: PropTypes.array.isRequired
}

export default UserList
