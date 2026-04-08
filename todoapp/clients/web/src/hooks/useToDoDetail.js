// todoapp/clients/web/src/hooks/useToDoDetail.js

import { useEffect, useState } from "react";
import { fetchToDoDetail, createTask } from "../api/toDoDetail";


export function useToDoDetail(currentUser, currentToDo) {
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
    } catch (err) {
      setCreateError(err.message)
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
  }
}