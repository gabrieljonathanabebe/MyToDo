// todoapp/clients/web/src/components/task/StatusBadge.jsx

function StatusBadge({ status }) {
  if (status === 'open') {
    return <span className="badge badge-purple">Open</span>
  }
  if (status === 'done') {
    return <span className="badge badge-green">Done</span>
  }
  if (status === 'cancelled') {
    return <span className="badge badge-red">Cancelled</span>
  }
  return <span className="badge badge-gray">{status ?? '-'}</span>
}

export default StatusBadge
