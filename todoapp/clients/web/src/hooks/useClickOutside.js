// todoapp/clients/web/src/hooks/useClickOutside.js

import { useEffect } from "react";


function useClickOutside(ref, onClose) {
  useEffect(() => {
    function handleClick(event) {
      if (ref.current && !ref.current.contains(event.target)) {
        onClose()
      }
    }

    document.addEventListener('mousedown', handleClick)

    return () => {
      document.removeEventListener('mousedown', handleClick)
    }
  }, [ref, onClose])
}


export default useClickOutside