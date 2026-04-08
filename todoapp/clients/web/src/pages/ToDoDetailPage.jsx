// todoapp/clients/web/src/pages/ToDoDetailPage.jsx

import { ListChecks } from 'lucide-react'
import EmptyState from '../components/common/EmptyState'
import { useToDoDetail } from '../hooks/useToDoDetail'
import TaskList from '../components/task/TaskList'
import CreateTaskForm from '../components/task/CreateTaskForm'
import Pagination from '../components/common/Pagination'
import LoadingState from '../components/common/LoadingState'
import ErrorState from '../components/common/ErrorState'
import { usePagination } from '../hooks/usePagination'


function ToDoDetailPage({ currentUser, currentToDo }) {
	const {
		toDoDetail,
		error,
		description,
		setDescription,
		priority,
		setPriority,
		due,
		setDue,
		createError,
		handleCreateTask
	} = useToDoDetail(currentUser, currentToDo)

	const tasks = toDoDetail?.tasks ?? []
	const {
		page,
		totalPages,
		paginatedItems: paginatedTasks,
		goPrevious,
		goNext,

	} = usePagination(tasks, 6)

	if (error) {
		return <ErrorState message={error} />
	}

	if (!toDoDetail) {
		return (
			<LoadingState
				title='Loading To-Do'
				message='Fetching your tasks...'
			/>
		)
	}

	return (
		<div>
			<h1 className='page-title'>{toDoDetail.title}</h1>
			<CreateTaskForm
				description={description}
				onDescriptionChange={setDescription}
				priority={priority}
				onPriorityChange={setPriority}
				due={due}
				onDueChange={setDue}
				onSubmit={handleCreateTask}
				error={createError}
			/>
			{tasks.length === 0 ? (
				<EmptyState
					icon={ListChecks}
					title='No tasks yet'
					description='Add your first task to get started in this list.'
				/>
			) : (
				<>
					<TaskList tasks={paginatedTasks} />
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

export default ToDoDetailPage