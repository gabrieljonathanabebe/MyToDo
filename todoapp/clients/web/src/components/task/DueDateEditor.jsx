// todoapp/clients/web/src/components/task/DueDateEditor.jsx

import { useEffect, useState } from 'react'
import { CalendarDays } from 'lucide-react'
import { formatDueDate } from '../../utils/formatters'

function DueDateEditor({ value, onChange }) {
  const [isEditing, setIsEditing] = useState(false)
  const [editValue, setEditValue] = useState(value ?? '')

  useEffect(() => {
    setEditValue(value ?? '')
  }, [value])

  async function handleSave(newValue) {
    if (newValue === (value ?? '')) {
      setIsEditing(false)
      return
    }

    await onChange(newValue || null)
    setIsEditing(false)
  }

  function handleCancel() {
    setEditValue(value ?? '')
    setIsEditing(false)
  }

  if (isEditing) {
    return (
      <input
        className='due-date-input'
        type='date'
        value={editValue}
        autoFocus
        onChange={(e) => setEditValue(e.target.value)}
        onBlur={() => handleSave(editValue)}
        onKeyDown={(e) => {
          if (e.key === 'Enter') {
            handleSave(editValue)
          }

          if (e.key === 'Escape') {
            handleCancel()
          }
        }}
      />
    )
  }

  return (
    <button
      type='button'
      className='due-date-display'
      onClick={() => setIsEditing(true)}
      title='Click to edit due date'
    >
      <CalendarDays className='meta-icon' size={14} strokeWidth={2} />
      <span>{formatDueDate(value)}</span>
    </button>
  )
}

export default DueDateEditor
