// todoapp/clients/web/src/components/todo/ToDoCard.jsx

import Panel from '../common/Panel'
import { formatRelativeDatetime } from '../../utils/formatters'
import { CalendarDays, Clock3, Trash2 } from 'lucide-react'


function ToDoCard({ todo, onOpenToDo, onDeleteToDo }) {
  function handleClick() {
    onOpenToDo(todo)
  }

  function handleDelete(e) {
    e.stopPropagation()
    onDeleteToDo(todo.id)
  }

  return (
    <Panel className="todo-card surface-card surface-card-hover">
      <div className="todo-card-button" onClick={handleClick}>
        <div className="todo-card-left">
          <h3 className="todo-card-title">{todo.title}</h3>
          <div className="todo-card-meta meta-row">
            <div className="meta-item">
              <CalendarDays className='meta-icon' size={14} strokeWidth={2} />
              <span>Created {formatRelativeDatetime(todo.created_at)}</span>
            </div>
            <span className="meta-separator">|</span>
            <div className="meta-item">
              <Clock3 className="meta-icon" size={14} strokeWidth={2} />
              <span>Updated {formatRelativeDatetime(todo.updated_at)}</span>
            </div>
          </div>
        </div>
        <div className="todo-card-right">
          <span className="badge badge-purple">{todo.task_count} tasks</span>
          <button
            type='button'
            className='icon-action icon-action-danger'
            onClick={handleDelete}
            aria-label={`Delete ${todo.title}`}
            title='Delete To-Do'
          >
            <Trash2 size={16} strokeWidth={2} />
          </button>
        </div>
      </div>
    </Panel>
  )
}

export default ToDoCard