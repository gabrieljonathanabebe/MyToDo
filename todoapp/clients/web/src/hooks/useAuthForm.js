// todoapp/clients/web/src/hooks/useAuthForm.js

import { useState } from 'react'
import { login, register } from '../api/auth'

export function useAuthForm(onLogin) {
  const [username, setUsername] = useState('')
  const [password, setPassword] = useState('')
  const [error, setError] = useState('')
  const [mode, setMode] = useState('login')

  async function handleSubmit(e) {
    e.preventDefault()
    setError('')

    try {
      const user =
        mode === 'login'
          ? await login(username, password)
          : await register(username, password)

      onLogin(user)
    } catch (err) {
      setError(err.message)
    }
  }

  function handleToggleMode() {
    setMode((prev) => (prev === 'login' ? 'register' : 'login'))
    setError('')
  }

  return {
    username,
    setUsername,
    password,
    setPassword,
    error,
    mode,
    handleSubmit,
    handleToggleMode,
  }
}