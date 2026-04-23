// todoapp/clients/web/src/components/common/Button.jsx


function Button({
  children,
  onClick,
  variant = 'primary',
  type = 'button',
  className = '',
  disabled = false
}) {
  const baseClassName = `btn btn-${variant}`
  const finalClassName = `${baseClassName} ${className}`.trim()

  return (
    <button
      type={type}
      className={finalClassName}
      onClick={onClick}
      disabled={disabled}
    >
      {children}
    </button>
  )
}


export default Button
