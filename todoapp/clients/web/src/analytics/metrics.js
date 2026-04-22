// todoapp/clients/web/src/analytics/metrics.js


export function getAllTasks(toDoDetails = []) {
  return toDoDetails.flatMap((todo) => todo.tasks ?? [])
}


export function getOverviewStats(toDoSummaries = [], toDoDetails = []) {
  const allTasks = getAllTasks(toDoDetails)
  const openTasks = allTasks.filter((task) => task.status === 'open').length
  const doneTasks = allTasks.filter((task) => task.status === 'done').length

  const overdueTasks = allTasks.filter(
    (task) => task.status !== 'done' && (task.days_left ?? 0) < 0
  ).length

  return {
    totalToDos: toDoSummaries.length,
    totalTasks: allTasks.length,
    openTasks,
    doneTasks,
    overdueTasks,
  }
}


export function getUpcomingTasks(toDoDetails = [], limit = 3) {
  return getAllTasks(toDoDetails)
    .filter((task) => task.status === 'open' && task.due)
    .sort((a, b) => new Date(a.due) - new Date(b.due))
    .slice(0, limit)
}


export function getRecentlyUpdatedToDos(toDoSummaries = [], limit = 3) {
  console.log('metrics/getRecentlyUpdatedToDos', {
    value: toDoSummaries,
    isArray: Array.isArray(toDoSummaries),
    type: typeof toDoSummaries,
  })

  const safeToDoSummaries = Array.isArray(toDoSummaries) ? toDoSummaries : []

  return [...safeToDoSummaries]
    .sort((a, b) => new Date(b.updated_at) - new Date(a.updated_at))
    .slice(0, limit)
}


export function getPriorityBreakdown(toDoDetails = []) {
  const allTasks = getAllTasks(toDoDetails)
  return {
    low: allTasks.filter((task) => task.priority === 'low').length,
    medium: allTasks.filter((task) => task.priority === 'medium').length,
    high: allTasks.filter((task) => task.priority === 'high').length
  }
}


export function getStatusBreakdown(toDoDetails = []) {
  const allTasks = getAllTasks(toDoDetails)
  return {
    open: allTasks.filter((task) => task.status === 'open').length,
    done: allTasks.filter((task) => task.status === 'done').length
  }
}