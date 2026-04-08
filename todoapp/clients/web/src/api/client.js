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