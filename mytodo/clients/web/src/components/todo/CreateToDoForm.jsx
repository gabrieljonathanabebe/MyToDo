// mytodo/clients/web/src/components/todo/CreateToDoForm.jsx

import Panel from "../common/Panel"
import Button from "../common/Button"


function CreateToDoForm({ title, onTitleChange, onSubmit, error }) {
  return (
    <Panel className="form-panel">
      <form
        className="form-row"
        onSubmit={(e) => {
          e.preventDefault()
          onSubmit()
        }}
      >
        <input
          className="form-control form-input"
          type="text"
          placeholder="New Todo"
          value={title}
          onChange={(e) => onTitleChange(e.target.value)}
        />

        <Button type="submit">Add</Button>
      </form>

      {error && <p className="form-error">{error}</p>}
    </Panel>
  )
}

export default CreateToDoForm
