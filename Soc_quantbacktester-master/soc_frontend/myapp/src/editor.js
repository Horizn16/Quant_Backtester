import React, { useState } from 'react';


function Edit() {
  const [text, setText] = useState('');

  return (
    <div className='container-fluid'>
        <h5> Write Your python code here :</h5>
 <div style={styles.container}>
        
        <textarea
          value={text}
          onChange={(e) => setText(e.target.value)}
          style={styles.textarea}
          placeholder="Start typing here..."
        />
      </div>
    </div>
   
  );
}

const styles = {
  container: {
    height: '100vh',
    display: 'flex',
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#f5f5f5',
    padding: '20px',
    boxSizing: 'border-box',
  },
  textarea: {
    width: '100%',
    height: '100%',
    padding: '20px',
    fontSize: '16px',
    fontFamily: '"Fira Sans", sans-serif',
    border: 'none',
    borderRadius: '10px',
    boxShadow: '0 0 10px rgba(0, 0, 0, 0.1)',
    outline: 'none',
    resize: 'none',
    boxSizing: 'border-box',
    backgroundColor: '#fff',
  },
};

export default Edit;
