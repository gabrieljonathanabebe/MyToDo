// todoapp/clients/web/src/components/layout/Sidebar.jsx

import { House, ListTodo, LayoutDashboard, Circle } from 'lucide-react'


function Sidebar({
  currentUser,
  currentPage,
  currentToDo,
  todos,
  onGoHome,
  onGoSummary,
  onGoDashboard,
  onOpenToDo,
}) {
  return (
    <aside className="sidebar surface-card">
      {currentUser && (
        <p className="sidebar-user">
          Hi, {currentUser.username}
        </p>
      )}
      <div className="sidebar-section">
        <p className="sidebar-section-title">Navigation</p>
        <button
          className={`sidebar-link ${currentPage === 'home' ? 'active' : ''}`}
          onClick={onGoHome}
        >
          <span className="sidebar-link-content">
            <House className="sidebar-link-icon" size={16} strokeWidth={2} />
            <span>Home</span>
          </span>
        </button>
        <button
          className={`sidebar-link ${currentPage === 'summary' ? 'active' : ''}`}
          onClick={onGoSummary}
        >
          <span className="sidebar-link-content">
            <ListTodo className="sidebar-link-icon" size={16} strokeWidth={2} />
            <span>Summary</span>
          </span>
        </button>
        <button
          className={`sidebar-link ${currentPage === 'dashboard' ? 'active' : ''}`}
          onClick={onGoDashboard}
        >
          <span className="sidebar-link-content">
            <LayoutDashboard className="sidebar-link-icon" size={16} strokeWidth={2} />
            <span>Dashboard</span>
          </span>
        </button>
      </div>
      <div className="sidebar-section sidebar-todos">
        <p className="sidebar-section-title">My Lists</p>
        <div className="sidebar-todo-list">
          {todos.map((todo) => (
            <button
              key={todo.id}
              className={`sidebar-link ${currentPage === 'detail' && currentToDo?.id === todo.id
                ? 'active'
                : ''
                }`}
              onClick={() => onOpenToDo(todo)}
            >
              <span className="sidebar-link-content">
                <Circle className="sidebar-link-icon sidebar-todo-icon" size={12} strokeWidth={2} />
                <span>{todo.title}</span>
              </span>
            </button>
          ))}
        </div>
      </div>
    </aside>
  )
}

export default Sidebar