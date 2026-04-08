// todoapp/clients/web/src/components/task/TaskCard.jsx

import { CalendarDays } from 'lucide-react'
import { formatDaysLeft, formatDueDate } from "../../utils/formatters";
import "../../styles/task.css"


function TaskCard({ task }) {
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

  return (
    <div className="task-card">
      <div className="task-card-left">
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
      <div className="task-card-right">
        {renderPriorityBadge(task.priority)}
        {renderStatusBadge(task.status)}
      </div>
    </div>
  )
}


export default TaskCard