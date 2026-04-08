// todoapp/clients/web/src/hooks/useSessionState.js

import { useState } from "react";


export function useSessionState() {
  const [currentUser, setCurrentUser] = useState(null)

  function loginUser(user) {
    setCurrentUser(user)
  }
  function logoutUser() {
    setCurrentUser(null)
  }

  return {
    currentUser,
    loginUser,
    logoutUser,
  }
}