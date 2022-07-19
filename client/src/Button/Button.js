import React from "react"

// import PropTypes  from "prop-types"

import styles from "./button.module.css"

function Button({text, type, isActive, onClick}) {
  return <button 
  className={isActive ? `${styles.filterButton} ${styles.active}` : styles.filterButton}
  onClick={() => {onClick(type)}}>
  {text}
  </button>
}

// Button.propTypes = {
//   text: PropTypes.string.isRequired,
//   type: PropTypes.string.isRequired,
//   isActive: PropTypes.bool.isRequired,
//   onClick: PropTypes.func.isRequired
// }

export default Button
