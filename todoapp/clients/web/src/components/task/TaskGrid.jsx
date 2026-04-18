// todoapp/clients/web/src/components/task/TaskGrid.jsx

import TaskWidgetCard from "./TaskWidgetCard";


function TaskGrid({
  tasks,
  onDeleteTask,
  onToggleStatus,
  onUpdateTaskDescription,
  onUpdateTaskPriority,
  onUpdateTaskDue,
}) {
  return (
    <div className="task-grid">
      {tasks.map((task) => (
        <TaskWidgetCard
          key={task.id}
          task={task}
          onDeleteTask={onDeleteTask}
          onToggleStatus={onToggleStatus}
          onUpdateTaskDescription={onUpdateTaskDescription}
          onUpdateTaskPriority={onUpdateTaskPriority}
          onUpdateTaskDue={onUpdateTaskDue}
        />
      ))}
    </div>
  )
}

export default TaskGrid