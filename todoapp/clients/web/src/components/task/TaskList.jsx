// todoapp/clients/web/src/components/task/TaskList.jsx

import Panel from "../common/Panel";
import TaskCard from "./TaskCard";
import "../../styles/task.css"


function TaskList({ tasks }) {
  return (
    <Panel className="task-list-panel">
      <div className="task-list-header">
        <div className="task-list-header-left">Description</div>
        <div className="task-list-header-right">
          <span>Priority</span>
          <span>Status</span>
        </div>
      </div>
      {tasks.map((task, index) => (
        <div
          key={task.id}
          className={`task-list-item ${index !== tasks.length - 1 ? 'with-separator' : ''
            }`}
        >
          <TaskCard task={task} />
        </div>
      ))}
    </Panel>
  )
}


export default TaskList