import React, { useEffect, useState } from 'react'

import UserList from './Users/UserList'
import Filters from './Filters/Filters'
import Paginator from './Paginator/Paginator'

function App() {
  const paginator = {
    page: 1,
    limit: 10,
    total_pages: 10
  }

  const [users, setUsers] = useState([])
  const [inGameCnt, setInGameCnt] = useState(0)
  const [currentType, setCurrentType] = useState()
  const [page, setPage] = useState()
  const [limit, setLimit] = useState()

  useEffect(() => {
    fetch(`${window.location.pathname}?filter=${currentType}&page=${page}`)
    .then((resp) => resp.json())
    .then((data) => {setUsers(data.users); setInGameCnt(data.in_game_cnt)})
    .catch((error) => {console.error(error)})
  }, [currentType, page])

  useEffect(() => {
    setCurrentType(
      new URLSearchParams(window.location.search).get("filter") || "year"
    )
    setPage(
      new URLSearchParams(window.location.search).get("page") || "1"
    )
    setLimit(
      new URLSearchParams(window.location.search).get("limit") || "10"
    )
  }, [])

  const onFilterClick = (type) => {
    window.history.pushState(null, window.title, `?filter=${type}`)
    setCurrentType(type)
    setPage(1)
  }

  const onPaginatorClick = (page) => {
    window.history.pushState(null, window.title, `?filter=${currentType}&page=${page}`)
    setPage(page)
  }

  return (
    <div className='wrapper'>
      <h1 className='titleHead'>{`ТОП-${limit} Лучших людей за последний год`}</h1>
      <Filters 
      currentType={currentType}
      onFilterClick={onFilterClick} />
      <UserList users={users}></UserList>
      <Paginator 
      totalPages={parseInt(paginator.total_pages)} 
      currentPage={parseInt(page)}
      onClick={onPaginatorClick} />
      <h1 className='titleFoot'>Всего ♂slaves♂ {inGameCnt}</h1>
    </div>
  )
}

export default App;
