// todoapp/clients/web/src/api/toDoSummary.js

import { apiRequest, deleteRequest, postJson } from "./client"
import { apiRoutes } from "./routes"


export async function fetchToDoSummaries(username) {
    return apiRequest(`/users/${username}/todos`)
}

export async function createToDo(username, title) {
    return postJson(
        apiRoutes.todos.create(username),
        { title },
    )
}


export async function deleteToDo(username, todoId) {
    return deleteRequest(
        apiRoutes.todos.delete(username, todoId)
    )
}
