// todoapp/clients/web/src/components/todo/ToDoLists.jsx

import ToDoCard from "./ToDoCard";
import "../../styles/todo.css"


function ToDoLists({ todos, onOpenToDo, onDeleteToDo }) {
  return (
    <div className="todo-lists">
      {todos.map((todo) => (
        <ToDoCard
          key={todo.id}
          todo={todo}
          onOpenToDo={onOpenToDo}
          onDeleteToDo={onDeleteToDo}
        />
      ))}
    </div>
  )
}


export default ToDoLists