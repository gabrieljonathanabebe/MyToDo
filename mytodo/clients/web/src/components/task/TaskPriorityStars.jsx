// mytodo/clients/web/src/components/task/TaskPriorityStars.jsx

import { Star } from 'lucide-react'
import { priorityConfig } from './config/priorityConfig'


function TaskPriorityStars({
  value,
  interactive = false,
  onChange,
  className = '',
  size = 16,
}) {
  const numericValue =
    typeof value === 'number'
      ? value
      : priorityConfig[value]?.value ?? Number(value)

  return (
    <div className={`task-priority-stars ${className}`}>
      {/* ===== STARS ===================================================== */}
      {[1, 2, 3].map((starValue) => {
        const isFilled = starValue <= numericValue

        const icon = (
          <Star
            size={size}
            strokeWidth={2}
            className={
              `task-priority-star ${isFilled ? 'is-filled' : ''}`
            }
            fill={isFilled ? 'currentColor' : 'none'}
          />
        )

        {/* ----- DISPLAY ONLY ----- */ }
        if (!interactive) {
          return (
            <span
              key={starValue}
              className='task-priority-star-display'
            >
              {icon}
            </span>
          )
        }

        {/* ----- INLINE EDITING ----- */ }
        return (
          <button
            key={starValue}
            type='button'
            className='task-priority-star-button'
            onClick={() => onChange?.(starValue)}
            aria-label={`Set priority to ${starValue}`}
            title={`Priority ${starValue}`}
          >
            {icon}
          </button>
        )
      })}
    </div>
  )
}

export default TaskPriorityStars
