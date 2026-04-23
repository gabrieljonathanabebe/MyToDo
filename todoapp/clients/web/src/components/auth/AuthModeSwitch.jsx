// todoapp/clients/web/src/components/common/auth/AuthModeSwitch.jsx


function AuthModeSwitch({ mode, onToggle }) {
  return (
    <div className="auth-switch">
      <span className="auth-switch-text">
        {mode === 'login'
          ? 'No account yet?'
          : 'Already have an account?'}
      </span>
      <button
        type="button"
        className="auth-switch-button"
        onClick={onToggle}
      >
        {mode === 'login' ? 'Register' : 'Login'}
      </button>
    </div>
  )
}

export default AuthModeSwitch
