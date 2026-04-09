// todoapp/clients/web/src/hooks/useToDoDetail.js

import { useEffect, useState } from "react";
import { fetchToDoDetail, createTask, deleteTask } from "../api/toDoDetail";


export function useToDoDetail(currentUser, currentToDo, refreshTodos) {
  const [toDoDetail, setToDoDetail] = useState(null)
  const [error, setError] = useState('')
  const [description, setDescription] = useState('')
  const [priority, setPriority] = useState('2')
  const [due, setDue] = useState('')
  const [createError, setCreateError] = useState('')

  async function loadToDoDetail() {
    if (!currentUser || !currentToDo) return
    setError('')
    try {
      const data = await fetchToDoDetail(
        currentUser.username,
        currentToDo.id
      )
      setToDoDetail(data)
    } catch (err) {
      setError(err.message)
    }
  }

  useEffect(() => {
    loadToDoDetail()
  }, [currentUser, currentToDo])

  async function handleCreateTask() {
    setCreateError('')
    if (!description.trim()) {
      setCreateError('Please enter a description.')
      return
    }
    try {
      await createTask(currentUser.username, currentToDo.id, {
        description: description.trim(),
        priority: Number(priority),
        due: due || null,
      })
      setDescription('')
      setPriority('2')
      setDue('')
      await loadToDoDetail()
      await refreshTodos?.()
    } catch (err) {
      setCreateError(err.message)
    }
  }

  async function handleDeleteTask(taskId) {
    const confirmed = window.confirm('Do you really want to delete this task?')
    if (!confirmed) return
    try {
      await deleteTask(currentUser.username, currentToDo.id, taskId)
      await loadToDoDetail()
      await refreshTodos?.()
    } catch (err) {
      setError(err.message)
    }
  }

  return {
    toDoDetail,
    error,
    description,
    setDescription,
    priority,
    setPriority,
    due,
    setDue,
    createError,
    handleCreateTask,
    handleDeleteTask,
  }
}