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

export async function sortTasks(username, todoId, key, reverse = false) {
	return apiRequest(`/users/${username}/todos/${todoId}/sort`, {
		method: 'PATCH',
		headers: {
			'Content-Type': 'application/json'
		},
		body: JSON.stringify({
			key,
			reverse
		})
	})
}


export async function updateTaskDescription(
	username, todoId, taskId, description
) {
	return apiRequest(
		`/users/${username}/todos/${todoId}/tasks/${taskId}/description`, {
		method: 'PATCH',
		headers: {
			'Content-Type': 'application/json',
		},
		body: JSON.stringify({
			description,
		}),
	})
}


export async function updateTaskPriority(
	username, todoId, taskId, priority
) {
	return apiRequest(
		`/users/${username}/todos/${todoId}/tasks/${taskId}/priority`, {
		method: 'PATCH',
		headers: {
			'Content-Type': 'application/json'
		},
		body: JSON.stringify({
			priority,
		}),
	})
}


export async function updateTaskDue(username, todoId, taskId, due) {
	return apiRequest(
		`/users/${username}/todos/${todoId}/tasks/${taskId}/due`, {
		method: 'PATCH',
		headers: {
			'Content-Type': 'application/json'
		},
		body: JSON.stringify({
			due,
		}),
	})
}