// mytodo/clients/web/src/components/task/config/priorityConfig.js


export const priorityConfig = {
  low: {
    label: 'Low',
    className: 'badge-gray',
    value: 1,
  },
  medium: {
    label: 'Medium',
    className: 'badge-yellow',
    value: 2,
  },
  high: {
    label: 'High',
    className: 'badge-red',
    value: 3,
  },
}

export const priorityOptions = Object.entries(priorityConfig).map(
  ([key, config]) => ({
    key,
    ...config,
  })
)
