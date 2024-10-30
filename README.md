# Poem Generator - Chinese Modern Poetry Creator

This is a Chinese modern poetry generator built using **React** and the **OpenAI API**. Users can input a poetry theme through an elegant, simple interface to generate AI-created modern poetry.

## Key Features

- **Welcome Page**: A welcome screen with fade-in animations, project title, and a "Start generating your first AI poem" button.
- **Chat Interface**: An interactive interface similar to ChatGPT, where users can enter themes or keywords, and the AI will generate corresponding poems.
- **Model Selection**: Support for selecting different OpenAI models, such as `ChatGLM-6B` and `gpt-4`.
- **Animations**: Smooth animation transitions for interface elements using Framer Motion to enhance the user experience.
- **Loading Indicator**: Displays a loading prompt while waiting for AI to generate the poem.

## Tech Stack

- **Frontend**: React, React Router, Framer Motion
- **Backend**: Node.js, Express, OpenAI API
- **Other**: Git LFS (for managing large files)

## Project Structure

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

## Installation and Setup

### Frontend

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-username/poem-generator.git
   cd poem-generator
   ```

2. **Install dependencies**

   ```bash
   npm install
   ```

3. **Run the frontend application**

   ```bash
   npm start
   ```

   The app will run on `http://localhost:3000`.

### Backend

1. **Navigate to the `server` directory**

   ```bash
   cd server
   ```

2. **Install dependencies**

   ```bash
   npm install
   ```

3. **Set up environment variables**

   Create a `.env` file in the `server` directory, and add your OpenAI API key:

   ```env
   OPENAI_API_KEY=your-openai-api-key
   ```

   **Note**: Do not commit the `.env` file to version control. Make sure your `.gitignore` file includes `.env`.

4. **Run the backend server**

   ```bash
   node index.js
   ```

   The server will run on `http://localhost:5000`.

## Usage Instructions

1. Open your browser and go to `http://localhost:3000`.
2. On the welcome page, click "Start generating your first AI poem."
3. In the chat interface, enter the theme or content of the poem you want.
4. (Optional) Select the model you wish to use.
5. Click send and wait for the AI to generate a poem.

## Dependencies

### Frontend

- **react**
- **react-dom**
- **react-router-dom**
- **framer-motion**
- **react-markdown**

### Backend

- **express**
- **cors**
- **openai**
- **dotenv**

## Git LFS Configuration

If your project includes large files, it’s recommended to use Git LFS for management.

1. **Install Git LFS**

   Follow the [official Git LFS guide](https://git-lfs.github.com/) based on your operating system.

2. **Initialize Git LFS**

   ```bash
   git lfs install
   ```

3. **Track large files**

   ```bash
   git lfs track "*.psd"
   ```

   This will track all `.psd` files. Adjust the file type as needed.

4. **Commit changes**

   ```bash
   git add .gitattributes
   git commit -m "Configure Git LFS"
   git push
   ```

## Notes

- **API Key Security**: Never expose your OpenAI API key in client code or public repositories. Use environment variables and call the OpenAI API on the server side.
- **CORS Configuration**: When deploying the backend server, configure CORS appropriately to allow access by the frontend application.
- **Dependency Management**: Ensure all required dependencies are installed. If issues arise, check the `package.json` file.

## FAQs

### 1. How can I prevent the `.env` file from being committed to the repository?

In the project root’s `.gitignore` file, add the following:

```gitignore
# Environment Variables
.env
```

### 2. How can I ensure Git LFS works properly after cloning the repository?

Before cloning, install Git LFS, then execute:

```bash
git lfs install
git clone https://github.com/your-username/poem-generator.git
```

## License

[MIT License](LICENSE)

## Acknowledgements

- Thanks to **OpenAI** for the powerful API that made this project possible.
- Thanks to **THU-ChatGLM** for their powerful API, which also contributed to this project.
- Thanks to the **React** community and all open-source contributors.

---
