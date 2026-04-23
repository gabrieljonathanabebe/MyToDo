// todoapp/clients/web/src/api/routes.js


export const apiRoutes = {
  auth: {
    login: () => '/auth/login',
    register: () => '/auth/register',
  },
  todos: {
    list: (username) => `/users/${username}/todos`,
    detail: (username, todoId) => `/users/${username}/todos/${todoId}`,
    create: (username) => `/users/${username}/todos`,
    delete: (username, todoId) => `/users/${username}/todos/${todoId}`,

    sort: (username, todoId) => `/users/${username}/todos/${todoId}/sort`,

    tasks: {
      create: (username, todoId) => `/users/${username}/todos/${todoId}/tasks`,
      delete: (username, todoId, taskId) =>
        `/users/${username}/todos/${todoId}/tasks/${taskId}`,
      updateStatus: (username, todoId, taskId) =>
        `/users/${username}/todos/${todoId}/tasks/${taskId}/status`,
      updateDescription: (username, todoId, taskId) =>
        `/users/${username}/todos/${todoId}/tasks/${taskId}/description`,
      updatePriority: (username, todoId, taskId) =>
        `/users/${username}/todos/${todoId}/tasks/${taskId}/priority`,
      updateDue: (username, todoId, taskId) =>
        `/users/${username}/todos/${todoId}/tasks/${taskId}/due`
    },
  }
}
