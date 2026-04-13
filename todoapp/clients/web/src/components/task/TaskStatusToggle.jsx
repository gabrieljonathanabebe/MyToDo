// todoapp/clients/web/src/components/task/TaskStatusToggle.jsx

import { Circle, Check } from "lucide-react";

function TaskStatusToggle({ task, onToggleStatus }) {
  function handleToggle(e) {
    e.stopPropagation()
    onToggleStatus(task)
  }

  const isDone = task.status === 'done'

  return (
    <button
      type='button'
      className={`icon-action ${isDone ? 'icon-action-done' : 'icon-action-neutral'
        }`}
      onClick={handleToggle}
      aria-label={`Toggle status for ${task.description}`}
      title='Toggle status'
    >
      {isDone ? (
        <Check size={12} strokeWidth={2.5} />
      ) : (
        <Circle size={24} strokeWidth={2} />
      )}
    </button>
  )
}

export default TaskStatusToggle