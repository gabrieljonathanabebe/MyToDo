// todoapp/clients/web/src/api/toDoDetail.js

import { apiRequest } from "./client"


export async function fetchToDoDetail(username, todoId) {
    return apiRequest(`/users/${username}/todos/${todoId}`)
}

export async function createTask(username, todoId, taskData) {
    return apiRequest(`/users/${username}/todos/${todoId}/tasks`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(taskData)
    })
}

export async function deleteTask(username, todoId, taskId) {
    return apiRequest(`/users/${username}/todos/${todoId}/tasks/${taskId}`, {
        method: 'DELETE'
    })
}

export async function updateTaskStatus(username, todoId, taskId, status) {
    return apiRequest(`/users/${username}/todos/${todoId}/tasks/${taskId}/status`, {
        method: 'PATCH',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ status }),
    })
}

