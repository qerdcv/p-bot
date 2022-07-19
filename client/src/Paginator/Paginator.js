import React from "react"

import Button from "../Button/Button"
import styles from "./paginator.module.css"

function Paginator({totalPages, currentPage, onClick}) {

  const generateButtons = (totalPages, currentPage, onClick) => {
    let pages = []
    if (totalPages > 5) {
      let [leftSide, rightSide] = [currentPage - 2, currentPage + 2]
      for (let page = leftSide; page <= rightSide; page++) {
        if (page > totalPages) {
          leftSide -= 1
          pages.push(leftSide)
        } else if (page <= 0) {
          rightSide += 1
          pages.push(rightSide)
        } else {
          pages.push(page)
        }
      }
      pages = [...new Set((pages.sort(function(a, b) {return a - b})))]
    } else {
        for (let page = 1; page <= totalPages; page++) {
          pages.push(page)
        }
    }
    return pages.map((page, idx) => {
      return <Button
        key={idx}
        text={page}
        type={page}
        isActive={currentPage === page}
        onClick={onClick}
      />
    })
  }

  return <div className={styles.paginator}>
    <Button
    text='<'
    type={currentPage - 1 > 0 ? currentPage - 1 : currentPage}
    isActive={currentPage === 1}
    onClick={onClick}
    />
    {generateButtons(totalPages, currentPage, onClick)}
    <Button
    text='>'
    type={currentPage + 1 <= totalPages ? currentPage + 1 : currentPage}
    isActive={currentPage === totalPages}
    onClick={onClick}
    />
  </div>
}

export default Paginator
