// todoapp/clients/web/src/pages/ToDoSummaryPage.jsx

import { ListTodo } from 'lucide-react'
import EmptyState from '../components/common/EmptyState.jsx'
import LoadingState from '../components/common/LoadingState.jsx'
import ErrorState from '../components/common/ErrorState.jsx'
import ToDoLists from '../components/todo/ToDoLists.jsx'
import CreateToDoForm from '../components/todo/CreateToDoForm.jsx'
import Pagination from '../components/common/Pagination.jsx'
import { usePagination } from '../hooks/usePagination.js'
import { useToDoSummaryActions } from '../hooks/useToDoSummaryActions.js'
import PageHeader from '../components/common/PageHeader.jsx'


function ToDoSummaryPage({
	currentUser, todos, loading, error, loadTodos, onOpenToDo
}) {
	const {
		error: actionError,
		newTitle,
		setNewTitle,
		createError,
		handleCreateToDo,
		handleDeleteToDo,
	} = useToDoSummaryActions(currentUser, loadTodos)

	const {
		page,
		totalPages,
		paginatedItems: paginatedTodos,
		goPrevious,
		goNext
	} = usePagination(todos, 5)

	if (error) {
		return <ErrorState message={error} />
	}

	if (loading) {
		return (
			<LoadingState
				title='Loading To-Dos'
				message='Fetching your lists...'
			/>
		)
	}

	return (
		<div>
			<PageHeader title='Summary' icon={ListTodo} />
			<CreateToDoForm
				title={newTitle}
				onTitleChange={setNewTitle}
				onSubmit={handleCreateToDo}
				error={createError}
			/>
			{todos.length === 0 ? (
				<EmptyState
					icon={ListTodo}
					title='No To-Dos yet'
					description='Create your first list to start organizing your tasks.'
				/>
			) : (
				<>
					<ToDoLists
						todos={paginatedTodos}
						onOpenToDo={onOpenToDo}
						onDeleteToDo={handleDeleteToDo}
					/>
					<Pagination
						page={page}
						totalPages={totalPages}
						onPrevious={goPrevious}
						onNext={goNext}
					/>
				</>
			)}
		</div>
	)
}
export default ToDoSummaryPage
