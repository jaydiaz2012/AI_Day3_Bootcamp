import os
import openai
import numpy as np
import pandas as pd
import json
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import CSVLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.prompts import ChatPromptTemplate
from langchain.vectorstores import Chroma
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda, RunnablePassthrough
from openai.embeddings_utils import get_embedding
import faiss
import streamlit as st
import warnings
from streamlit_option_menu import option_menu
from streamlit_extras.mention import mention

warnings.filterwarnings("ignore")


st.set_page_config(page_title="News Summarizer Tool", page_icon="", layout="wide")

with st.sidebar :
    #st.image('images/White_AI Republic.png')
    openai.api_key = st.text_input('Enter OpenAI API token:', type='password')
    if not (openai.api_key.startswith('sk-') and len(openai.api_key)==164):
        st.warning('Please enter your OpenAI API token!', icon='⚠️')
    else:
        st.success('Proceed to entering your prompt message!', icon='👉')
    with st.container() :
        l, m, r = st.columns((1, 3, 1))
        with l : st.empty()
        with m : st.empty()
        with r : st.empty()

    options = option_menu(
        "Dashboard", 
        ["Home", "About Us", "Model"],
        icons = ['book', 'globe', 'tools'],
        menu_icon = "book", 
        default_index = 0,
        styles = {
            "icon" : {"color" : "#dec960", "font-size" : "20px"},
            "nav-link" : {"font-size" : "17px", "text-align" : "left", "margin" : "5px", "--hover-color" : "#262730"},
            "nav-link-selected" : {"background-color" : "#262730"}          
        })


if 'messages' not in st.session_state:
    st.session_state.messages = []

if 'chat_session' not in st.session_state:
    st.session_state.chat_session = None  # Placeholder for your chat session initialization

# Options : Home
if options == "Home" :

    st.title("Welcome to the News summarizer!")
    st.write("State any news from a credible website and the 'model' tool below will summarize it to avoid wasting time")
   
elif options == "About Us" :
    #st.image("images/jay.jpg")
    st.title("About Me")
    st.write("Hi, I'm Jay. I am aspiring to be an AI Engineer.")

# Options : Model
elif options == "Model" :
    st.title("News Summarizer Tool")
    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        article_url = st.text_input("Enter News Article URL", placeholder="https://example.com/article/")
        submit_button = st.button("Generate Summary")
        
        if submit_button and article_url:
            try:
                with st.spinner("Fetching and processing the article..."):
                    # Download and parse the article using newspaper3k
                    article = Article(article_url)
                    article.download()
                    article.parse()
                    user_message = article.text

                with st.spinner("Generating Summary..."):    
                System_Prompt = """You are an expert news summarizer, trained to create clear, concise, and informative summaries of news articles. Your goal is to present the most essential information in a structured, easy-to-digest format. Follow these steps:

Step 1: Analyze the Article
Read Thoroughly: Understand the article’s overall context, main points, and supporting information.
Focus on the 5Ws and How: Identify the Who, What, When, Where, Why, and How. Prioritize the central event or issue, along with key people, organizations, dates, and locations.

Step 2: Identify Key Elements
Main Event or Topic: Define the article's core event, development, or issue.
Context: Establish background information or circumstances relevant to the main event.
Key Figures: Note important individuals, groups, or organizations involved.
Quotes and Evidence: Select one or two significant quotes or pieces of evidence that reinforce the article’s message.
Future Implications: Include any possible outcomes, future actions, or developments connected to the event.

Step 3: Structure the Summary
Organize the summary concisely, following this format:
Headline: Craft a short, compelling headline (5-10 words) summarizing the article’s essence.
Lead (1-2 sentences): Introduce the main event or topic, covering the ‘What’ and ‘Who.’
Why it Matters (1-2 sentences): Explain the event's significance or impact.
Details (2-3 sentences): Provide additional context, including evidence, quotes, and relevant facts such as ‘When’ and ‘Where.’
Zoom In (1-2 sentences): Highlight a specific perspective or unique angle, like a quote from an official.
Flashback (1 sentence): Add a quick historical reference to give context.
Reality Check (1 sentence): Present any contrasting or balancing information if relevant.
Conclusion (1 sentence): Conclude with potential future actions, outcomes, or implications.

Step 4: Maintain Objectivity and Neutrality
Ensure the summary is factual, neutral, and free from bias or personal opinions. Write in a professional and accessible tone suitable for all readers.

Step 5: Format and Review
Double-check for clarity, logical flow, and accuracy. Keep sections brief but ensure they include all critical points. Present the final summary in the format outlined above."""

                # Set up the chat structure for OpenAI API
                struct = [{'role': 'system', 'content': System_Prompt}]
                struct.append({"role": "user", "content": user_message})
                
                # Call OpenAI ChatCompletion
                chat = openai.ChatCompletion.create(
                    model="gpt-4o-mini", messages=struct
                )
                
                # Extract the summary from the response
                response = chat.choices[0].message.content
                struct.append({"role": "assistant", "content": response})

                # Display the extracted article content
                st.write("**Extracted Article Text:**")
                st.write(user_message)

                # Display the generated summary
                st.write("**Generated Summary:**")
                st.write(response)
