# 🐺 WOLF AI — AI-Powered Chatbot

**A modern conversational AI chatbot built with Python and Streamlit.**

WOLF AI is an interactive chatbot that allows users to ask questions, understand concepts, explore ideas, and receive AI-generated responses through a simple, user-friendly interface.

The project combines AI-powered conversations, chat history, contextual responses, and a modern interface to create a practical AI assistant.

## ✨ Features

- **AI-Powered Chat:** Ask questions and receive AI-generated answers.
- **Conversational Memory:** Continue a conversation with relevant previous messages.
- **Chat History:** Save conversations locally and revisit them later.
- **New Conversation:** Start a fresh chat without intentionally deleting previous conversations.
- **Markdown Responses:** Display organized answers with headings, lists, and code blocks.
- **Modern Interface:** Enjoy a dark theme and wolf-inspired branding.
- **Study Assistance:** Explore concepts, summarize information, and generate practice questions.
- **Python Integration:** Connect the user interface to an AI model through an API.

## 🛠️ Technologies Used

- Python
- Streamlit
- OpenAI Python SDK or a compatible API client
- Large Language Models (LLMs)
- JSON for local chat history
- Environment variables for API configuration

## 📁 Project Structure

```text
WOLF-AI/
│
├── .env              # API key and environment settings
├── AI_client.py      # AI API connection and response logic
├── App.py            # Main Streamlit user interface
├── chatbot.py        # Chatbot functionality
├── README.md         # Project documentation
└── chat_history.json # Local history file, if generated
```

*Note: Keep the filenames exactly as they appear in your project. The history file may be created automatically when the application runs.*

---

## 🚀 Getting Started

Follow these steps to install and run WOLF AI on your computer.

### Step 1: Install Python

Download Python from the official website:

https://www.python.org/downloads/

Install a Python version compatible with your project's dependencies.

On Windows, select **Add Python to PATH** during installation if that option is available.

Verify the installation in your terminal:

```bash
python --version
```

### Step 2: Install Visual Studio Code

Download VS Code:

https://code.visualstudio.com/

Open VS Code and select **File → Open Folder**. Choose the folder containing your WOLF AI files.

### Step 3: Open the Terminal

In VS Code, select:

**Terminal → New Terminal**

Make sure the terminal is opened inside your project folder.

### Step 4: Create a Virtual Environment (Recommended)

Run:

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

If you use macOS or Linux, run:

```bash
source .venv/bin/activate
```

A virtual environment keeps the project's Python dependencies separate from other projects.

### Step 5: Install the Required Packages

Install the packages used by the application:

```bash
pip install streamlit openai python-dotenv
```

If your project has a `requirements.txt` file, use this command instead:

```bash
pip install -r requirements.txt
```

Install any additional packages required by your own code.

### Step 6: Configure Your API Key

Open the `.env` file in your project folder.

Add your API key using the variable name expected by `AI_client.py`.

For example, if your code reads `OPENAI_API_KEY`, the file should contain:

```env
OPENAI_API_KEY=your_api_key_here
```

Replace `your_api_key_here` with your own API key from the provider configured in your project.

**Important:**
- Never publish your real API key on GitHub.
- Do not share your `.env` file publicly.
- The environment variable name must match the one used in your Python code.
- Your API provider may require a separate account, API access, or billing.

If your project uses a different provider or variable name, follow the configuration in `AI_client.py`.

### Step 7: Check the AI Client Configuration

Open `AI_client.py` and verify that:

- The required API library is imported.
- The API key is loaded correctly.
- The correct model name is configured.
- The response function accepts conversation messages and returns the AI's answer.

The chatbot will not generate responses until its API configuration is valid.

### Step 8: Run WOLF AI

If `App.py` contains the main Streamlit interface, run:

```bash
streamlit run App.py
```

Streamlit will start the application and display a local URL, usually:

```text
http://localhost:8501
```

Open the URL in your web browser to use WOLF AI.

If your main application file is named differently, replace `App.py` with its actual filename.

---

## 💬 How to Use WOLF AI

