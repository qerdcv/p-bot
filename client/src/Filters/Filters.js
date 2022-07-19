import React from "react"
import Button from "../Button/Button"
import styles from "./filters.module.css"

const filters = {
  year: "Текущий топ",
  last_year: "Прошлогодний топ",
  all_time: "Топ ладера",
}

function Filters({currentType, onFilterClick}) {
  return (
    <div className={styles.filters}>
      {Object.entries(filters).map(([type, text], idx) => {
        return <Button
        key={idx}
        text={text}
        type={type} 
        isActive={currentType === type}
        onClick={onFilterClick}>
        </Button>
      })}
    </div>
  )
}

export default Filters
