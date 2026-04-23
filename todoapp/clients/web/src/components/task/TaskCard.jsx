// todoapp/clients/web/src/components/task/TaskCard.jsx

import { useState, useEffect } from 'react'
import StatusBadge from './StatusBadge'
import TaskStatusToggle from './TaskStatusToggle'
import TaskDeleteButton from './TaskDeleteButton'
import TaskPriorityStars from './TaskPriorityStars'
import TaskMeta from './TaskMeta'
import TaskActionsMenu from './TaskActionsMenu'
import TaskInfoModal from './TaskInfoModal'


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
  const [showInfo, setShowInfo] = useState(false)

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
          <TaskMeta
            task={task}
            onUpdateTaskDue={onUpdateTaskDue}
            className='task-card-meta task-meta-row'
            showSeparator={true}
          />
        </div>
      </div>

      <div className='task-card-right'>
        <TaskPriorityStars
          value={task.priority}
          interactive
          onChange={(newPriority) =>
            onUpdateTaskPriority(task.id, newPriority)
          }
        />
        <StatusBadge status={task.status} />
        <div className='task-card-actions'>
          <TaskActionsMenu
            onDelete={() => onDeleteTask(task.id)}
            onOpenInfo={() => setShowInfo(true)}
          />

          <TaskInfoModal
            show={showInfo}
            onClose={() => setShowInfo(false)}
            task={task}
          />
        </div>
      </div>
    </div>
  )
}

export default TaskCard
