// todoapp/clients/web/src/App.jsx

import AppShell from './components/layout/AppShell'
import LoginPage from './pages/LoginPage'
import HomePage from './pages/HomePage'
import ToDoSummaryPage from './pages/ToDoSummaryPage'
import DashboardPage from './pages/DashboardPage'
import ToDoDetailPage from './pages/toDoDetail/ToDoDetailPage'
import { useWorkspaceData } from './hooks/useWorkspaceData'
import { useNavigationState } from './hooks/useNavigationState'
import { useSessionState } from './hooks/useSessionState'
import { useEffect } from 'react'


function App() {
	// ===== HOOKS ==========================================================
	const { currentUser, loginUser, logoutUser } = useSessionState()
	const { page, currentToDo, navigateTo, openToDo } = useNavigationState()

	const {
		toDoSummaries,
		toDoDetails,
		loading,
		error,
		loadWorkspace,
		refreshSummaries,
		refreshToDo,
		getToDoDetail,
		clearWorkspace,
	} = useWorkspaceData()

	function handleLogin(user) {
		loginUser(user)
		navigateTo('home')
	}

	function handleLogout() {
		logoutUser()
		clearWorkspace()
		navigateTo('login')
	}

	useEffect(() => {
		if (currentUser) {
			loadWorkspace(currentUser)
		} else {
			clearWorkspace()
		}
	}, [currentUser])

	const shellProps = {
		currentUser,
		currentPage: page,
		currentToDo,
		toDoSummaries,
		onGoHome: () => navigateTo('home'),
		onGoSummary: () => navigateTo('summary'),
		onGoDashboard: () => navigateTo('dashboard'),
		onOpenToDo: openToDo,
		onLogout: handleLogout,
	}

	function renderPageContent() {
		if (page === 'home') {
			return (
				<HomePage
					currentUser={currentUser}
					toDoSummaries={toDoSummaries}
					toDoDetails={toDoDetails}
				/>
			)
		}

		if (page === 'summary') {
			return (
				<ToDoSummaryPage
					currentUser={currentUser}
					todos={toDoSummaries}
					loading={loading}
					error={error}
					loadTodos={() => refreshSummaries(currentUser)}
					onOpenToDo={openToDo}
				/>
			)
		}

		if (page === 'dashboard') {
			return (
				<DashboardPage
					currentUser={currentUser}
					toDoSummaries={toDoSummaries}
					toDoDetails={toDoDetails}
				/>
			)
		}

		if (page === 'detail') {
			return (
				<ToDoDetailPage
					currentUser={currentUser}
					currentToDo={currentToDo}
					initialToDoDetail={getToDoDetail(currentToDo?.id)}
					refreshToDos={() => refreshSummaries(currentUser)}
					refreshCurrentToDo={() => refreshToDo(currentUser, currentToDo?.id)}
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