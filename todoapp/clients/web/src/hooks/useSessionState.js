// todoapp/clients/web/src/hooks/useSessionState.js

import { useState } from "react";


const SESSION_STORAGE_KEY = 'mytodo.session.user'


export function useSessionState() {
  const [currentUser, setCurrentUser] = useState(() => {
    const raw = localStorage.getItem(SESSION_STORAGE_KEY)
    return raw ? JSON.parse(raw) : null
  })

  function loginUser(user) {
    setCurrentUser(user)
    localStorage.setItem(SESSION_STORAGE_KEY, JSON.stringify(user))
  }
  function logoutUser() {
    setCurrentUser(null)
    localStorage.removeItem(SESSION_STORAGE_KEY)
  }

  return {
    currentUser,
    loginUser,
    logoutUser,
  }
}