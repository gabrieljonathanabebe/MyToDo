// todoapp/clients/web/src/components/task/TaskMeta.jsx

import { CalendarDays } from 'lucide-react'
import { formatDaysLeft, formatDueDate } from '../../utils/formatters'


function TaskMeta({ task, className = '', showSeparator = true }) {
  return (
    <div className={className}>
      <span className='meta-item'>
        <CalendarDays className='meta-icon' size={14} strokeWidth={2} />
        {formatDueDate(task.due)}
      </span>

      {showSeparator && (
        <span className='meta-separator'>|</span>
      )}

      <span className='meta-item'>
        {formatDaysLeft(task.days_left)}
      </span>
    </div>
  )
}

export default TaskMeta