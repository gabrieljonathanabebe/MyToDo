// todoapp/clients/web/src/hooks/useToDoDetail.js

import { useEffect, useState } from 'react'
import {
  createTask,
  deleteTask,
  updateTaskStatus,
  sortTasks,
  updateTaskDescription,
  updateTaskPriority,
  updateTaskDue,
} from '../api/toDoDetail'


export function useToDoDetail(
  currentUser,
  currentToDo,
  initialToDoDetail,
  refreshToDos,
  refreshCurrentToDo
) {
  const [toDoDetail, setToDoDetail] = useState(initialToDoDetail ?? null)
  const [error, setError] = useState('')
  const [description, setDescription] = useState('')
  const [priority, setPriority] = useState('2')
  const [due, setDue] = useState('')
  const [notes, setNotes] = useState('')
  const [showNotes, setShowNotes] = useState(false)
  const [createError, setCreateError] = useState('')

  // ===== SYNC DETAIL FROM CENTRAL WORKSPACE ============================
  useEffect(() => {
    setToDoDetail(initialToDoDetail ?? null)
  }, [initialToDoDetail])

  // ===== HANDLE CREATE TASK ============================================
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
        notes: notes?.trim() ? notes : null,
      })

      setDescription('')
      setPriority('2')
      setDue('')
      setNotes('')
      setShowNotes(false)

      await refreshCurrentToDo?.()
      await refreshToDos?.()
    } catch (err) {
      setCreateError(err.message)
    }
  }

  // ===== HANDLE DELETE TASK ============================================
  async function handleDeleteTask(taskId) {
    const confirmed = window.confirm('Do you really want to delete this task?')
    if (!confirmed) return

    try {
      await deleteTask(currentUser.username, currentToDo.id, taskId)
      await refreshCurrentToDo?.()
      await refreshToDos?.()
    } catch (err) {
      setError(err.message)
    }
  }

  // ===== HANDLE TOGGLE TASK STATUS =====================================
  async function handleToggleTaskStatus(task) {
    let newStatus

    if (task.status === 'open') {
      newStatus = 'done'
    } else if (task.status === 'done') {
      newStatus = 'open'
    } else {
      newStatus = 'open'
    }

    try {
      await updateTaskStatus(
        currentUser.username,
        currentToDo.id,
        task.id,
        newStatus
      )
      await refreshCurrentToDo?.()
      await refreshToDos?.()
    } catch (err) {
      setError(err.message)
    }
  }

  // ===== HANDLE SORT TASKS =============================================
  async function handleSortTasks(key, reverse = false) {
    try {
      await sortTasks(
        currentUser.username,
        currentToDo.id,
        key,
        reverse
      )
      await refreshCurrentToDo?.()
      await refreshToDos?.()
    } catch (err) {
      setError(err.message)
    }
  }

  // ===== HANDLE UPDATE TASK DESCRIPTION ================================
  async function handleUpdateTaskDescription(taskId, description) {
    try {
      await updateTaskDescription(
        currentUser.username,
        currentToDo.id,
        taskId,
        description
      )
      await refreshCurrentToDo?.()
      await refreshToDos?.()
    } catch (err) {
      setError(err.message)
    }
  }

  // ===== HANDLE UPDATE TASK PRIORITY ===================================
  async function handleUpdateTaskPriority(taskId, priority) {
    try {
      await updateTaskPriority(
        currentUser.username,
        currentToDo.id,
        taskId,
        priority
      )
      await refreshCurrentToDo?.()
      await refreshToDos?.()
    } catch (err) {
      setError(err.message)
    }
  }

  // ===== HANDLE UPDATE TASK DUE ========================================
  async function handleUpdateTaskDue(taskId, newDue) {
    try {
      await updateTaskDue(
        currentUser.username,
        currentToDo.id,
        taskId,
        newDue
      )
      await refreshCurrentToDo?.()
      await refreshToDos?.()
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
    notes,
    setNotes,
    showNotes,
    setShowNotes,
    createError,
    handleCreateTask,
    handleDeleteTask,
    handleToggleTaskStatus,
    handleSortTasks,
    handleUpdateTaskDescription,
    handleUpdateTaskPriority,
    handleUpdateTaskDue,
  }
}
