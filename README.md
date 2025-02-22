# Voice Assistant Project

A Python-based voice assistant with a modern **PyQt6 GUI**, speech capabilities, GIF animations, and advanced scheduling features. Designed to handle tasks like app management, speech interaction, and task automation, this project offers a seamless desktop experience.

## 🚀 Features

- 🎤 Voice command functionality
- 🎞️ GIF animations synced with speech output
- 📂 Application management (open, close, minimize apps)
- 📊 Task automation and execution
- 🔍 Real-time information retrieval (e.g., weather, news)
- 🗂️ File management (open, create, delete files)
- 🖥️ System monitoring (CPU usage, memory status)

## 🛠️ Technologies Used

- **Python 3.x**
- **PyQt6** for GUI
- **gTTS** or **pyttsx3** for text-to-speech
- **Pillow** for GIF animations

## 📦 Installation

1. **Clone the repository**

```bash
git clone https://github.com/Thiyagu-2003/voice-assistance.git
cd voice-assistance
```

2. **Create a virtual environment** (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. **Install the dependencies**

```bash
pip install -r requirements.txt
```

## 🎯 Usage

1. **Run the main file**

```bash
python Jarvis.py
```

2. **Features flow:**
   - Launches `desktop_1.py` from `Jarvis.py`.
   - Clicking the **Start** button plays a GIF and speaks sentences.
   - Automatically closes `desktop_1.py` and opens `desktop_2.py`.

## 🔔 Upcoming Features

- Enhanced voice recognition with AI
- App minimization and closing functions
- Customizable task execution sequences
- File organization automation

## 📂 Project Structure

```
voice-assistance/
│
├── Jarvis.py              # Main launcher script
├── desktop_1.py           # Initial GUI with Start button
├── desktop_2.py           # Secondary functionality
├── requirements.txt       # Project dependencies
├── README.md              # Project documentation
└── assets/                # GIFs, icons, and media files
```

## 🤝 Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m 'Add feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a Pull Request.

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

Made with ❤️ by Thiyagu S

