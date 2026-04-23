// todoapp/clients/web/src/components/common/PageHeader.jsx


function PageHeader({ title, icon: Icon = null, actions = null }) {
  return (
    <div className='page-header'>
      <div className='page-title-row'>
        {Icon && (
          <Icon className='page-title-icon' size={24} strokeWidth={2.2} />
        )}
        <h1 className='page-title'>{title}</h1>
      </div>

      {actions && (
        <div className='page-header-actions'>
          {actions}
        </div>
      )}
    </div>
  )
}

export default PageHeader