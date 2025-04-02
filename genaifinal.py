import streamlit as st
import assemblyai as aai
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
from config import CHROMA_DB_PATH, EMBEDDING_MODEL, ASSEMBLYAI_API_KEY
import tempfile
import os

# Initialize AssemblyAI
aai.settings.api_key = ASSEMBLYAI_API_KEY
transcriber = aai.Transcriber()

# Load embeddings model
embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)

# Load ChromaDB
db = Chroma(persist_directory=CHROMA_DB_PATH, embedding_function=embeddings)

def transcribe_audio(audio_path):
    """Convert audio to text using AssemblyAI, with error handling."""
    try:
        transcript = transcriber.transcribe(audio_path)
        if transcript and hasattr(transcript, 'text'):
            return transcript.text.strip()
        return None
    except Exception as e:
        st.error(f"Error transcribing audio: {e}")
        return None

def retrieve_similar_chunks(query: str, k=5):
    """Retrieve top-k most relevant document chunks from ChromaDB."""
    try:
        results = db.similarity_search(query, k=k)
        return [(doc.metadata.get('num', 'N/A'), doc.page_content) for doc in results if doc.page_content]
    except Exception as e:
        st.error(f"Error retrieving similar subtitles: {e}")
        return []

# Streamlit UI
st.title("🎬 Video Subtitle Search Engine")

uploaded_file = st.file_uploader("📤 Upload an audio/video file", type=["mp3", "wav", "mp4"])
num_results = st.slider("🔍 Number of results", 1, 10, 5)

if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp_file:
        tmp_file.write(uploaded_file.read())
        tmp_path = tmp_file.name
    
    st.info("⏳ Transcribing audio... Please wait.")
    query_text = transcribe_audio(tmp_path)

    # Cleanup temporary file
    os.remove(tmp_path)

    if query_text:
        st.success("✅ Transcription successful!")
        st.markdown(f"**🎙️ Transcription:** \n> {query_text}")

        st.info("🔍 Searching for relevant subtitles...")
        results = retrieve_similar_chunks(query_text, num_results)

        if results:
            for num, content in results:
                subtitle_url = f"https://www.opensubtitles.org/en/subtitles/{num}" if num != "N/A" else "#"
                st.markdown(f"📜 **Subtitle ID:** [{num}]({subtitle_url})")
                st.write(content)
                st.markdown("---")
        else:
            st.warning("⚠️ No relevant subtitles found. Try a different audio clip.")
    else:
        st.warning("⚠️ Could not extract transcription. Try a different audio file.")
