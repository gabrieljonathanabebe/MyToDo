// todoapp/clients/web/src/api/toDoDetail.js

import { apiRequest, deleteRequest, patchJson, postJson } from "./client"
import { apiRoutes } from "./routes"


export async function fetchToDoDetail(username, todoId) {
	return apiRequest(`/users/${username}/todos/${todoId}`)
}

export async function createTask(username, todoId, taskData) {
	return postJson(
		apiRoutes.todos.tasks.create(username, todoId),
		{ taskData }
	)
}


export async function deleteTask(username, todoId, taskId) {
	return deleteRequest(
		apiRoutes.todos.tasks.delete(username, todoId, taskId)
	)
}


export async function updateTaskStatus(username, todoId, taskId, status) {
	return patchJson(
		apiRoutes.todos.tasks.updateStatus(username, todoId, taskId),
		{ status }
	)
}


export async function sortTasks(username, todoId, key, reverse = false) {
	return patchJson(
		apiRoutes.todos.sort(username, todoId),
		{ key, reverse }
	)
}


export async function updateTaskDescription(
	username, todoId, taskId, description
) {
	return patchJson(
		apiRoutes.todos.tasks.updateDescription(username, todoId, taskId),
		{ description }
	)
}


export async function updateTaskPriority(username, todoId, taskId, priority) {
	return patchJson(
		apiRoutes.todos.tasks.updatePriority(username, todoId, taskId),
		{ priority }
	)
}


export async function updateTaskDue(username, todoId, taskId, due) {
	return patchJson(
		apiRoutes.todos.tasks.updateDue(username, todoId, taskId),
		{ due }
	)
}