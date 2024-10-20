import React from 'react';
import './ModelSelector.css';

function ModelSelector({ model, setModel }) {
  return (
    <div className="model-selector">
      <label htmlFor="model">选择模型：</label>
      <select
        id="model"
        value={model}
        onChange={(e) => setModel(e.target.value)}
      >
        <option value="gpt-3.5-turbo">GPT-3.5 Turbo</option>
        <option value="gpt-4">GPT-4</option>
        {/* 添加更多模型选项 */}
      </select>
    </div>
  );
}

export default ModelSelector;
