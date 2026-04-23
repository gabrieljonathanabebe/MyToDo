// todoapp/clients/web/src/pages/toDoDetail/ToDoDetailGridView.jsx

import { CheckCircle2, Circle, LayoutGrid } from 'lucide-react'
import EmptyState from '../../components/common/EmptyState'
import Pagination from '../../components/common/Pagination'
import TaskGrid from '../../components/task/TaskGrid'

function ToDoDetailGridView({
  allTasks,
  filteredTasks,
  paginatedTasks,
  statusFilter,
  page,
  totalPages,
  onPrevious,
  onNext,
  onDeleteTask,
  onToggleStatus,
  onUpdateTaskDescription,
  onUpdateTaskPriority,
  onUpdateTaskDue,
}) {
  if (allTasks.length === 0) {
    return (
      <EmptyState
        icon={LayoutGrid}
        title='No tasks yet'
        description='Add your first task to get started in this list.'
      />
    )
  }

  if (filteredTasks.length === 0) {
    if (statusFilter === 'done') {
      return (
        <EmptyState
          icon={CheckCircle2}
          title='No completed tasks yet'
          description='Complete your first task to see it here.'
        />
      )
    }

    if (statusFilter === 'open') {
      return (
        <EmptyState
          icon={Circle}
          title='No open tasks'
          description='All tasks in this list are completed.'
        />
      )
    }
  }

  return (
    <>
      <TaskGrid
        tasks={paginatedTasks}
        onDeleteTask={onDeleteTask}
        onToggleStatus={onToggleStatus}
        onUpdateTaskDescription={onUpdateTaskDescription}
        onUpdateTaskPriority={onUpdateTaskPriority}
        onUpdateTaskDue={onUpdateTaskDue}
      />

      <Pagination
        page={page}
        totalPages={totalPages}
        onPrevious={onPrevious}
        onNext={onNext}
      />
    </>
  )
}

export default ToDoDetailGridView
