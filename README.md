# Voice Assistant

This project is a simple voice-activated assistant built with Python that can perform tasks like opening websites, searching Wikipedia, playing music, telling the time, and sending emails. The assistant uses speech recognition and text-to-speech technologies to interact with the user.

## About the Project

The Python Voice Assistant is designed to perform various tasks through voice commands. It listens to the user's instructions, recognizes speech, and executes tasks such as opening websites, searching information on Wikipedia, playing music, and even sending emails.

## Features

- **Voice Interaction**: The assistant listens and responds to your voice commands.
- **Web Search**: Open websites like YouTube, Google, and StackOverflow with voice commands.
- **Wikipedia Search**: Get brief summaries from Wikipedia on any topic.
- **Music Playback**: Play music from a specified directory on your computer.
- **Time Announcement**: Get the current time on request.
- **Email Sending**: Send emails using voice commands (requires configuration).
- **System Interaction**: Open applications like VS Code directly through voice commands.

## Getting Started

### Prerequisites

Ensure you have Python 3 installed on your system. You'll need the following Python packages:

- `pyttsx3` - Text-to-speech conversion
- `speech_recognition` - Speech-to-text conversion
- `wikipedia` - For fetching summaries from Wikipedia
- `pyaudio` - Audio input/output support
- `smtplib` - For sending emails
- `webbrowser` - To open websites
- `os` - For interacting with the operating system

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/python-voice-assistant.git
   ```

2. Navigate to the project directory:

   ```bash
   cd python-voice-assistant
   ```

3. Install the required modules:

   ```bash
   pip install pyttsx3 speechrecognition wikipedia pyaudio
   ```

### Setup

1. Configure the music directory in the `play music` command (`music_dir` variable) to your local folder containing songs.
2. Set your email credentials in the `sendEmail` function to enable email functionality.
   
   ```python
   server.login('YOUR_GMAIL_ACCOUNT', 'YOUR_PASSWORD')
   ```

> **Warning**: Be cautious when storing sensitive information like passwords in your code. Consider using environment variables or secure vaults for production use.

### Usage

1. Run the script:

   ```bash
   python assistant.py
   ```

2. The assistant will greet you and start listening for your commands. Speak clearly into your microphone and interact with your assistant.

### Commands

- **"Search Wikipedia for [query]"**: Searches Wikipedia and reads a brief summary.
- **"Open YouTube"**: Opens YouTube in your default browser.
- **"Play music"**: Plays music from the specified directory.
- **"What is the time?"**: Tells the current time.
- **"Send email to [contact]"**: Sends an email to the specified contact.

