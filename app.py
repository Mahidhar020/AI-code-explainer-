import streamlit as st
import openai

# Set your OpenAI API key here
openai.api_key = "YOUR_OPENAI_API_KEY"

# App UI
st.set_page_config(page_title="AI Code Explainer")
st.markdown("<h1 style='text-align: center;'>🧠 AI Code Explainer</h1>", unsafe_allow_html=True)

# Input text area
code_input = st.text_area("Paste your code here:", height=150)

# Explain button
if st.button("Explain Code"):
    if not code_input.strip():
        st.warning("Please enter some code to explain.")
    else:
        with st.spinner("Explaining..."):
            try:
                # OpenAI API call
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant that explains code in simple terms."},
                        {"role": "user", "content": f"Explain this code:\n{code_input}"}
                    ],
                    temperature=0.5,
                    max_tokens=300
                )
                explanation = response['choices'][0]['message']['content']
                st.markdown("**Explanation:**")
                st.success(explanation)

            except Exception as e:
                st.error(f"An error occurred: {e}")
