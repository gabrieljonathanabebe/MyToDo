// mytodo/clients/web/src/pages/LoginPage.jsx

import '../styles/features/auth.css'
import Panel from '../components/common/Panel'
import Button from '../components/common/Button'
import AuthHeader from '../components/auth/AuthHeader'
import AuthModeSwitch from '../components/auth/AuthModeSwitch'
import { useAuthForm } from '../hooks/useAuthForm'
import Brand from '../components/common/Brand'


function LoginPage({ onLogin }) {
	const {
		username,
		setUsername,
		password,
		setPassword,
		error,
		mode,
		handleSubmit,
		handleToggleMode,
	} = useAuthForm(onLogin)

	return (
		<div className='auth-shell'>
			<Panel className='auth-card'>
				<Brand size='lg' />

				<AuthHeader mode={mode} />

				<form className='auth-form' onSubmit={handleSubmit}>
					<input
						className='form-control form-input'
						type='text'
						placeholder='Username'
						value={username}
						onChange={(e) => setUsername(e.target.value)}
					/>

					<input
						className='form-control form-input'
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

				<AuthModeSwitch mode={mode} onToggle={handleToggleMode} />
			</Panel>
		</div>
	)
}

export default LoginPage
