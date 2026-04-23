// todoapp/clients/web/src/components/common/PageToolbar.jsx


function PageToolbar({ title, titleIcon: TitleIcon, viewControls, children }) {
  return (
    <div className="page-toolbar-surface">
      <div className="page-toolbar-left">
        <div className="page-toolbar-title-row">
          <div className="page-toolbar-title-wrap">
            {TitleIcon && (
              <span className="page-toolbar-title-icon">
                <TitleIcon size={22} strokeWidth={2} />
              </span>
            )}
            <h1 className="page-toolbar-title">{title}</h1>
          </div>

          {viewControls && (
            <div className="page-toolbar-view-controls surface-control">
              {viewControls}
            </div>
          )}
        </div>
      </div>

      <div className="page-toolbar-actions">
        {children}
      </div>
    </div>
  )
}

export default PageToolbar
