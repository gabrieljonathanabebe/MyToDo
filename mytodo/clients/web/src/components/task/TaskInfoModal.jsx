// mytodo/clients/web/src/components/task/TaskInfoModal.jsx

import { useEffect } from 'react'
import { createPortal } from 'react-dom'

import TaskAdvancedMeta from './TaskAdvancedMeta'


function TaskInfoModal({ show, onClose, task }) {
  useEffect(() => {
    if (!show) return

    function handleKeyDown(event) {
      if (event.key === 'Escape') {
        onClose()
      }
    }

    window.addEventListener('keydown', handleKeyDown)
    return () => window.removeEventListener('keydown', handleKeyDown)
  }, [show, onClose])

  if (!show) return null

  return createPortal(
    <div className='task-info-modal-backdrop' onClick={onClose}>
      <div
        className='task-info-modal surface-card'
        onClick={(event) => event.stopPropagation()}
      >
        {/* ===== HEADER =================================================== */}
        <div className='task-info-modal-header'>
          <h3 className='task-info-modal-title'>Task details</h3>
          <button
            type='button'
            className='icon-action icon-action-plain'
            onClick={onClose}
            aria-label='Close task details'
            title='Close'
          >
            ✕
          </button>
        </div>

        {/* ===== CONTENT ================================================== */}
        <TaskAdvancedMeta task={task} />
      </div>
    </div>,
    document.body
  )
}

export default TaskInfoModal
