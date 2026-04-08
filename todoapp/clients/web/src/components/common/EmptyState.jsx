// todoapp/clients/web/src/components/common/EmptyState.jsx


function EmptyState({ icon, title, description }) {
  const Icon = icon

  return (
    <div className="state-card panel">
      <div className="empty-state-icon-wrap">
        <Icon className="state-icon state-icon-primary" size={28} strokeWidth={2} />
      </div>
      <h2 className="empty-state-title">{title}</h2>
      <p className="empty-state-description">{description}</p>
    </div>
  )
}

export default EmptyState