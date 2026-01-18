# Image to LaTeX (Groq + LLaMA)

This project converts **mathematical equations from images into LaTeX code** using **Groq's API** and a **vision-capable LLaMA model**.

The model is strictly instructed to output **only raw LaTeX**, making it suitable for automated pipelines, datasets, and evaluation tasks.

---

## 🚀 Features

- 📸 Accepts image input (PNG/JPG)
- 🔢 Extracts mathematical equations
- 🧾 Outputs **pure LaTeX only** (no explanations, no formatting wrappers)
- 🤖 Uses `meta-llama/llama-4-scout-17b-16e-instruct`
- ⚡ Powered by **Groq API**

---

## 🛠 Requirements

- Python 3.9+
- Groq Python SDK

Install dependencies:

```bash
pip install groq
```

---

## 🔑 Environment Setup

Set your Groq API key as an environment variable:

```bash
export GROQ_API_KEY="your_api_key_here"
```

(Windows PowerShell)

```powershell
setx GROQ_API_KEY "your_api_key_here"
```

---

## 📄 Usage

1. Place your equation image in the project directory (e.g. `1406-7.png`)
2. Run the script

```bash
python main.py
```

The output will be **only the LaTeX code** corresponding to the equation in the image.

---

## 📌 Prompt Constraints

The model is explicitly instructed to:

- ❌ Not add explanations
- ❌ Not simplify equations
- ❌ Not add `$`, `\\[ ]`, or document wrappers
- ❌ Not include LaTeX packages or preambles
- ✅ Output **only the exact LaTeX equation**

This ensures clean and deterministic output.

---

## 🧠 Example Workflow

```
Image → Base64 → Groq Vision Model → Raw LaTeX
```

---

## 📂 File Structure

```
.
├── main.py
├── 1406-7.png
├── README.md
```

---

## ⚠ Notes

- Image quality significantly affects accuracy
- Best results with high-resolution, clean mathematical notation

---

## 📜 License

MIT License

---

## ⭐ Acknowledgments

- Groq API
- Meta LLaMA Models

---

If you find this useful, feel free to ⭐ the repository.
