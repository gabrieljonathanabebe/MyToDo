// todoapp/clients/web/src/components/task/TaskCard.jsx

import { CalendarDays, Trash2, Circle, CheckCircle } from 'lucide-react'
import { formatDaysLeft, formatDueDate } from "../../utils/formatters";
import "../../styles/task.css"


function TaskCard({ task, onDeleteTask, onToggleStatus }) {
  function renderPriorityBadge(priority) {
    if (priority === "low") {
      return <span className="badge badge-gray">Low</span>
    }
    if (priority === "medium") {
      return <span className="badge badge-yellow">Medium</span>
    }
    if (priority === "high") {
      return <span className="badge badge-red">High</span>
    }
    return <span className="badge">{priority ?? "-"}</span>
  }

  function renderStatusBadge(status) {
    if (status === 'open') {
      return <span className="badge badge-blue">Open</span>
    }
    if (status === 'done') {
      return <span className="badge badge-green">Done</span>
    }
    if (status === 'cancelled') {
      return <span className="badge badge-red">Cancelled</span>
    }
    return <span className="badge badge-gray">{status ?? '-'}</span>
  }

  function handleDelete(e) {
    e.stopPropagation()
    onDeleteTask(task.id)
  }

  function handleToggle(e) {
    e.stopPropagation()
    onToggleStatus(task)
  }

  return (
    <div className="task-card">
      <div className="task-card-left">
        <button
          type="button"
          className={`icon-action ${task.status === 'done'
              ? 'icon-action-success'
              : 'icon-action-neutral'
            }`}
          onClick={handleToggle}
          aria-label={`Toggle status for ${task.description}`}
        >
          {task.status === 'done' ? (
            <CheckCircle size={18} strokeWidth={2} />
          ) : (
            <Circle size={18} strokeWidth={2} />
          )}
        </button>

        <div className="task-card-content">
          <h3 className="task-card-title">{task.description}</h3>

          <div className="task-card-meta meta-row">
            <span className="meta-item">
              <CalendarDays className="meta-icon" size={14} strokeWidth={2} />
              {formatDueDate(task.due)}
            </span>
            <span className="meta-separator">|</span>
            <span className="meta-item">
              {formatDaysLeft(task.days_left)}
            </span>
          </div>
        </div>
      </div>
      <div className="task-card-right">
        {renderPriorityBadge(task.priority)}
        {renderStatusBadge(task.status)}
        <button
          type='button'
          className='icon-action icon-action-danger'
          onClick={handleDelete}
          aria-label={`Delete task ${task.description}`}
          title='Delete Task'
        >
          <Trash2 size={16} strokeWidth={2} />
        </button>
      </div>
    </div>
  )
}


export default TaskCard