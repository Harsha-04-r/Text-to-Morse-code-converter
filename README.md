# 📡 Text to Morse Code Converter

A simple Python project that converts normal text into Morse code using dictionaries and loops.

This project takes user input, translates each character into Morse code, and displays the final encoded message in the terminal.

---

# ✨ Features

- 🔤 Converts text into Morse code
- 🔢 Supports numbers (`0-9`)
- 🔠 Supports uppercase alphabets (`A-Z`)
- ␣ Supports spaces between words using `/`
- ⚠️ Detects invalid characters
- 🔁 Continuous conversion loop until user exits

---

# 🛠️ Built With

- Python

---

# ▶️ How to Run

## 1. Clone the repository

```bash
git clone https://github.com/your-username/morse-code-converter.git
```

## 2. Navigate into the project folder

```bash
cd morse-code-converter
```

## 3. Run the program

```bash
python main.py
```

---

# 🎮 Example Usage

```text
Enter text to convert to morse code: Hello World
Morse code: ......-...-..---/.-----.-..-..-..
Do you wish to continue? (y/n):y
Enter text to convert to morse code: Python
Morse code: .--.-.---....----.
Do you wish to continue? (y/n):n
```

---

# 🧠 Concepts Practiced

This project helped me practice:

- Python dictionaries
- Functions
- Loops
- Conditional statements
- String manipulation
- User input handling
- Input validation

---

# ⚙️ How It Works

The program uses a Python dictionary where:

```python
'A': '.-'
'B': '-...'
```

Each character entered by the user is checked against the dictionary and converted into its Morse code equivalent.

If an unsupported character is detected, the program displays:

```text
Invalid characters
```

---

# 🚀 Future Improvements

- Morse code to text conversion
- GUI version using Tkinter
- Better spacing between Morse letters
- File input support

---

# 📄 License

This project was created for learning and educational purposes.

---
