# Poem Generator 中文现代诗生成器

这是一个使用 **React** 和 **OpenAI API** 构建的中文现代诗歌生成器。用户可以通过简洁优雅的界面，输入诗歌主题，生成由 AI 创作的现代诗歌。

## 功能特色

- **开始页面**：带有浮现动画的欢迎页面，包含项目标题和“开始生成你的第一首AI诗歌”按钮。
- **聊天界面**：类似于 ChatGPT 的交互界面，用户可以输入主题或关键词，AI 将生成对应的诗歌。
- **模型选择**：支持选择不同的 OpenAI 模型，例如 `ChatGLM-6B` 和 `gpt-4`。
- **动画效果**：使用 Framer Motion，实现界面元素的平滑动画过渡，提升用户体验。
- **加载指示器**：在等待 AI 生成诗歌时，显示加载提示。

## 技术栈

- **前端**：React、React Router、Framer Motion
- **后端**：Node.js、Express、OpenAI API
- **其他**：Git LFS（用于管理大型文件）

## 项目结构

```
project-root/
├── README.md
├── .gitignore
├── package.json
├── server/
│   ├── index.js
│   ├── package.json
│   └── .env
└── src/
    ├── App.jsx
    ├── index.js
    ├── components/
    │   ├── StartPage.jsx
    │   ├── ChatPage.jsx
    │   ├── ChatWindow.jsx
    │   ├── InputArea.jsx
    │   └── ModelSelector.jsx
    └── styles/
        ├── StartPage.css
        ├── ChatPage.css
        └── ...
```

## 安装和运行

### 前端

1. **克隆仓库**

   ```bash
   git clone https://github.com/your-username/poem-generator.git
   cd poem-generator
   ```

2. **安装依赖项**

   ```bash
   npm install
   ```

3. **运行前端应用**

   ```bash
   npm start
   ```

   应用将运行在 `http://localhost:3000`。

### 后端

1. **导航到 `server` 目录**

   ```bash
   cd server
   ```

2. **安装依赖项**

   ```bash
   npm install
   ```

3. **设置环境变量**

   在 `server` 目录下创建一个 `.env` 文件，添加您的 OpenAI API 密钥：

   ```env
   OPENAI_API_KEY=your-openai-api-key
   ```

   **注意**：请勿将 `.env` 文件提交到版本控制系统中。请确保 `.gitignore` 文件中已包含 `.env`。

4. **运行后端服务器**

   ```bash
   node index.js
   ```

   服务器将运行在 `http://localhost:5000`。

## 使用说明

1. 打开浏览器，访问 `http://localhost:3000`。
2. 在开始页面，点击“开始生成你的第一首AI诗歌”按钮。
3. 在聊天界面，输入您想要的诗歌主题或内容。
4. 选择您想使用的模型（可选）。
5. 点击发送，等待 AI 生成诗歌。

## 依赖项

### 前端

- **react**
- **react-dom**
- **react-router-dom**
- **framer-motion**
- **react-markdown**

### 后端

- **express**
- **cors**
- **openai**
- **dotenv**

## Git LFS 配置

如果您的项目包含大型文件，建议使用 Git LFS 进行管理。

1. **安装 Git LFS**

   请根据您的操作系统，按照 [Git LFS 官方指南](https://git-lfs.github.com/) 进行安装。

2. **初始化 Git LFS**

   ```bash
   git lfs install
   ```

3. **跟踪大型文件**

   ```bash
   git lfs track "*.psd"
   ```

   这将跟踪所有 `.psd` 文件。您可以根据需要更改文件类型。

4. **提交更改**

   ```bash
   git add .gitattributes
   git commit -m "配置 Git LFS"
   git push
   ```

## 注意事项

- **API 密钥安全性**：切勿在客户端代码或公共仓库中暴露您的 OpenAI API 密钥。请使用环境变量，并在服务器端调用 OpenAI API。
- **CORS 配置**：在部署后端服务器时，确保正确配置 CORS，以允许前端应用程序访问。
- **依赖项管理**：请确保安装了所有必要的依赖项。如果遇到问题，请检查 `package.json` 文件。

## 常见问题

### 1. 如何防止 `.env` 文件被提交到仓库？

请在项目根目录的 `.gitignore` 文件中添加以下内容：

```gitignore
# Environment Variables
.env
```

### 2. 克隆仓库后，如何确保 Git LFS 正常工作？

请确保在克隆仓库之前已安装 Git LFS，然后执行：

```bash
git lfs install
git clone https://github.com/your-username/poem-generator.git
```

## 许可证

[MIT License](LICENSE)

## 致谢

- 感谢 **OpenAI** 提供的强大 API，使本项目得以实现。
- 感谢 **THU-ChatGLM** 提供的强大 API，使本项目得以实现。
- 感谢 **React** 社区和所有开源贡献者。

---
