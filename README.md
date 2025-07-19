
# RST to HTML Converter with Time Limit

This repository contains two simple Python scripts:

## 1. `rsttohtmlchangeonpandoc.py`

A script that converts `.rst` (reStructuredText) files into `.html` using [Pandoc](https://pandoc.org/).

**How it works:**
- It walks through a specified directory (`/var/home/rafo/matplotlib`) and finds all `.rst` files.
- It uses Pandoc to convert them to HTML files.

>  **Note**: Pandoc must be installed on your system.

---

## 2. `stoprogram.py`

This script is a wrapper function to measure how long a function runs.

**Features:**
- If the execution time exceeds 60 seconds, the program automatically stops.
- Helps prevent infinite loops or long-running tasks.

---

## 🔧 How to Use

1. Clone the repository:
```bash
git clone https://github.com/Rafo044/your-repo-name.git
cd your-repo-name
```

2. Run the RST to HTML script:
```bash
python rsttohtmlchangeonpandoc.py
```

3. Use the `stop()` wrapper to limit your script’s runtime.

---

## Requirements

- Python 3.x
- [Pandoc](https://pandoc.org/) installed and accessible via command line

---

##  License

[MIT License]()
