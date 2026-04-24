// mytodo/clients/web/src/api/auth.js

import { apiRequest, postJson } from './client'
import { apiRoutes } from './routes'


export async function login(username, password) {
    return postJson(
        apiRoutes.auth.login(),
        { username, password }
    )
}

export async function register(username, password) {
    return postJson(
        apiRoutes.auth.register(),
        { username, password }
    )
}
