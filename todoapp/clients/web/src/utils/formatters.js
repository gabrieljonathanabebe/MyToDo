// todoapp/clients/web/src/utils/formatters.js


export function formatRelativeDatetime(value) {
  if (!value) return '-'

  const dt = new Date(value)
  const now = new Date()

  const totalSeconds = Math.floor((now - dt) / 1000)
  const minutes = Math.floor(totalSeconds / 60)
  const hours = Math.floor(totalSeconds / 3600)
  const days = Math.floor(totalSeconds / 86400)

  if (totalSeconds < 60) return 'just now'
  if (minutes < 60) return `${minutes} min ago`
  if (hours < 24) return `${hours} h ago`
  if (days < 2) return 'yesterday'

  return dt.toLocaleDateString(undefined, {
    month: 'short',
    day: 'numeric',
    year: 'numeric',
  })
}


export function formatDaysLeft(value) {
  if (value === null || value == undefined) return 'No deadline'
  if (value === 0) return 'Due today'
  if (value === 1) return '1 day left'
  if (value > 1) return `${value} days left`
  if (value === -1) return '1 day overdue'
  return `${Math.abs(value)} days overdue`
}


export function formatDueDate(dateStr) {
  if (!dateStr) return 'No due date'
  const date = new Date(dateStr)
  return date.toLocaleDateString(undefined, {
    month: 'short',
    day: 'numeric',
    year: 'numeric'
  })
}