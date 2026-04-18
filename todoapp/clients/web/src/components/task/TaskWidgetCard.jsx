// todoapp/clients/web/src/components/task/TaskWidgetCard.jsx

import TaskStatusToggle from './TaskStatusToggle'
import TaskDeleteButton from './TaskDeleteButton'
import TaskMeta from './TaskMeta'
import PriorityEditor from './PriorityEditor'
import DueDateEditor from './DueDateEditor'
import { formatDaysLeft } from '../../utils/formatters'
import { useEffect, useState } from 'react'


function TaskWidgetCard({
  task,
  onDeleteTask,
  onToggleStatus,
  onUpdateTaskDescription,
  onUpdateTaskPriority,
  onUpdateTaskDue,
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
    setIsEditing(faöse)
  }

  return (
    <div className='widget surface-card surface-card-hover task-widget-card'>
      <div className='task-widget-top'>
        <TaskStatusToggle task={task} onToggleStatus={onToggleStatus} />
        <TaskDeleteButton task={task} onDeleteTask={onDeleteTask} />
      </div>

      <div className='task-widget-body'>
        {isEditing ? (
          <input
            className='task-widget-input'
            type='text'
            value={editValue}
            autoFocus
            onChange={(e) => setEditValue(e.target.value)}
            onBlur={handleSave}
            onKeyDown={(e) => {
              if (e.key === 'Enter') handleSave()
              if (e.key === 'Escape') handleCancel()
            }}
          />
        ) : (
          <h3
            className='task-widget-title is-editable'
            onClick={() => setIsEditing(true)}
            title='Click to edit'
          >
            {task.description}
          </h3>
        )}
      </div>

      <div className='task-widget-footer'>
        <div className='task-widget-badges'>
          <PriorityEditor
            value={task.priority}
            onChange={(newPriority) =>
              onUpdateTaskPriority(task.id, newPriority)
            }
            placement='top'
          />
        </div>
        <div className='task-widget-meta'>
          <span className='meta-item'>
            <DueDateEditor
              value={task.due}
              onChange={(newDue) => onUpdateTaskDue(task.id, newDue)}
            />
          </span>
          <span className='meta-item'>
            {formatDaysLeft(task.days_left)}
          </span>
        </div>
      </div>
    </div>
  )
}

export default TaskWidgetCard