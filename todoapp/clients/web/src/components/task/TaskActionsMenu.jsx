// todoapp/clients/web/src/components/task/TaskActionMenu.jsx

import { useState } from "react";
import { MoreHorizontal, Info, Trash2 } from "lucide-react";
import PopoverMenu from "../common/PopoverMenu";


function TaskActionMenu({ onDelete, onOpenInfo }) {
  const [open, setOpen] = useState(false)

  function handleInfo() {
    setOpen(false)
    onOpenInfo()
  }

  function handleDelete() {
    setOpen(false)
    const confirmed = window.confirm('Delete this task?')
    if (confirmed) {
      onDelete()
    }
  }

  return (
    <PopoverMenu
      show={open}
      onClose={() => setOpen(false)}
      anchorClassName="task-actions-anchor"
      trigger={
        <button
          type="button"
          className="icon-action icon-action-plain"
          onClick={() => setOpen((prev) => !prev)}
          aria-label="Open task actions"
          title="Task actions"
        >
          <MoreHorizontal size={18} strokeWidth={2} />
        </button>
      }
    >
      <div className="sort-menu">
        <button
          type="button"
          className="sort-menu-item"
          onClick={handleInfo}
        >
          <span className="sort-menu-label">
            <Info size={15} strokeWidth={2} />
            <span>Info</span>
          </span>
        </button>
        <button
          type="button"
          className="sort-menu-item"
          onClick={handleDelete}
        >
          <span className="sort-menu-label">
            <Trash2 size={15} strokeWidth={2} />
            <span>Delete</span>
          </span>
        </button>
      </div>
    </PopoverMenu>
  )
}

export default TaskActionMenu
