// mytodo/clients/web/src/hooks/usePagination.js

import { useState, useEffect } from "react";


export function usePagination(items, itemsPerPage = 5) {
  const [page, setPage] = useState(1)
  const totalPages = Math.ceil(items.length / itemsPerPage)
  const startIndex = (page - 1) * itemsPerPage
  const paginatedItems = items.slice(startIndex, startIndex + itemsPerPage)

  function goPrevious() {
    if (page > 1) setPage(page - 1)
  }

  function goNext() {
    if (page < totalPages) setPage(page + 1)
  }

  useEffect(() => {
    if (page > totalPages) {
      setPage(totalPages || 1)
    }
  }, [items, totalPages, page])

  return {
    page, totalPages, paginatedItems, goPrevious, goNext, setPage
  }
}
