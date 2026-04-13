// todoapp/clients/web/src/components/task/TaskWidgetCard.jsx

import PriorityBadge from './PriorityBadge'
import TaskStatusToggle from './TaskStatusToggle'
import TaskDeleteButton from './TaskDeleteButton'
import TaskMeta from './TaskMeta'
import '../../styles/task.css'

function TaskWidgetCard({ task, onDeleteTask, onToggleStatus }) {
  return (
    <div className='widget surface-card surface-card-hover task-widget-card'>
      <div className='task-widget-top'>
        <TaskStatusToggle task={task} onToggleStatus={onToggleStatus} />
        <TaskDeleteButton task={task} onDeleteTask={onDeleteTask} />
      </div>

      <div className='task-widget-body'>
        <h3 className='task-widget-title'>{task.description}</h3>
      </div>

      <div className='task-widget-footer'>
        <div className='task-widget-badges'>
          <PriorityBadge priority={task.priority} />
        </div>
        <TaskMeta
          task={task}
          className='task-widget-meta'
          showSeparator={false}
        />
      </div>
    </div>
  )
}

export default TaskWidgetCard