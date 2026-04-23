// todoapp/clients/web/src/components/common/Pagination.jsx

import Button from "./Button";


function Pagination({ page, totalPages, onPrevious, onNext }) {
  return (
    <div className="pagination">
      <Button
        type="button"
        variant="secondary"
        className="btn-sm btn-wide"
        disabled={page === 1}
        onClick={onPrevious}
      >
        Previous
      </Button>
      <span className="pagination-info">
        Page {page} of {totalPages || 1}
      </span>
      <Button
        type="button"
        variant="secondary"
        className="btn-sm btn-wide"
        disabled={page === totalPages || totalPages === 0}
        onClick={onNext}
      >
        Next
      </Button>
    </div>
  )
}

export default Pagination
