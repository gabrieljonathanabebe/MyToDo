// todoapp/clients/web/src/hooks/useNavigationState.js

import { useState } from 'react'

const PAGE_STORAGE_KEY = 'mytodo.navigation.page'
const TODO_ID_STORAGE_KEY = 'mytodo.navigation.todoId'

export function useNavigationState() {
  const [page, setPage] = useState(() => {
    return localStorage.getItem(PAGE_STORAGE_KEY) ?? 'login'
  })

  const [currentToDoId, setCurrentToDoId] = useState(() => {
    return localStorage.getItem(TODO_ID_STORAGE_KEY)
  })

  function navigateTo(nextPage) {
    setCurrentToDoId(null)
    setPage(nextPage)

    localStorage.setItem(PAGE_STORAGE_KEY, nextPage)
    localStorage.removeItem(TODO_ID_STORAGE_KEY)
  }

  function openToDo(toDo) {
    setCurrentToDoId(toDo.id)
    setPage('detail')

    localStorage.setItem(PAGE_STORAGE_KEY, 'detail')
    localStorage.setItem(TODO_ID_STORAGE_KEY, toDo.id)
  }

  function clearNavigation() {
    setPage('login')
    setCurrentToDoId(null)

    localStorage.removeItem(PAGE_STORAGE_KEY)
    localStorage.removeItem(TODO_ID_STORAGE_KEY)
  }

  return {
    page,
    currentToDoId,
    setPage,
    navigateTo,
    openToDo,
    clearNavigation,
  }
}
