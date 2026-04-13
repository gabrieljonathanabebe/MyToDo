// todoapp/clients/web/src/components/task/TaskGrid.jsx

import TaskWidgetCard from "./TaskWidgetCard";
import '../../styles/task.css'


function TaskGrid({ tasks, onDeleteTask, onToggleStatus }) {
  return (
    <div className="task-grid">
      {tasks.map((task) => (
        <TaskWidgetCard
          key={task.id}
          task={task}
          onDeleteTask={onDeleteTask}
          onToggleStatus={onToggleStatus}
        />
      ))}
    </div>
  )
}

export default TaskGrid