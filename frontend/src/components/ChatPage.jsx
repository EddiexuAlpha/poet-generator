// ChatPage.jsx
import React, { useState } from 'react';
import ModelSelector from './ModelSelector';
import ChatWindow from './ChatWindow';
import InputArea from './InputArea';
import './ChatPage.css';

function ChatPage() {
    const [messages, setMessages] = useState([
        { text: '请输入你想生成的诗歌关键词，如“爱情”，“生存”', sender: 'bot' }
      ]);
  const [model, setModel] = useState('chatglm-6b');
  const [loading, setLoading] = useState(false);

  const handleSend = async (message) => {
    const userMessage = { text: message, sender: 'user' };
    setMessages((prev) => [...prev, userMessage]);

    setLoading(true);

    try {
      const response = await fetch('http://localhost:5000/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ user_id: 'user1', message }),
      });
      const data = await response.json();
      const botMessage = { text: data.response, sender: 'bot' };
      setMessages((prev) => [...prev, botMessage]);
    } catch (error) {
      console.error('Error:', error);
      const errorMessage = { text: '抱歉，服务器出现错误。', sender: 'bot' };
      setMessages((prev) => [...prev, errorMessage]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="chat-page">
      <ModelSelector model={model} setModel={setModel} />
      <ChatWindow messages={messages} loading={loading} />
      <InputArea onSend={handleSend} />
    </div>
  );
}

export default ChatPage;
