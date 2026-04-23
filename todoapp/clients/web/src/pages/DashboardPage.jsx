// todoapp/clients/web/src/pages/DashboardPage.jsx

import Widget from '../components/common/Widget'
import PageHeader from '../components/common/PageHeader'
import {
  getOverviewStats,
  getStatusBreakdown,
  getPriorityBreakdown,
  getAverageLeadTime,
  getMostActiveToDos,
} from '../analytics/metrics'
import { formatDuration } from '../utils/formatters'
import { LayoutDashboard } from 'lucide-react'


function DashboardPage({
  currentUser,
  toDoSummaries = [],
  toDoDetails = [],
}) {
  const overview = getOverviewStats(toDoSummaries, toDoDetails)
  const statusBreakdown = getStatusBreakdown(toDoDetails)
  const priorityBreakdown = getPriorityBreakdown(toDoDetails)
  const averageLeadTime = getAverageLeadTime(toDoDetails)
  const mostActiveToDos = getMostActiveToDos(toDoDetails, 3)
  const totalStatusCount =
    statusBreakdown.open + statusBreakdown.done || 1

  const totalPriorityCount =
    priorityBreakdown.low +
    priorityBreakdown.medium +
    priorityBreakdown.high || 1

  const completionRate =
    overview.totalTasks > 0
      ? Math.round((overview.doneTasks / overview.totalTasks) * 100)
      : 0

  return (
    <div className='dashboard-page'>
      {/* ===== PAGE TITLE ================================================ */}
      <PageHeader title='Dashboard' icon={LayoutDashboard} />

      {/* ===== DASHBOARD GRID ============================================ */}
      <div className='dashboard-grid'>
        {/* ===== KPI OVERVIEW ============================================ */}
        <Widget
          title='Overview'
          subtitle='Your key metrics at a glance'
          className='dashboard-widget dashboard-widget-overview'
        >
          {/* ----- TOTAL TASKS ----- */}
          <div className='dashboard-kpi-grid'>
            <div className='dashboard-kpi-card'>
              <span className='dashboard-kpi-label'>Total tasks</span>
              <strong className='dashboard-kpi-value'>
                {overview.totalTasks}
              </strong>
            </div>
            {/* ----- COMPLETION RATE ----- */}
            <div className='dashboard-kpi-card'>
              <span className='dashboard-kpi-label'>Completion rate</span>
              <strong className='dashboard-kpi-value'>
                {completionRate}%
              </strong>
            </div>
            {/* ----- AVERAGE LEAD TIME ----- */}
            <div className='dashboard-kpi-card'>
              <span className='dashboard-kpi-label'>Average lead time</span>
              <strong className='dashboard-kpi-value'>
                {averageLeadTime !=
                  null ? formatDuration(averageLeadTime) : '-'}
              </strong>
            </div>
            {/* ----- OVERDUE TASKS ----- */}
            <div className='dashboard-kpi-card'>
              <span className='dashboard-kpi-label'>Overdue tasks</span>
              <strong className='dashboard-kpi-value is-danger'>
                {overview.overdueTasks}
              </strong>
            </div>
          </div>
        </Widget>

        {/* ===== STATUS BREAKDOWN ======================================== */}
        <Widget
          title='Status breakdown'
          subtitle='Open versus completed work'
          className='dashboard-widget dashboard-widget-status'
        >
          <div className='dashboard-breakdown-list'>
            <div className='dashboard-breakdown-row'>
              <div className='dashboard-breakdown-header'>
                <span className='dashboard-breakdown-label'>Open</span>
                <span className='dashboard-breakdown-value'>
                  {statusBreakdown.open}
                </span>
              </div>
              <div className='dashboard-bar-track'>
                <div
                  className='dashboard-bar-fill is-open'
                  style={{
                    width: `${(statusBreakdown.open / totalStatusCount) * 100}%`,
                  }}
                />
              </div>
            </div>

            <div className='dashboard-breakdown-row'>
              <div className='dashboard-breakdown-header'>
                <span className='dashboard-breakdown-label'>Done</span>
                <span className='dashboard-breakdown-value'>
                  {statusBreakdown.done}
                </span>
              </div>
              <div className='dashboard-bar-track'>
                <div
                  className='dashboard-bar-fill is-success'
                  style={{
                    width: `${(statusBreakdown.done / totalStatusCount) * 100}%`,
                  }}
                />
              </div>
            </div>
          </div>
        </Widget>

        {/* ===== PRIORITY BREAKDOWN ====================================== */}
        <Widget
          title='Priority breakdown'
          subtitle='Distribution across low, medium and high'
          className='dashboard-widget dashboard-widget-priority'
        >
          <div className='dashboard-breakdown-list'>
            <div className='dashboard-breakdown-row'>
              <div className='dashboard-breakdown-header'>
                <span className='dashboard-breakdown-label'>Low</span>
                <span className='dashboard-breakdown-value'>
                  {priorityBreakdown.low}
                </span>
              </div>
              <div className='dashboard-bar-track'>
                <div
                  className='dashboard-bar-fill is-low'
                  style={{
                    width: `${(priorityBreakdown.low / totalPriorityCount) * 100}%`,
                  }}
                />
              </div>
            </div>

            <div className='dashboard-breakdown-row'>
              <div className='dashboard-breakdown-header'>
                <span className='dashboard-breakdown-label'>Medium</span>
                <span className='dashboard-breakdown-value'>
                  {priorityBreakdown.medium}
                </span>
              </div>
              <div className='dashboard-bar-track'>
                <div
                  className='dashboard-bar-fill is-medium'
                  style={{
                    width: `${(priorityBreakdown.medium / totalPriorityCount) * 100}%`,
                  }}
                />
              </div>
            </div>

            <div className='dashboard-breakdown-row'>
              <div className='dashboard-breakdown-header'>
                <span className='dashboard-breakdown-label'>High</span>
                <span className='dashboard-breakdown-value'>
                  {priorityBreakdown.high}
                </span>
              </div>
              <div className='dashboard-bar-track'>
                <div
                  className='dashboard-bar-fill is-danger'
                  style={{
                    width: `${(priorityBreakdown.high / totalPriorityCount) * 100}%`,
                  }}
                />
              </div>
            </div>
          </div>
        </Widget>
        <Widget
          title='Most active lists'
          subtitle='Lists with the highest amount of open work'
          className='dashboard-widget dashboard-widget-active-lists'
        >
          {mostActiveToDos.length === 0 ? (
            <p className='dashboard-muted-text'>No active lists yet.</p>
          ) : (
            <div className='dashboard-breakdown-list'>
              {mostActiveToDos.map((toDo) => (
                <div key={toDo.id} className='dashboard-breakdown-row'>
                  <div className='dashboard-breakdown-header'>
                    <span className='dashboard-breakdown-label'>{toDo.title}</span>
                    <span className='dashboard-breakdown-value'>
                      {toDo.openTasks} open / {toDo.totalTasks} total
                    </span>
                  </div>

                  <div className='dashboard-bar-track'>
                    <div
                      className='dashboard-bar-fill'
                      style={{
                        width: `${mostActiveToDos[0]?.openTasks
                          ? (toDo.openTasks / mostActiveToDos[0].openTasks) * 100
                          : 0
                          }%`,
                      }}
                    />
                  </div>

                  {toDo.overdueTasks > 0 && (
                    <p className='dashboard-muted-text'>
                      {toDo.overdueTasks} overdue
                    </p>
                  )}
                </div>
              ))}
            </div>
          )}
        </Widget>
      </div>
    </div>
  )
}

export default DashboardPage