// todoapp/clients/web/src/components/common/ErrorState.jsx

import { AlertCircle } from "lucide-react";


function ErrorState({
  title = 'Something went wrong',
  message = 'An unexpected error occurred. Please try again.'
}) {
  return (
    <div className="state-card surface-card">
      <div className="state-icon-wrap">
        <AlertCircle
          className="state-icon state-icon-danger"
          size={28}
          strokeWidth={2}
        />
      </div>
      <h2 className="state-title">{title}</h2>
      <p className="state-description">{message}</p>
    </div>
  )
}

export default ErrorState