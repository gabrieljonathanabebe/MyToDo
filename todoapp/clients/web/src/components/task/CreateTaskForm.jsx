// todoapp/clients/web/src/components/task/CreateTaskForm.jsx

import { useRef, useState } from 'react'
import { CalendarDays, FileText } from 'lucide-react'
import TaskPriorityStars from './TaskPriorityStars'
import Panel from '../common/Panel'
import Button from '../common/Button'


function CreateTaskForm({
  description,
  onDescriptionChange,
  priority,
  onPriorityChange,
  due,
  onDueChange,
  notes,
  onNotesChange,
  showNotes,
  onToggleNotes,
  onSubmit,
  error,
}) {
  const [showDetails, setShowDetails] = useState(false)

  const shouldShowDetails =
    showDetails || showNotes || due || notes?.trim()
  const dateInputRef = useRef(null)

  function handleOpenDatePicker() {
    if (dateInputRef.current) {
      dateInputRef.current.showPicker?.()
      dateInputRef.current.focus()
    }
  }

  return (
    <Panel className='form-panel'>
      {/* ===== CREATE TASK FORM ========================================= */}
      <form
        className='create-task-form'
        onSubmit={(e) => {
          e.preventDefault()
          onSubmit(e)
        }}
      >
        {/* ===== MAIN ROW ================================================ */}
        <div className='create-task-main-row'>
          {/* ----- DESCRIPTION INPUT ----- */}
          <input
            className='form-control form-input create-task-description'
            type='text'
            placeholder='Add a new task...'
            value={description}
            onFocus={() => setShowDetails(true)}
            onChange={(e) => onDescriptionChange(e.target.value)}
          />

          {/* ----- SUBMIT BUTTON ----- */}
          <Button type='submit'>Add Task</Button>
        </div>

        {/* ===== META ROW ================================================ */}
        {shouldShowDetails && (
          <div className='create-task-meta-row'>
            {/* ----- PRIORITY ----- */}
            <div className='create-task-meta-group'>
              <TaskPriorityStars
                value={priority}
                interactive
                onChange={
                  (newPriority) => onPriorityChange(String(newPriority))
                }
              />
            </div>

            <span className='create-task-meta-separator' />

            {/* ----- DUE DATE ----- */}
            <div className='create-task-meta-group create-task-due-group'>
              <button
                type='button'
                className='icon-action icon-action-primary'
                onClick={handleOpenDatePicker}
                aria-label='Choose due date'
                title='Choose due date'
              >
                <CalendarDays size={16} strokeWidth={2} />
              </button>

              <span className='create-task-due-value'>
                {due || 'No due date'}
              </span>

              <input
                ref={dateInputRef}
                className='create-task-hidden-date-input'
                type='date'
                value={due}
                onChange={(e) => onDueChange(e.target.value)}
              />
            </div>

            <span className='create-task-meta-separator' />

            {/* ----- NOTES TOGGLE ----- */}
            <div className='create-task-meta-group'>
              <button
                type='button'
                className='icon-action icon-action-primary'
                onClick={onToggleNotes}
                aria-label='Toggle notes'
                title='Toggle notes'
              >
                <FileText size={16} strokeWidth={2} />
              </button>
            </div>
          </div>
        )}

        {/* ===== NOTES AREA ============================================== */}
        {showNotes && (
          <div className='create-task-notes-row'>
            <textarea
              className='form-control form-textarea create-task-notes'
              placeholder='Add notes...'
              value={notes}
              onChange={(e) => onNotesChange(e.target.value)}
              rows={3}
            />
          </div>
        )}
      </form>

      {/* ===== ERROR ==================================================== */}
      {error && <p className='form-error'>{error}</p>}
    </Panel>
  )
}

export default CreateTaskForm