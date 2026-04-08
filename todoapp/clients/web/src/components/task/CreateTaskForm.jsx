// todoapp/clients/web/src/components/todo/CreateTaskForm.jsx

import Panel from "../common/Panel";
import Button from "../common/Button";


function CreateTaskForm({
  description,
  onDescriptionChange,
  priority,
  onPriorityChange,
  due,
  onDueChange,
  onSubmit,
  error,
}) {
  return (
    <Panel className="form-panel">
      <form
        className="form-row"
        onSubmit={(e) => {
          e.preventDefault()
          onSubmit(e)
        }}
      >
        <input
          className="form-input"
          type="text"
          placeholder="Description"
          value={description}
          onChange={(e) => onDescriptionChange(e.target.value)}
        />
        <select
          className="form-select"
          value={priority}
          onChange={(e) => onPriorityChange(e.target.value)}
        >
          <option value={'1'}>Low</option>
          <option value={'2'}>Medium</option>
          <option value={'3'}>High</option>
        </select>
        <input
          className="form-date"
          type="date"
          value={due}
          onChange={(e) => onDueChange(e.target.value)}
        />
        <Button type="submit">Add Task</Button>
      </form>
      {error && <p className="form-error"></p>}
    </Panel>
  )
}

export default CreateTaskForm