// todoapp/clients/web/src/api/auth.js

import { apiRequest } from './client'


export async function login(username, password) {
    return apiRequest('/auth/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            username,
            password,
        }),
    })
}

export async function register(username, password) {
    return apiRequest('/auth/register', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            username,
            password,
        }),
    })
}