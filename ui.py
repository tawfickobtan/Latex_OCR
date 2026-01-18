import streamlit as tl
from PIL import Image
import llm
import base64

tl.set_page_config(
    page_title="LaTeX OCR with Llama 3.2 Vision",
    page_icon="🦙",
    layout="wide",
    initial_sidebar_state="expanded"
)

tl.title("🦙 LaTeX OCR with Llama 3.2 Vision")

col1, col2 = tl.columns([6,1])
with col2:
    if tl.button("Clear 🗑️"):
        if 'ocr_result' in tl.session_state:
            del tl.session_state['ocr_result']
        tl.rerun()

tl.markdown('<p style="margin-top: -20px;">Extract LaTeX code from images using Llama!</p>', unsafe_allow_html=True)

tl.markdown("---")

with tl.sidebar:
    tl.header("Upload Image")
    uploaded_file = tl.file_uploader("Choose an image...", type=['png', 'jpg', 'jpeg'])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        tl.image(image, caption="Uploaded Image")

        if tl.button("Extract Latex 🔍"):
            with tl.spinner("Processing request..."):
                try:
                    bytes = uploaded_file.getvalue()
                    b64 = base64.b64encode(bytes).decode("ascii")

                    code = llm.getLatex(b64)
                    tl.session_state["result"] = code
                except Exception as e:
                    tl.error(f"Error processing image: {str(e)}")

if "result" in tl.session_state:
    tl.markdown("### LaTeX Code")
    tl.code(tl.session_state['result'], language='latex')

    tl.markdown("### LaTeX Rendered")

    cleaned_latex = tl.session_state['result'].replace(r"\[", "").replace(r"\]", "")
    tl.latex(cleaned_latex)
else:
    tl.info("Upload an image and click 'Extract LaTeX' to see the results here.")

tl.markdown("---")
