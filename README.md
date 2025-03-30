# Voice Assistant Project

A Python-based voice assistant with a modern **PyQt6 GUI**, speech capabilities, GIF animations, and advanced scheduling features. Designed to handle tasks like app management, speech interaction, and task automation, this project offers a seamless desktop experience.

## 🚀 Features

### 🔧 System Control & Navigation

- Activates wake-up and sleep modes.
- Closes the program.
- Manages system functions like shutdown, restart, log out, and sleep.
- Takes screenshots, starts/stops recording, and closes applications.

### 🔍 Search & Information Retrieval

- Performs Wikipedia searches.
- Finds locations by name or pincode.
- Provides current location and IP address.
- Checks internet speed and battery status.
- Retrieves the current time and date.

### 🎭 Entertainment & Media

- Tells jokes.
- Plays songs on YouTube.
- Controls YouTube playback (pause, resume, mute, volume adjustments, etc.).

### 🌐 Web & Browser Automation

- Scrolls webpages.
- Opens/closes tabs, zooms in/out, refreshes pages, and manages browser history.
- Navigates forward and backward in the browser.

### 🧠 Smart Assistant Features

- Provides dictionary meanings.
- Searches for books and movie ratings.
- Offers motivational quotes and random facts.
- Retrieves anime quotes and character details.

### 🖥️ System Applications & Control

- Opens and closes apps or websites.
- Controls the camera.
- Opens Nova documentation.

### ⌨️ Typing & Editing Functions

- Enables/disables typing mode.
- Performs clipboard operations like copy, paste, and selecting all text.
- Saves documents and supports undo/redo actions.

### 🖱️ Mouse & Input Control

- Moves the mouse cursor.
- Executes left, right, and double-click actions.

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
python main_2.py
```

2. **Features flow:**
   - Launches `desktop_1.py` from `main_2.py`.
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
├── alarm.py               # Alarm feature module
├── app_handler.py         # App handling utilities
├── assignment_writer.py   # Assignment automation tool
├── call-function.py       # Function call handler
├── Features.py            # Additional voice assistant features
├── game.py                # Game module
├── internet_speed_test.py # Internet speed testing script
├── jarvisUi.py            # GUI for Jarvis
├── Nasa.py                # NASA-related features
├── on_off.py              # System on/off control
├── Requirements.txt       # Project dependencies
├── scrool_system.py       # School system automation
├── utils.py               # Utility functions
├── Web_Open.py            # Web automation script
├── WindowsAuto.py         # Windows automation tasks
├── YT.py                  # YouTube functionalities
├── NasalImages/           # NASA-related images and assets
├── README.md              # Project documentation
└── Material/              # Additional materials or assets

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

