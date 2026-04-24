// mytodo/clients/web/src/components/task/PriorityBadge.jsx

import { priorityConfig } from "./config/priorityConfig"


function PriorityBadge({ priority }) {
  const config = priorityConfig[priority]

  if (!config) {
    return <span className="badge">{priority ?? '-'}</span>
  }
  return (
    <span className={`badge ${config.className}`}>
      {config.label}
    </span>
  )
}

export default PriorityBadge
