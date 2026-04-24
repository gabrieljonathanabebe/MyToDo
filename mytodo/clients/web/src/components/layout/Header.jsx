// mytodo/clients/web/src/components/layout/Header.jsx

import Button from "../common/Button"
import Brand from "../common/Brand"


function Header({ currentUser, onLogout, onGoHome }) {
  return (
    <header className="app-header surface-card surface-strong">
      {/* ===== BRAND ===================================================== */}
      <button
        type="button"
        className="app-brand-button"
        onClick={onGoHome}
        aria-label="Go to home"
        title="Go to home"
      >
        <Brand />
      </button>
      {/* ===== ACTIONS =================================================== */}
      {currentUser && (
        <Button onClick={onLogout}>Logout</Button>
      )}
    </header>
  )
}

export default Header
