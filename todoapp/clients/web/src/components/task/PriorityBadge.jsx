// todoapp/clients/web/src/components/task/PriorityBadge.jsx


function PriorityBadge({ priority }) {
  if (priority === 'low') {
    return <span className="badge badge-gray">Low</span>
  }
  if (priority === 'medium') {
    return <span className="badge badge-yellow">Medium</span>
  }
  if (priority === 'high') {
    return <span className="badge badge-red">High</span>
  }
  return <span className="badge">{priority ?? '-'}</span>
}

export default PriorityBadge