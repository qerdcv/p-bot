import React from 'react'

import UserList from './users/UserList'
import Filters from './users/Filters'

function App() {
  const users = [
    {user_id: 549675022, username: '@VIBtea', selected_count: 36},
    {user_id: 371668940, username: '@chykchas', selected_count: 35},
    {user_id: 553092701, username: '@qerdcv', selected_count: 33},
    {user_id: 443242502, username: '@polymorphous', selected_count: 31},
    {user_id: 475527566, username: '@dr0zdoff', selected_count: 24},
    {user_id: 549675022, username: '@VIBtea', selected_count: 36},
    {user_id: 371668940, username: '@chykchas', selected_count: 35},
    {user_id: 553092701, username: '@qerdcv', selected_count: 33},
    {user_id: 443242502, username: '@polymorphous', selected_count: 31},
    {user_id: 475527566, username: '@dr0zdoff', selected_count: 24},
  ]

  const in_game_cnt = users.length

  return (
    <div className='wrapper'>
      <h1 className='titleHead'>ТОП-10 Лучших людей за последний год</h1>
      <Filters></Filters>
      <UserList users={users}></UserList>
      <h1 className='titleFoot'>Всего ♂slaves♂ {in_game_cnt}</h1>
    </div>
  )
}

export default App;
