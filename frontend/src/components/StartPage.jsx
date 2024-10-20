import React from 'react';
import { useNavigate } from 'react-router-dom';
import { motion } from 'framer-motion';
import './StartPage.css'; // 引入样式

function StartPage() {
  const navigate = useNavigate();

  const handleStart = () => {
    navigate('/chat');
  };

  return (
    <div className="start-page">
      <motion.h1
        className="title"
        initial={{ opacity: 0, y: -20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 1 }}
      >
        Poem Generator 中文现代诗生成器
      </motion.h1>
      <motion.button
        className="start-button"
        onClick={handleStart}
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ delay: 0.5, duration: 1 }}
        whileHover={{ scale: 1.05 }}
      >
        开始生成你的第一首AI诗歌
      </motion.button>
    </div>
  );
}

export default StartPage;
