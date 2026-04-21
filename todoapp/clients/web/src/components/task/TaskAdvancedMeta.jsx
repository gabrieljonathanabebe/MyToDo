// todoapp/clients/web/src/components/task/TaskAdvancedMeta.jsx

import {
  formatRelativeDatetime,
  formatDuration,
} from '../../utils/formatters'


function TaskAdvancedMeta({ task }) {
  return (
    <div className='task-advanced-meta'>
      {/* ===== HEADER ==================================================== */}
      <div className='task-advanced-meta-title'>
        {task.description}
      </div>

      {/* ===== META ROWS ================================================= */}
      {/* ----- CREATED AT ----- */}
      <div className='task-advanced-meta-row'>
        <span className='task-advanced-meta-label'>Created</span>
        <span className='task-advanced-meta-value'>
          {task.created_at ? formatRelativeDatetime(task.created_at) : '-'}
        </span>
      </div>

      {/* ----- UPDATED AT ----- */}
      <div className='task-advanced-meta-row'>
        <span className='task-advanced-meta-label'>Updated</span>
        <span className='task-advanced-meta-value'>
          {task.updated_at ? formatRelativeDatetime(task.updated_at) : '-'}
        </span>
      </div>

      {/* ----- COMPLETED AT ----- */}
      <div className='task-advanced-meta-row'>
        <span className='task-advanced-meta-label'>Completed</span>
        <span className='task-advanced-meta-value'>
          {task.completed_at ? formatRelativeDatetime(task.completed_at) : '-'}
        </span>
      </div>

      {/* ----- LEAD TIME ----- */}
      <div className='task-advanced-meta-row'>
        <span className='task-advanced-meta-label'>Lead time</span>
        <span className='task-advanced-meta-value'>
          {task.lead_time_seconds != null
            ? formatDuration(task.lead_time_seconds)
            : '-'}
        </span>
      </div>

      {/* ----- NOTES ----- */}
      <div className='task-advanced-meta-notes'>
        <div className='task-advanced-meta-label'>Notes</div>
        <div className='task-advanced-meta-note-text'>
          {task.notes?.trim() ? task.notes : '-'}
        </div>
      </div>
    </div>
  )
}

export default TaskAdvancedMeta