// todoapp/clients/web/src/components/layout/AppShell.jsx

import Sidebar from './Sidebar'
import Header from './Header'
import MainContent from './MainContent'
import '../../styles/layout.css'


function AppShell({
  currentUser,
  currentPage,
  currentToDo,
  sidebarToDos,
  onGoHome,
  onGoSummary,
  onGoDashboard,
  onOpenToDo,
  onLogout,
  children,
}) {
  return (
    <div className='app-shell'>
      <Header currentUser={currentUser} onLogout={onLogout} />
      <div className='app-body'>
        <Sidebar
          currentUser={currentUser}
          currentPage={currentPage}
          currentToDo={currentToDo}
          todos={sidebarToDos}
          onGoHome={onGoHome}
          onGoSummary={onGoSummary}
          onGoDashboard={onGoDashboard}
          onOpenToDo={onOpenToDo}
        />
        <MainContent>{children}</MainContent>
      </div>
    </div>
  )
}

export default AppShell