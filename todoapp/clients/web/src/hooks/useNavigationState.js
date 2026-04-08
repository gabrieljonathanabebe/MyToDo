// todoapp/clients/web/src/hooks/useNavigationState.js

import { useState } from "react";


export function useNavigationState() {
  const [page, setPage] = useState('login')
  const [currentToDo, setCurrentToDo] = useState(null)

  function navigateTo(nextPage) {
    setCurrentToDo(null)
    setPage(nextPage)
  }

  function openToDo(todo) {
    setCurrentToDo(todo)
    setPage('detail')
  }

  return {
    page,
    currentToDo,
    setPage,
    navigateTo,
    openToDo,
  }
}