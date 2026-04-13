// todoapp/clients/web/src/components/task/TaskCard.jsx

import PriorityBadge from './PriorityBadge'
import StatusBadge from './StatusBadge'
import TaskStatusToggle from './TaskStatusToggle'
import TaskDeleteButton from './TaskDeleteButton'
import TaskMeta from './TaskMeta'
import '../../styles/task.css'

function TaskCard({ task, onDeleteTask, onToggleStatus }) {
  return (
    <div className='task-card'>
      <div className='task-card-left'>
        <TaskStatusToggle task={task} onToggleStatus={onToggleStatus} />
        <div className='task-card-content'>
          <h3 className='task-card-title'>{task.description}</h3>
          <TaskMeta
            task={task}
            className='task-card-meta meta-row'
            showSeparator={true}
          />
        </div>
      </div>

      <div className='task-card-right'>
        <PriorityBadge priority={task.priority} />
        <StatusBadge status={task.status} />
        <TaskDeleteButton task={task} onDeleteTask={onDeleteTask} />
      </div>
    </div>
  )
}

export default TaskCard