import React from 'react';
import { motion } from 'framer-motion';
import './ChatWindow.css'; // 引入样式

function ChatWindow({ messages, loading }) {
  return (
    <div className="chat-window">
      {messages.map((msg, index) => (
        <motion.div
          key={index}
          className={`message ${msg.sender}`}
          initial={{ opacity: 0, y: 10 }}
          animate={{ opacity: 1, y: 0 }}
        >
          {msg.text}
        </motion.div>
      ))}
      {loading && (
        <div className="loading-indicator">
          <span className="dot"></span>
          <span className="dot"></span>
          <span className="dot"></span>
        </div>
      )}
    </div>
  );
}

export default ChatWindow;
