// todoapp/clients/web/src/pages/HomePage.jsx

import Widget from '../components/common/Widget'
import {
  getOverviewStats,
  getUpcomingTasks,
  getRecentlyUpdatedToDos,
} from '../analytics/metrics'
import {
  formatDueDate,
  formatDaysLeft,
  formatRelativeDatetime,
} from '../utils/formatters'
import { House } from 'lucide-react'
import PageHeader from '../components/common/PageHeader'


function HomePage({
  currentUser,
  toDoSummaries = [],
  toDoDetails = [],
}) {
  const overview = getOverviewStats(toDoSummaries, toDoDetails)
  const upcomingTasks = getUpcomingTasks(toDoDetails, 3)
  const recentTodos = getRecentlyUpdatedToDos(toDoSummaries, 3)


  return (
    <div className='home-page'>
      {/* ===== PAGE TITLE ================================================= */}
      <PageHeader title='Home' icon={House} />
      {/* ===== HOME GRID ================================================== */}
      <div className='home-grid'>
        {/* ===== WELCOME ================================================== */}
        <Widget
          title={`Welcome back, ${currentUser?.username ?? 'there'}`}
          subtitle='Here is a quick overview of your current workspace.'
          className='home-widget home-widget-welcome'
        >
          <div className='home-welcome-copy'>
            <p className='home-muted-text'>
              Stay focused on upcoming and overdue work.
            </p>
          </div>
        </Widget>

        {/* ===== OVERVIEW ================================================= */}
        <Widget
          title='Overview'
          subtitle='Your most important numbers at a glance'
          className='home-widget home-widget-overview'
        >
          <div className='home-overview-stats'>
            {/* ----- OPEN TASKS ----- */}
            <div className='home-stat-card'>
              <span className='home-stat-label'>Open tasks</span>
              <strong className='home-stat-value'>{overview.openTasks}</strong>
            </div>

            {/* ----- DONE TASKS ----- */}
            <div className='home-stat-card'>
              <span className='home-stat-label'>Done tasks</span>
              <strong className='home-stat-value'>{overview.doneTasks}</strong>
            </div>

            {/* ----- OVERDUE TASKS ----- */}
            <div className='home-stat-card'>
              <span className='home-stat-label'>Overdue tasks</span>
              <strong className='home-stat-value is-danger'>
                {overview.overdueTasks}
              </strong>
            </div>

            {/* ----- TOTAL TODOS ----- */}
            <div className='home-stat-card'>
              <span className='home-stat-label'>To-do lists</span>
              <strong className='home-stat-value'>{overview.totalToDos}</strong>
            </div>
          </div>
        </Widget>

        {/* ===== UPCOMING TASKS ========================================== */}
        <Widget
          title='Upcoming tasks'
          subtitle='What needs attention next'
          className='home-widget home-widget-upcoming'
        >
          {upcomingTasks.length === 0 ? (
            <p className='home-muted-text'>No upcoming tasks with due dates.</p>
          ) : (
            <div className='home-list'>
              {upcomingTasks.map((task) => (
                <div key={`${task.toDoId}-${task.id}`} className='home-list-item'>
                  <div className='home-list-main'>
                    <div className='home-list-title'>{task.description}</div>
                    <div className='home-list-subtitle'>
                      {formatDueDate(task.due)} · {formatDaysLeft(task.days_left)}
                    </div>
                  </div>
                </div>
              ))}
            </div>
          )}
        </Widget>

        {/* ===== RECENTLY UPDATED TODOS ================================== */}
        <Widget
          title='Recently updated lists'
          subtitle='Your latest activity'
          className='home-widget home-widget-recent'
        >
          {recentTodos.length === 0 ? (
            <p className='home-muted-text'>No recent list activity yet.</p>
          ) : (
            <div className='home-list'>
              {recentTodos.map((todo) => (
                <div key={todo.id} className='home-list-item'>
                  <div className='home-list-main'>
                    <div className='home-list-title'>{todo.title}</div>
                    <div className='home-list-subtitle'>
                      Updated {formatRelativeDatetime(todo.updated_at)}
                    </div>
                  </div>
                </div>
              ))}
            </div>
          )}
        </Widget>
      </div>
    </div>
  )
}

export default HomePage