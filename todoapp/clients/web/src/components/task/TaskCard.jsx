// todoapp/clients/web/src/components/task/TaskCard.jsx

import { useState, useEffect } from 'react'
import StatusBadge from './StatusBadge'
import TaskStatusToggle from './TaskStatusToggle'
import TaskDeleteButton from './TaskDeleteButton'
import TaskMeta from './TaskMeta'
import PriorityEditor from './PriorityEditor'
import DueDateEditor from './DueDateEditor'
import { formatDaysLeft } from '../../utils/formatters'


function TaskCard({
  task,
  onDeleteTask,
  onToggleStatus,
  onUpdateTaskDescription,
  onUpdateTaskPriority,
  onUpdateTaskDue
}) {
  const [isEditing, setIsEditing] = useState(false)
  const [editValue, setEditValue] = useState(task.description)

  useEffect(() => {
    setEditValue(task.description)
  }, [task.description])

  async function handleSave() {
    const trimmed = editValue.trim()
    if (!trimmed) {
      setEditValue(task.description)
      setIsEditing(false)
      return
    }
    if (trimmed === task.description) {
      setIsEditing(false)
      return
    }
    await onUpdateTaskDescription(task.id, trimmed)
    setIsEditing(false)
  }

  function handleCancel() {
    setEditValue(task.description)
    setIsEditing(false)
  }

  return (
    <div className='task-card'>
      <div className='task-card-left'>
        <TaskStatusToggle task={task} onToggleStatus={onToggleStatus} />
        <div className='task-card-content'>
          {isEditing ? (
            <input
              className='task-card-input'
              type='text'
              value={editValue}
              autoFocus
              onChange={(e) => setEditValue(e.target.value)}
              onBlur={handleSave}
              onKeyDown={(e) => {
                if (e.key === 'Enter') {
                  handleSave()
                }
                if (e.key === 'Escape') {
                  handleCancel()
                }
              }}
            />
          ) : (
            <h3
              className='task-card-title is-editable'
              onClick={() => setIsEditing(true)}
              title='Click to edit'
            >
              {task.description}
            </h3>
          )}
          <div className='task-card-meta meta-row'>
            <span className='meta-item'>
              <DueDateEditor
                value={task.due}
                onChange={(newDue) => onUpdateTaskDue(task.id, newDue)}
              />
            </span>
            <span className='meta-separator'>|</span>
            <span className='meta-item'>
              {formatDaysLeft(task.days_left)}
            </span>
          </div>
        </div>
      </div>

      <div className='task-card-right'>
        <PriorityEditor
          value={task.priority}
          onChange={(newPriority) =>
            onUpdateTaskPriority(task.id, newPriority)
          }
          placement='top'
        />
        <StatusBadge status={task.status} />
        <TaskDeleteButton task={task} onDeleteTask={onDeleteTask} />
      </div>
    </div>
  )
}

export default TaskCard