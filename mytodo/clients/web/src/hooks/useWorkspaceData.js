// mytodo/clients/web/src/hooks/useWorkspaceData.js


import { useEffect, useState } from "react";
import { fetchToDoSummaries } from "../api/toDoSummary";
import { fetchToDoDetail } from "../api/toDoDetail";


export function useWorkspaceData() {
  const [toDoSummaries, setToDoSummaries] = useState([])
  const [toDoDetailsbyId, setToDoDetailsById] = useState({})
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState('')

  // ===== LOAD FULL WORKSPACE ================================================
  async function loadWorkspace(user) {
    if (!user) return
    setLoading(true)
    setError('')

    try {
      const summaries = await fetchToDoSummaries(user.username)
      setToDoSummaries(summaries)

      const details = await Promise.all(
        summaries.map((todo) => fetchToDoDetail(user.username, todo.id))
      )

      const detailsMap = Object.fromEntries(
        details.map((todo) => [todo.id, todo])
      )

      setToDoDetailsById(detailsMap)
    } catch (err) {
      setError(err.message)
    } finally {
      setLoading(false)
    }
  }

  // ===== REFRESH ONLY SUMMARIES =============================================
  async function refreshSummaries(user) {
    if (!user) return

    try {
      const summaries = await fetchToDoSummaries(user.username)
      setToDoSummaries(summaries)
    } catch (err) {
      setError(err.message)
    }
  }

  // ===== REFRESH SINGLE TODO DETAIL =========================================
  async function refreshToDo(user, todoId) {
    if (!user || !todoId) return

    try {
      const detail = await fetchToDoDetail(user.username, todoId)
      setToDoDetailsById((prev) => ({
        ...prev,
        [todoId]: detail
      }))
    } catch (err) {
      setError(err.message)
    }
  }

  // ===== GETTERS ============================================================
  function getToDoDetail(todoId) {
    return toDoDetailsbyId[todoId] ?? null
  }

  function getAllToDoDetails() {
    return Object.values(toDoDetailsbyId)
  }

  // ===== CLEAR ==============================================================
  function clearWorkspace() {
    setToDoSummaries([])
    setToDoDetailsById({})
    setError('')
    setLoading(false)
  }

  return {
    toDoSummaries,
    toDoDetailsbyId,
    toDoDetails: getAllToDoDetails(),
    loading,
    error,
    loadWorkspace,
    refreshSummaries,
    refreshToDo,
    getToDoDetail,
    clearWorkspace,
  }
}
