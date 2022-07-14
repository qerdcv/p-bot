import React from "react"
import Button from "../utils/Button"


function CreateButton(count, filter) {
  for (let idx = 0; idx <= count; idx++) {
    if (idx === 0) {
      return <Button
      key={idx}
      url={`?page=${0}&filter=${filter}`}
      text={'<'}
      ></Button>
    } else if (idx === count) {
      return <Button
      key={idx}
      url={`?page=${0}&filter=${filter}`}
      text={'>'}
      ></Button>
    } else {
      return <Button
      key={idx}
      url={`?page=${0}&filter=${filter}`}
      text={idx}
      ></Button>
    }
  }
}

function Paginator() {
  let count_page = 5
  let activeFilter = 'year'
  return <div>
    {count_page > 3 ? CreateButton(5, activeFilter) : CreateButton(count_page + 2, activeFilter)}
  </div>
}

export default Paginator
