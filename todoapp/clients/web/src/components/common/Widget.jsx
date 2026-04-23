// todoapp/clients/web/src/components/common/Widget.jsx

3
function Widget({ title, subtitle = '', actions = null, children, className = '' }) {
  return (
    <section className={`widget ${className}`}>
      {/* ===== HEADER ==================================================== */}
      {(title || subtitle || actions) && (
        <div className='widget-header'>
          <div className='widget-header-text'>
            {title && <h3 className='widget-title'>{title}</h3>}
            {subtitle && <p className='widget-subtitle'>{subtitle}</p>}
          </div>

          {actions && (
            <div className='widget-actions'>
              {actions}
            </div>
          )}
        </div>
      )}

      {/* ===== CONTENT =================================================== */}
      <div className='widget-content'>
        {children}
      </div>
    </section>
  )
}

export default Widget
