// todoapp/clients/web/src/api/client.js

import { API_BASE_URL } from "./config";


export async function apiRequest(path, options = {}) {
  const response = await fetch(`${API_BASE_URL}${path}`, options)
  let data = null
  try {
    data = await response.json()
  } catch {
    data = null
  }
  if (!response.ok) {
    throw new Error(data?.detail || "Request failed.")
  }
  return data
}


export async function postJson(path, payload) {
  return apiRequest(path, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(payload),
  })
}


export async function patchJson(path, payload) {
  return apiRequest(path, {
    method: 'PATCH',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(payload),
  })
}


export async function deleteRequest(path) {
  return apiRequest(path, {
    method: 'DELETE',
  })
}


export async function getRequest(path) {
  return apiRequest(path)
}