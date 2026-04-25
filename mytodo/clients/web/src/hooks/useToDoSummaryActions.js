// mytodo/clients/web/src/hooks/useToDoSummaryActions.js

import { useState } from "react";
import { createToDo, deleteToDo } from "../api/toDoSummary";


export function useToDoSummaryActions(currentUser, loadTodos, onOpenToDo) {
  const [error, setError] = useState('')
  const [newTitle, setNewTitle] = useState('')
  const [createError, setCreateError] = useState('')

  async function handleCreateToDo() {
    setCreateError('')
    if (!newTitle.trim()) {
      setCreateError('Please enter a title.')
      return
    }
    try {
      const createdToDo = await createToDo(currentUser.username, newTitle.trim())
      setNewTitle('')
      await loadTodos()
      onOpenToDo?.(createdToDo)
    } catch (err) {
      setCreateError(err.message)
    }
  }

  async function handleDeleteToDo(todoId) {
    const confirmed = window.confirm('Do you really want to delete this To-Do?')
    if (!confirmed) return
    setError('')
    try {
      await deleteToDo(currentUser.username, todoId)
      await loadTodos()
    } catch (err) {
      setError(err.message)
    }
  }

  return {
    error,
    newTitle,
    setNewTitle,
    createError,
    handleCreateToDo,
    handleDeleteToDo,
  }
}
