import streamlit as st
import docx
import re
import spacy
from collections import defaultdict
from textblob import TextBlob

# Load spaCy model for NLP
nlp = spacy.load('en_core_web_sm')

# Function to read text file
def read_file(file):
    if file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        doc = docx.Document(file)
        return "\n".join([para.text for para in doc.paragraphs])
    else:
        return str(file.read(), 'utf-8')

# Function to analyze document for legal parameters
def analyze_document(text):
    doc = nlp(text)
    clauses = defaultdict(list)
    for sent in doc.sents:
        if "agreement" in sent.text.lower():
            clauses["Agreement"].append(sent.text)
        if "termination" in sent.text.lower():
            clauses["Termination"].append(sent.text)
        if "confidentiality" in sent.text.lower():
            clauses["Confidentiality"].append(sent.text)
        if "warranty" in sent.text.lower():
            clauses["Warranty"].append(sent.text)
    return clauses

# Function to perform sentiment analysis
def sentiment_analysis(text):
    blob = TextBlob(text)
    return blob.sentiment

# Streamlit App
st.image("image\\yo.jpg")
st.title("JurisIQ - Automated Legal Document Analysis Software")
# File Upload
st.sidebar.title("Please Upload Document") 
uploaded_file = st.sidebar.file_uploader("Choose a text file", type=["txt", "docx"])

if uploaded_file is not None:
    # Read and display the file content
    document_text = read_file(uploaded_file)
    st.text_area("Document Content", document_text, height=300)
    
    # Analyze document
    st.subheader("Legal Parameters Analysis")
    clauses = analyze_document(document_text)
    for clause, sentences in clauses.items():
        st.write(f"**{clause} Clauses:**")
        for sentence in sentences:
            st.write(f"- {sentence}")

    # Sentiment Analysis
    st.subheader("Sentiment Analysis")
    sentiment = sentiment_analysis(document_text)
    st.write(f"Polarity: {sentiment.polarity}")
    st.write(f"Subjectivity: {sentiment.subjectivity}")
    
    # Keyword Search
    st.subheader("Keyword Search")
    keyword = st.text_input("Enter a keyword to search for")
    if keyword:
        keyword_sentences = [sent.text for sent in nlp(document_text).sents if re.search(keyword, sent.text, re.IGNORECASE)]
        st.write(f"Sentences containing '{keyword}':")
        for sentence in keyword_sentences:
            st.write(f"- {sentence}")

    
