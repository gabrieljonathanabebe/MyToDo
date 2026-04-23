// todoapp/clients/web/src/components/common/auth/AuthHeader.jsx

function AuthHeader({ mode }) {
  return (
    <div className="auth-header">
      <h1 className="auth-title">
        {mode === 'login' ? 'Welcome back' : 'Create account'}
      </h1>
      <p className="auth-subtitle">
        {mode === 'login'
          ? 'Sign in to continue to your workspace.'
          : 'Create your account to start organizing your tasks.'}
      </p>
    </div>
  )
}

export default AuthHeader
