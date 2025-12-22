# Pipe-and-Filter Text Processing Pipeline

This project demonstrates the **Pipe-and-Filter architectural pattern** through a web-based text processing pipeline.  
Raw text input is processed sequentially through independent filters, where each filter performs a specific task and passes its output to the next stage.

The system is designed to clearly illustrate **separation of concerns**, **data flow transparency**, and **filter independence**, which are core principles of the pipe-and-filter architecture.

---

## 📐 Architecture Overview

The pipeline consists of four sequential stages:

1. **Tokenize**
2. **Clean**
3. **Transform**
4. **Analyze**

```
Input Text
    ↓
Tokenize Filter
    ↓
Clean Filter
    ↓
Transform Filter
    ↓
Analyze Filter
    ↓
Results & Statistics
```

---

## 🧩 Pipeline Stages

### 1. Tokenize Stage
- Splits the input text into individual tokens
- Normalizes basic formatting
- Produces a raw list of tokens

---

### 2. Clean Stage
- Removes stop-words and punctuation
- Produces cleaned tokens
- Tracks removed tokens with reasons

---

### 3. Transform Stage
- Converts tokens to lowercase
- Removes tokens shorter than 3 characters
- Tracks modified and removed tokens

---

### 4. Analyze Stage
- Computes statistical insights:
  - Total tokens
  - Unique tokens
  - Average token length
  - Most frequent tokens
  - Token length distribution

---

## 🖥️ User Interface Features

- Visual pipeline stages
- Token badges with color coding
- Info buttons showing removed/modified tokens
- Responsive layout

---

## 🛠️ Technologies Used

- **Python 3** – Core programming language
- **Flask** – Web framework for handling requests and pipeline execution
- **HTML5 / CSS3** – User interface and responsive layout
- **Jinja2** – Template engine used to dynamically render pipeline outputs in HTML
- **collections.Counter** – Used for token frequency analysis in the analysis stage


---

## 📂 Project Structure

```
PIPE_AND_FILTER_TEXT_PIPELINE/
│
├── filters/
│   ├── __init__.py
│   ├── tokenize.py
│   ├── clean.py
│   ├── transform.py
│   └── analyze.py
│
├── pipeline/
│   ├── __init__.py
│   └── pipeline.py
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
├── app.py
├── requirements.txt
└── README.md
```

---

## ▶️ How to Run

```bash
pip install -r requirements.txt
python app.py
```

Open: http://127.0.0.1:5000

---
