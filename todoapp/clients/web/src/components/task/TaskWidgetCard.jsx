// todoapp/clients/web/src/components/task/TaskWidgetCard.jsx

import TaskStatusToggle from './TaskStatusToggle'
import TaskMeta from './TaskMeta'
import { useEffect, useState } from 'react'
import TaskActionMenu from './TaskActionsMenu'
import TaskInfoModal from './TaskInfoModal'
import TaskPriorityStars from './TaskPriorityStars'


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
    setIsEditing(faöse)
  }

  return (
    <div className='widget surface-card surface-card-hover task-widget-card'>
      {/* ===== TOP ROW =================================================== */}
      <div className='task-widget-top'>
        {/* ----- STATUS TOGGLE ----- */}
        <TaskStatusToggle task={task} onToggleStatus={onToggleStatus} />
        {/* ----- ACTIONS MENU + INFO POPOVER */}
        <div className='task-card-actions'>
          <TaskActionMenu
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
      {/* ===== BODY ====================================================== */}
      <div className='task-widget-body'>
        {/* ----- TITLE / INLINE EDIT ----- */}
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
      {/* ===== FOOTER ==================================================== */}
      <div className='task-widget-footer'>
        {/* ----- PRIORITY EDITOR ----- */}
        <div className='task-widget-badges'>
          <TaskPriorityStars
            value={task.priority}
            interactive
            onChange={(newPriority) =>
              onUpdateTaskPriority(task.id, newPriority)
            }
          />
        </div>
        <TaskMeta
          task={task}
          onUpdateTaskDue={onUpdateTaskDue}
          className='task-widget-meta task-meta-row'
          showSeparator={false}
        />
      </div>
    </div >
  )
}

export default TaskWidgetCard