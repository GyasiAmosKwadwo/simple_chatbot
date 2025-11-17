# Chatbot

A simple chatbot application built with Python using the OpenAI API via Groq.

## Features

- Interactive command-line chatbot
- Uses Groq's API for fast inference
- Supports continuous conversation

## Prerequisites

- Python 3.7+
- A Groq API key

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd chatbot
   ```

2. Create a virtual environment:
   ```
   python -m venv env
   ```

3. Activate the virtual environment:
   - On Windows: `env\Scripts\activate`
   - On macOS/Linux: `source env/bin/activate`

4. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

5. Create a `.env` file in the root directory and add your Groq API key:
   ```
   OPENAI_API_KEY=your_groq_api_key_here
   ```

## Usage

Run the chatbot:
```
python main.py
```

Enter your prompts when prompted. The chatbot will respond and continue the conversation.

## Configuration

- The model used is `openai/gpt-oss-20b`.
- API base URL is set to `https://api.groq.com/openai/v1`.

## Dependencies

- openai: For interacting with the OpenAI API
- python-dotenv: For loading environment variables from .env file

