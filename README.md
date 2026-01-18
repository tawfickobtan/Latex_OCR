# Image to LaTeX (Groq + LLaMA + Streamlit)

This project converts **mathematical equations from images into LaTeX code** using **Groq's API**, a **vision-capable LLaMA model**, and provides a **Streamlit web interface** for easy interaction.

The model is strictly instructed to output **only raw LaTeX**, making it suitable for automated pipelines, datasets, and evaluation tasks.

---

## 🚀 Features

- 📸 Accepts image input (PNG/JPG)
- 🔢 Extracts mathematical equations
- 🧾 Outputs **pure LaTeX only** (no explanations, no formatting wrappers)
- 🤖 Uses `meta-llama/llama-4-scout-17b-16e-instruct`
- ⚡ Powered by **Groq API**
- 🌐 Streamlit interface for **interactive OCR**

---

## 🛠 Requirements

- Python 3.9+
- Groq Python SDK
- Pillow
- Streamlit

Install dependencies:

```bash
pip install groq pillow streamlit
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

```bash
streamlit run app.py
```

- Upload an image
- Click **Extract LaTeX**
- View raw LaTeX and rendered equation
- Use **Clear** button to reset

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
Image → Base64 → Groq Vision Model / LLaMA → Raw LaTeX → Streamlit Display
```

---

## 📂 File Structure

```
.
├── main.py          # Python script using Groq
├── ui.py           # Streamlit app for interactive OCR
├── README.md
```

---

## ⚠ Notes

- Image quality significantly affects accuracy
- Best results with high-resolution, clean mathematical notation

---

If you find this useful, feel free to ⭐ the repository, or checkout my [LinkedIn Profile](https://www.linkedin.com/in/tawfic-kobtan/).
