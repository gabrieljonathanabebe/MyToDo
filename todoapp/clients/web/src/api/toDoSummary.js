// todoapp/clients/web/src/api/toDoSummary.js

import { apiRequest } from "./client"


export async function fetchToDoSummaries(username) {
    return apiRequest(`/users/${username}/todos`)
}

export async function createToDo(username, title) {
    return apiRequest(`/users/${username}/todos`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ title }),
    })
}

export async function deleteToDo(username, todoId) {
    return apiRequest(`/users/${username}/todos/${todoId}`, {
        method: 'DELETE'
    })
}