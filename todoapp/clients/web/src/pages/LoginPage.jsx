// todoapp/clients/web/src/pages/LoginPage.jsx

import { useState } from 'react'
import { login, register } from '../api/auth'
import '../styles/auth.css'
import Panel from '../components/common/Panel'
import Button from '../components/common/Button'


function LoginPage({ onLogin }) {
    const [username, setUsername] = useState('')
    const [password, setPassword] = useState('')
    const [error, setError] = useState('')
    const [mode, setMode] = useState('login')


    async function handleSubmit(e) {
        e.preventDefault()
        setError('')
        try {
            const user =
                mode === 'login'
                    ? await login(username, password)
                    : await register(username, password)

            onLogin(user)
        } catch (err) {
            setError(err.message)
        }
    }

    function handleToggleMode() {
        setMode((prev) => (prev === 'login' ? 'register' : 'login'))
        setError('')
    }

    return (
        <div className='auth-shell'>
            <Panel className='auth-card'>
                <div className='auth-brand'>
                    <span className='brand-mark' />
                    <span className='brand-text'>MyToDo</span>
                </div>
                <div className='auth-header'>
                    <h1 className='auth-title'>
                        {mode === 'login' ? 'Welcome back' : 'Create account'}
                    </h1>
                    <p className='auth-subtitle'>
                        {mode === 'login'
                            ? 'Sign in to continue to your workspace.'
                            : 'Create your account to start organizing your tasks.'
                        }
                    </p>
                </div>
                <form className='auth-form' onSubmit={handleSubmit}>
                    <input
                        className='form-input'
                        type='text'
                        placeholder='Username'
                        value={username}
                        onChange={(e) => setUsername(e.target.value)}
                    />
                    <input
                        className='form-input'
                        type='password'
                        placeholder='Password'
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                    />
                    {error && <p className='form-error'>{error}</p>}
                    <Button type='submit' className='auth-submit'>
                        {mode === 'login' ? 'Login' : 'Create account'}
                    </Button>
                </form>
                <div className='auth-switch'>
                    <span className='auth-switch-text'>
                        {mode === 'login'
                            ? 'No account yet?'
                            : 'Already have an account?'}
                    </span>
                    <button
                        type='button'
                        className='auth-switch-button'
                        onClick={handleToggleMode}
                    >
                        {mode === 'login' ? 'Register' : 'Login'}
                    </button>
                </div>
            </Panel>
        </div>
    )
}


export default LoginPage