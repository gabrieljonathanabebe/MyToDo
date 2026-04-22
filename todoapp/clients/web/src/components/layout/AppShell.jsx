// todoapp/clients/web/src/components/layout/AppShell.jsx

import Sidebar from './Sidebar'
import Header from './Header'
import MainContent from './MainContent'
import '../../styles/primitives/layout.css'


function AppShell({
  currentUser,
  currentPage,
  currentToDo,
  toDoSummaries = [],
  onGoHome,
  onGoSummary,
  onGoDashboard,
  onOpenToDo,
  onLogout,
  children,
}) {
  console.log('AppShell toDoSummaries', toDoSummaries)
  return (
    <div className='app-shell'>
      <Header currentUser={currentUser} onLogout={onLogout} />
      <div className='app-body'>
        <Sidebar
          currentUser={currentUser}
          currentPage={currentPage}
          currentToDo={currentToDo}
          toDoSummaries={toDoSummaries}
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