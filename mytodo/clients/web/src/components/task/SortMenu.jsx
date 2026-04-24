// mytodo/clients/web/src/components/task/SortMenu.jsx

import { ArrowUpDown, ArrowDownAZ, CalendarDays, Flag } from 'lucide-react'
import PopoverMenu from '../common/PopoverMenu'


function SortMenu({
  show,
  sortKey,
  sortReverse,
  onToggle,
  onSelect,
  onClose,
}) {
  return (
    <PopoverMenu
      show={show}
      onClose={onClose}
      trigger={
        <button
          type='button'
          className={`icon-action icon-action-plain ${show ? 'is-active' : ''}`}
          onClick={onToggle}
          aria-label='Open sort options'
          title='Sort tasks'
        >
          <ArrowUpDown size={20} strokeWidth={2} />
        </button>
      }
      menuClassName='sort-menu'
    >
      <button
        type='button'
        className={`sort-menu-item ${sortKey === 'due' ? 'is-active' : ''}`}
        onClick={() => onSelect('due')}
      >
        <span className='sort-menu-label'>
          <CalendarDays size={15} strokeWidth={2} />
          <span>Due date</span>
        </span>
        {sortKey === 'due' && (
          <span className='sort-menu-order'>{sortReverse ? '↓' : '↑'}</span>
        )}
      </button>

      <button
        type='button'
        className={`sort-menu-item ${sortKey === 'priority' ? 'is-active' : ''}`}
        onClick={() => onSelect('priority')}
      >
        <span className='sort-menu-label'>
          <Flag size={15} strokeWidth={2} />
          <span>Priority</span>
        </span>
        {sortKey === 'priority' && (
          <span className='sort-menu-order'>{sortReverse ? '↓' : '↑'}</span>
        )}
      </button>

      <button
        type='button'
        className={`sort-menu-item ${sortKey === 'description' ? 'is-active' : ''}`}
        onClick={() => onSelect('description')}
      >
        <span className='sort-menu-label'>
          <ArrowDownAZ size={15} strokeWidth={2} />
          <span>Description</span>
        </span>
        {sortKey === 'description' && (
          <span className='sort-menu-order'>{sortReverse ? '↓' : '↑'}</span>
        )}
      </button>
    </PopoverMenu>
  )
}

export default SortMenu
