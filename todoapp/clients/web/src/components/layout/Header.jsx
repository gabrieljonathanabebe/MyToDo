// todoapp/clients/web/src/components/layout/Header.jsx

import Button from "../common/Button"


function Header({ currentUser, onLogout }) {
  return (
    <header className="app-header">
      <div className="brand">
        <span className="brand-mark" />
        <span className="brand-text">MyToDo</span>
      </div>
      {currentUser && (
        <Button onClick={onLogout}>Logout</Button>
      )}
    </header>
  )
}

export default Header

