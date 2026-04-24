// mytodo/clients/web/src/components/task/TaskDeleteButton.jsx

import { Trash2 } from "lucide-react";

function TaskDeleteButton({ task, onDeleteTask }) {
  function handleDelete(e) {
    e.stopPropagation()
    onDeleteTask(task.id)
  }

  return (
    <button
      type="button"
      className="icon-action icon-action-danger"
      onClick={handleDelete}
      aria-label={`Delete task ${task.description}`}
      title="Delete task"
    >
      <Trash2 size={16} strokeWidth={2} />
    </button>
  )
}

export default TaskDeleteButton
