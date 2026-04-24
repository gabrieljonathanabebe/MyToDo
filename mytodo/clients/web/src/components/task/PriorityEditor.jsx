// mytodo/clients/web/src/components/task/PriorityEditor.jsx

import { useState } from 'react'
import PopoverMenu from '../common/PopoverMenu'
import PriorityBadge from './PriorityBadge'
import { Check } from 'lucide-react'
import { priorityOptions } from './config/priorityConfig'


function PriorityEditor({ value, onChange, placement = 'bottom' }) {
  const [open, setOpen] = useState(false)

  function handleSelect(newPriority) {
    setOpen(false)

    if (newPriority !== value) {
      onChange(newPriority)
    }
  }

  return (
    <PopoverMenu
      show={open}
      onClose={() => setOpen(false)}
      anchorClassName='priority-editor-anchor'
      placement={placement}
      trigger={
        <button
          type='button'
          onClick={() => setOpen((prev) => !prev)}
          className='badge-button'
        >
          <PriorityBadge priority={value} />
        </button>
      }
    >
      <div className='priority-menu'>
        {priorityOptions.map((option) => (
          <button
            key={option.key}
            type='button'
            className={`priority-menu-item ${value === option.key ? 'is-active' : ''}`}
            onClick={() => handleSelect(option.value)}
          >
            <span className='priority-menu-check-slot'>
              {value === option.key && (
                <Check size={16} strokeWidth={2.5} className='priority-menu-check-icon' />
              )}
            </span>

            <span className='priority-menu-label'>
              <PriorityBadge priority={option.key} />
            </span>
          </button>
        ))}
      </div>
    </PopoverMenu>
  )
}

export default PriorityEditor
