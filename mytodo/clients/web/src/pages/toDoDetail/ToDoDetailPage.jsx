// mytodo/clients/web/src/pages/toDoDetail/ToDoDetailPage.jsx

import {
	Plus,
	List,
	LayoutGrid,
	ClipboardList
} from 'lucide-react'
import { useState } from 'react'
import { useToDoDetail } from '../../hooks/useToDoDetail'
import CreateTaskForm from '../../components/task/CreateTaskForm'
import LoadingState from '../../components/common/LoadingState'
import ErrorState from '../../components/common/ErrorState'
import { usePagination } from '../../hooks/usePagination'
import PageToolbar from '../../components/common/PageToolbar'
import ToDoDetailListView from './ToDoDetailListView'
import ToDoDetailGridView from './ToDoDetailGridView'
import SortMenu from '../../components/task/SortMenu'


function ToDoDetailPage({
	currentUser,
	currentToDo,
	initialToDoDetail,
	refreshToDos,
	refreshCurrentToDo,
}) {
	const {
		toDoDetail,
		error,
		description,
		setDescription,
		priority,
		setPriority,
		due,
		setDue,
		notes,
		setNotes,
		showNotes,
		setShowNotes,
		createError,
		handleCreateTask,
		handleDeleteTask,
		handleToggleTaskStatus,
		handleSortTasks,
		handleUpdateTaskDescription,
		handleUpdateTaskPriority,
		handleUpdateTaskDue,
	} = useToDoDetail(
		currentUser, currentToDo, initialToDoDetail,
		refreshToDos, refreshCurrentToDo
	)

	const [showCreateTaskForm, setShowCreateTaskForm] = useState(false)
	const [viewMode, setViewMode] = useState('list')
	const [statusFilter, setStatusFilter] = useState('all')

	const [showSortMenu, setShowSortMenu] = useState(false)
	const [sortKey, setSortKey] = useState('due')
	const [sortReverse, setSortReverse] = useState(false)

	const tasks = toDoDetail?.tasks ?? []

	const filteredTasks = tasks.filter((task => {
		if (statusFilter === 'all') return true
		return task.status === statusFilter
	}))

	async function handleSortSelection(key) {
		let nextReverse = false
		if (key === sortKey) {
			nextReverse = !sortReverse
		}
		setSortKey(key)
		setSortReverse(nextReverse)
		await handleSortTasks(key, nextReverse)
		setShowSortMenu(false)
	}

	const {
		page,
		totalPages,
		paginatedItems: paginatedTasks,
		goPrevious,
		goNext,
	} = usePagination(filteredTasks, 7)

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
			<PageToolbar
				title={toDoDetail.title}
				titleIcon={ClipboardList}
				viewControls={
					<>
						<button
							type="button"
							className={
								`segmented-control-item view-switch-button
								${viewMode === 'list' ? 'is-active' : ''}`}
							onClick={() => setViewMode('list')}
							aria-label="List view"
							title="List view"
						>
							<List size={18} strokeWidth={2} />
						</button>

						<button
							type="button"
							className={
								`segmented-control-item view-switch-button
								${viewMode === 'grid' ? 'is-active' : ''}`}
							onClick={() => setViewMode('grid')}
							aria-label="Grid view"
							title="Grid view"
						>
							<LayoutGrid size={18} strokeWidth={2} />
						</button>
					</>
				}
			>
				<button
					type="button"
					className="icon-action icon-action-plain"
					onClick={() => setShowCreateTaskForm((prev) => !prev)}
					aria-label="Add task"
					title="Add task"
				>
					<Plus size={20} strokeWidth={2} />
				</button>
				<SortMenu
					show={showSortMenu}
					sortKey={sortKey}
					sortReverse={sortReverse}
					onToggle={() => setShowSortMenu((prev) => !prev)}
					onSelect={handleSortSelection}
					onClose={() => setShowSortMenu(false)}
				/>
			</PageToolbar>
			{showCreateTaskForm && (
				<div className='detail-create-task-wrap'>
					<CreateTaskForm
						description={description}
						onDescriptionChange={setDescription}
						priority={priority}
						onPriorityChange={setPriority}
						due={due}
						onDueChange={setDue}
						notes={notes}
						onNotesChange={setNotes}
						showNotes={showNotes}
						onToggleNotes={() => setShowNotes((prev) => !prev)}
						onSubmit={handleCreateTask}
						error={createError}
					/>
				</div>
			)}
			<div className='detail-filter-row'>
				<div className='task-filter surface-control'>
					<button
						className={
							`segmented-control-item filter-pill
							${statusFilter === 'all' ? 'is-active' : ''}`}
						onClick={() => setStatusFilter('all')}
					>
						All
					</button>
					<button
						className={
							`segmented-control-item filter-pill
							${statusFilter === 'open' ? 'is-active' : ''}`}
						onClick={() => setStatusFilter('open')}
					>
						Open
					</button>
					<button
						className={
							`segmented-control-item filter-pill
							${statusFilter === 'done' ? 'is-active' : ''}`}
						onClick={() => setStatusFilter('done')}
					>
						Done
					</button>
				</div>
			</div>
			<div className='detail-view-content'>
				{viewMode === 'list' && (
					<ToDoDetailListView
						allTasks={tasks}
						filteredTasks={filteredTasks}
						paginatedTasks={paginatedTasks}
						statusFilter={statusFilter}
						page={page}
						totalPages={totalPages}
						onPrevious={goPrevious}
						onNext={goNext}
						onDeleteTask={handleDeleteTask}
						onToggleStatus={handleToggleTaskStatus}
						onUpdateTaskDescription={handleUpdateTaskDescription}
						onUpdateTaskPriority={handleUpdateTaskPriority}
						onUpdateTaskDue={handleUpdateTaskDue}
					/>
				)}
				{viewMode === 'grid' && (
					<ToDoDetailGridView
						allTasks={tasks}
						filteredTasks={filteredTasks}
						paginatedTasks={paginatedTasks}
						statusFilter={statusFilter}
						page={page}
						totalPages={totalPages}
						onPrevious={goPrevious}
						onNext={goNext}
						onDeleteTask={handleDeleteTask}
						onToggleStatus={handleToggleTaskStatus}
						onUpdateTaskDescription={handleUpdateTaskDescription}
						onUpdateTaskPriority={handleUpdateTaskPriority}
						onUpdateTaskDue={handleUpdateTaskDue}
					/>
				)}
			</div>
		</div>
	)
}

export default ToDoDetailPage