You do not need advanced programming knowledge to use the chatbot after it has been configured.

1. **Open WOLF AI:** Start the application and open its browser URL.
2. **Ask a Question:** Type your question in the chat input box.
3. **Send Your Message:** Submit the question and wait for the AI response.
4. **Read the Answer:** Review the explanation, examples, and formatted content.
5. **Ask Follow-Up Questions:** Continue the same conversation when you need more details.
6. **Start a New Chat:** Use the New Conversation option to begin a separate discussion.
7. **Review Chat History:** Select a saved conversation to revisit earlier messages, if history is enabled.
8. **Stop the Application:** Press `Ctrl + C` in the terminal when you want to stop the local server.

### Example Questions

You can ask WOLF AI questions such as:

- What is Artificial Intelligence?
- Explain Python functions with examples.
- Summarize this paragraph in simple English.
- Generate practice questions about Object-Oriented Programming.
- Explain the difference between machine learning and deep learning.

---

## 🧠 How It Works

WOLF AI uses separate components to manage the interface and AI responses.

**1. App.py — User Interface**

Runs the Streamlit application, displays messages, accepts user questions, and presents AI responses.

**2. AI_client.py — AI Connection**

Handles communication with the configured AI API, sends conversation messages, and retrieves the generated response.

**3. chatbot.py — Chatbot Logic**

Contains additional chatbot functionality as implemented in the project. Its exact responsibilities depend on the code in this file.

**4. .env — Configuration**

Stores local environment settings, such as API credentials, when supported by the application.

**Conversation flow:**

```text
User enters a question
        ↓
Streamlit interface
        ↓
AI client sends messages to the model
        ↓
AI generates a response
        ↓
Response appears in the chat
        ↓
Conversation history is saved, if enabled
```

---

## 🔐 Security and Privacy

- Keep API credentials private.
- Add `.env` to `.gitignore` before uploading your project.
- Do not commit private chat histories or sensitive information.
- Review your AI provider's privacy and data-retention policies.
- Remember that API requests may be processed by an external provider.
- Local JSON history is not the same as cloud storage or a secure database.

Example `.gitignore` entries:

```gitignore
.env
.venv/
__pycache__/
*.pyc
chat_history.json
```

If you have already uploaded a real API key to a public repository, revoke it and create a replacement.

---

## 🛠️ Troubleshooting

### Problem: `streamlit` is not recognized

Install Streamlit in your active Python environment:

```bash
python -m pip install streamlit
```

Then try running the application again.

### Problem: API key error

- Check that the `.env` file exists in the expected location.
- Verify the variable name used by your code.
- Make sure your API key is valid.
- Confirm that the application loads environment variables correctly.

### Problem: The model returns an error

Check your internet connection, configured model name, provider access, and API usage limits.

### Problem: Chat history is missing

Check whether the history file exists and whether the application is saving and loading it from the expected working directory.

### Problem: A Python module is missing

Install the missing dependency in your active virtual environment. If a `requirements.txt` file exists, install the listed packages.

---

## 🔮 Future Improvements

Potential improvements for WOLF AI include:

- Exporting conversations to text or PDF
- Searching previous conversations
- Renaming and deleting chats
- Supporting file uploads and document-based questions
- Adding user authentication
- Deploying the application online
- Improving conversation management and persistent storage

These are possible future enhancements and are not necessarily implemented in the current version.

## 👨‍💻 Project Purpose

WOLF AI is a hands-on project focused on learning and applying Python, conversational AI, Large Language Models, API integration, and interactive application development.

It demonstrates how AI capabilities can be integrated into a practical chatbot interface.

## 📌 Important Notes

- An API key and internet connection may be required.
- Available features depend on the current implementation and AI provider.
- Local chat history depends on the application's storage configuration.
- Never expose API keys or private user data in a public repository.

## 📄 License

If you want others to reuse and modify your project, you may choose an open-source license such as the MIT License. Add a `LICENSE` file before claiming that the repository is distributed under that license.

---

**Built with Python, Streamlit, and AI. 🐺**
