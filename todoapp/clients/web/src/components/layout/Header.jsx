// todoapp/clients/web/src/components/layout/Header.jsx

import Button from "../common/Button"
import Brand from "../common/Brand"


function Header({ currentUser, onLogout }) {
  return (
    <header className="app-header surface-card surface-strong">
      <Brand />
      {currentUser && (
        <Button onClick={onLogout}>Logout</Button>
      )}
    </header>
  )
}

export default Header

