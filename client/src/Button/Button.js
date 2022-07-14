import React from "react"

function Button({text, styleButton}) {
  return <button className={styleButton}>{text}</button>
}

export default Button
