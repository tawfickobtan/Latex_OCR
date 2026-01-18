from groq import Groq
import os
import base64

with open("1406-7.png", "rb") as f:
    image = base64.b64encode(f.read()).decode('utf-8')

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY")
)

messages = [
    {"role": "user",
     "content": [
        {"type": "text",
         "text": "Understand the mathematical equation in the provided image and output the corresponding LaTeX code.\n" +
                            "Here are some guidelines you MUST follow or you will be penalized:\n" +
                            "- NEVER include any additional text or explanations.\n" +
                            "- DON'T add dollar signs ($) around the LaTeX code.\n" +
                            "- DO NOT extract simplified versions of the equations.\n" +
                            "- NEVER add documentclass, packages or begindocument.\n" +
                            "- DO NOT explain the symbols used in the equation.\n" +
                            "- Output only the LaTeX code corresponding to the mathematical equations in the image."},
        {"type": "image_url",
         "image_url":
         {"url": f"data:image/jpeg;base64,{image}" }}]}
]

response = client.chat.completions.create(
    model = "meta-llama/llama-4-scout-17b-16e-instruct",
    messages=messages
)

print(response.choices[0].message.content)