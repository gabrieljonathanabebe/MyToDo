// todoapp/clients/web/src/App.jsx

import AppShell from './components/layout/AppShell'
import LoginPage from './pages/LoginPage'
import HomePage from './pages/HomePage'
import ToDoSummaryPage from './pages/ToDoSummaryPage'
import DashboardPage from './pages/DashboardPage'
import ToDoDetailPage from './pages/ToDoDetailPage'
import { useNavigationState } from './hooks/useNavigationState'
import { useToDoSummaries } from './hooks/useToDoSummaries'
import { useSessionState } from './hooks/useSessionState'
import { useEffect } from 'react'


function App() {
	// ===== hooks ============================================================== 
	const { currentUser, loginUser, logoutUser } = useSessionState()
	const { page, currentToDo, navigateTo, openToDo } = useNavigationState()
	const { todos, loading, error, loadTodos, clearTodos } = useToDoSummaries()

	function handleLogin(user) {
		loginUser(user)
		navigateTo('home')
	}

	function handleLogout() {
		logoutUser()
		clearTodos()
		navigateTo('login')
	}

	useEffect(() => {
		if (currentUser) {
			loadTodos(currentUser)
		} else {
			clearTodos()
		}
	}, [currentUser])

	const shellProps = {
		currentUser,
		currentPage: page,
		currentToDo,
		sidebarToDos: todos,
		onGoHome: () => navigateTo('home'),
		onGoSummary: () => navigateTo('summary'),
		onGoDashboard: () => navigateTo('dashboard'),
		onOpenToDo: openToDo,
		onLogout: handleLogout
	}

	function renderPageContent() {
		if (page === 'home') {
			return <HomePage />
		}
		if (page === 'summary') {
			return (
				<ToDoSummaryPage
					currentUser={currentUser}
					todos={todos}
					loading={loading}
					error={error}
					loadTodos={() => loadTodos(currentUser)}
					onOpenToDo={openToDo}
				/>
			)
		}
		if (page === 'dashboard') {
			return <DashboardPage />
		}
		if (page === 'detail') {
			return (
				<ToDoDetailPage
					currentUser={currentUser}
					currentToDo={currentToDo}
					refreshTodos={() => loadTodos(currentUser)}
				/>
			)
		}
		return null
	}

	if (page === 'login') {
		return <LoginPage onLogin={handleLogin} />
	}

	return <AppShell {...shellProps}>{renderPageContent()}</AppShell>
}

export default App