// mytodo/clients/web/src/hooks/useToDoSummaries.js

import { useState } from 'react'
import { fetchToDoSummaries } from '../api/toDoSummary'


export function useToDoSummaries() {
  const [todos, setTodos] = useState([])
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState('')

  async function loadTodos(user) {
    if (!user) return
    setLoading(true)
    setError('')
    try {
      const data = await fetchToDoSummaries(user.username)
      setTodos(data)
    } catch (err) {
      setError(err.message)
    } finally {
      setLoading(false)
    }
  }

  function clearTodos() {
    setTodos([])
    setError('')
    setLoading(false)
  }

  return {
    todos,
    loading,
    error,
    loadTodos,
    clearTodos,
  }
}
