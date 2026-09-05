import os
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

MODEL = "gpt-5.4-mini"

st.set_page_config(
    page_title="Prompt Engineering Demo",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Prompt Engineering Demo")
st.write(
    "See how changing the prompt can change the quality and format of the response."
)

# -------------------------------------------------
# Prompt 1
# -------------------------------------------------

st.subheader("1️⃣ Basic / Vague Prompt")

prompt1 = st.text_area(
    "Enter a simple prompt:",
    value="Explain Generative AI.",
    height=120
)

# -------------------------------------------------
# Prompt 2
# -------------------------------------------------

st.subheader("2️⃣ Improved Prompt")

prompt2 = st.text_area(
    "Enter an improved prompt:",
    value="""Explain Generative AI to a beginner who knows basic Python.

Requirements:
- Use simple language
- Give one real-world analogy
- Give 3 practical examples
- Keep the answer under 200 words""",
    height=180
)

# -------------------------------------------------
# Run button
# -------------------------------------------------

if st.button("🚀 Compare Prompts", type="primary"):

    if not prompt1.strip() or not prompt2.strip():
        st.warning("Please enter both prompts.")
        st.stop()

    with st.spinner("Calling the LLM..."):

        response1 = client.responses.create(
            model=MODEL,
            input=prompt1
        )

        response2 = client.responses.create(
            model=MODEL,
            input=prompt2
        )

    # -------------------------------------------------
    # Display results
    # -------------------------------------------------

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🔴 Response to Basic Prompt")
        st.write(response1.output_text)

        if response1.usage:
            st.caption(
                f"Input tokens: {response1.usage.input_tokens} | "
                f"Output tokens: {response1.usage.output_tokens}"
            )

    with col2:
        st.subheader("🟢 Response to Improved Prompt")
        st.write(response2.output_text)

        if response2.usage:
            st.caption(
                f"Input tokens: {response2.usage.input_tokens} | "
                f"Output tokens: {response2.usage.output_tokens}"
            )

    # -------------------------------------------------
    # Explanation
    # -------------------------------------------------

    st.divider()

    st.subheader("💡 What changed?")

    st.markdown("""
    The model received two different instructions.

    **Basic prompt**
    - Task is vague
    - No audience specified
    - No format specified
    - No length constraint
    - No examples requested

    **Improved prompt**
    - Clear task
    - Specific audience
    - Context provided
    - Constraints added
    - Output requirements specified

    👉 This is the basic idea of **Prompt Engineering**:
    **communicating your requirement clearly to the LLM.**
    """)
