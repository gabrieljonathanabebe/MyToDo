// mytodo/clients/web/src/components/common/Brand.jsx

function Brand({ size = 'md' }) {
  return (
    <div className={`brand brand-${size}`}>
      <span className="brand-mark" />
      <span className="brand-text">MyToDo</span>
    </div>
  )
}

export default Brand
