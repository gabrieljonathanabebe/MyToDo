// mytodo/clients/web/src/components/task/TaskList.jsx

import Panel from "../common/Panel";
import TaskCard from "./TaskCard";


function TaskList({
  tasks,
  onDeleteTask,
  onToggleStatus,
  onUpdateTaskDescription,
  onUpdateTaskPriority,
  onUpdateTaskDue
}) {
  return (
    <Panel className="task-list-panel">
      <div className="task-list-header">
        <div className="task-list-header-left">Description</div>
        <div className="task-list-header-right">
          <span>Priority</span>
          <span>Status</span>
          <span className="task-list-header-action" aria-hidden="true"></span>
        </div>
      </div>
      {tasks.map((task, index) => (
        <div
          key={task.id}
          className={`task-list-item ${index !== tasks.length - 1 ? 'with-separator' : ''
            }`}
        >
          <TaskCard
            task={task}
            onDeleteTask={onDeleteTask}
            onToggleStatus={onToggleStatus}
            onUpdateTaskDescription={onUpdateTaskDescription}
            onUpdateTaskPriority={onUpdateTaskPriority}
            onUpdateTaskDue={onUpdateTaskDue}
          />
        </div>
      ))}
    </Panel>
  )
}


export default TaskList
