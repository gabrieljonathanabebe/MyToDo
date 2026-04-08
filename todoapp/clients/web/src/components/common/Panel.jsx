// todoapp/clients/web/src/components/common/Panel.jsx


function Panel({ children, className = '' }) {
  return (
    <div className={`panel ${className}`.trim()}>
      {children}
    </div>
  )
}

export default Panel