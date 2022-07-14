import React from "react"
import Button from "../utils/Button"
import styles from "./filters.module.css"

const filtersName = [
  'Текущий топ',
  'Прошлогодний топ',
  'Топ ладера'
]

function Filters(props) {
  return (
    <div className={styles.filter}>
      {filtersName.map((filterName, idx) => {
          return <Button
          key={idx}
          text={filterName} 
          styleButton={
            props.activeFilterIdx === idx ? `${styles.filterButton} active` : styles.filterButton
          }>
          </Button>
      })}
    </div>
  )
}

Filters.defaultProps = {
  activeFilterIdx: 0
}

export default Filters
