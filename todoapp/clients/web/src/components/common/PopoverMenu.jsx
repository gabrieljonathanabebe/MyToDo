// todoapp/clients/web/src/components/common/PopoverMenu.jsx

import { useRef } from "react";
import useClickOutside from '../../hooks/useClickOutside'


function PopoverMenu({
  show,
  onClose,
  trigger,
  children,
  anchorClassName = '',
  menuClassName = '',
  placement = 'bottom'
}) {
  const menuRef = useRef(null)

  useClickOutside(menuRef, () => {
    if (show) onClose()
  })
  return (
    <div className={`popover-anchor ${anchorClassName}`.trim()} ref={menuRef}>
      {trigger}
      {show && (
        <div
          className={`
            popover-menu 
            surface-dropdown 
            ${placement === 'top' ? 'popover-menu--top' : ''}
            ${menuClassName}
            `.trim()}
        >
          {children}
        </div>
      )}
    </div>
  )
}


export default PopoverMenu