// todoapp/clients/web/src/components/task/TaskMeta.jsx

import { Timer } from 'lucide-react'
import { formatDaysLeft } from '../../utils/formatters'
import DueDateEditor from './DueDateEditor'


function TaskMeta({
  task,
  onUpdateTaskDue,
  className = '',
  showSeparator = true,
}) {
  return (
    <div className={className}>
      {/* ===== CORE META ================================================= */}
      {/* ----- DUE DATE ----- */}
      <span className='meta-item'>
        <DueDateEditor
          value={task.due}
          onChange={(newDue) => onUpdateTaskDue(task.id, newDue)}
        />
      </span>

      {/* ----- SEPARATOR ----- */}
      {showSeparator && (
        <span className='meta-separator'>|</span>
      )}

      {/* ----- DAYS LEFT ----- */}
      <span className='meta-item'>
        <Timer className='meta-icon' size={14} strokeWidth={2} />
        {formatDaysLeft(task.days_left)}
      </span>
    </div>
  )
}

export default TaskMeta