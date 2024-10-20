import React, { useState } from 'react';
import './InputArea.css';


function InputArea({ onSend }) {
  const [message, setMessage] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    onSend(message);
    setMessage('');
  };

  return (
    <form onSubmit={handleSubmit} className="input-area">
      <input
        type="text"
        placeholder="输入您的消息..."
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        required
      />
      <button type="submit">Send</button>
    </form>
  );
}

export default InputArea;
