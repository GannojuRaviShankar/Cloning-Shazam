# 📽️ Enhancing Search Engine Relevance for Video Subtitles

## 📌 Overview
This project focuses on improving search relevance for video subtitles using **Natural Language Processing (NLP)** and **Machine Learning (ML)**. The goal is to develop a **semantic search engine** that retrieves relevant subtitles from a database based on user queries.

## 🚀 Features
- **Keyword-Based & Semantic Search** using TF-IDF and BERT-based embeddings.
- **Audio-to-Text Transcription** using AssemblyAI.
- **Efficient Data Storage** with ChromaDB for embeddings.
- **Cosine Similarity Retrieval** to find relevant subtitles.
- **Streamlit UI** for a user-friendly experience.


## 🛠️ Installation & Setup
### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/your-username/Enhancing-Search-Engine-Relevance-for-Video-Subtitles.git
cd Enhancing-Search-Engine-Relevance-for-Video-Subtitles
```

### **2️⃣ Create & Activate Virtual Environment (Optional)**
```bash
python -m venv venv  # Create virtual environment
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows
```

### **3️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4️⃣ Set Up Environment Variables**
Create a `.env` file in the root directory and add:
```plaintext
ASSEMBLYAI_API_KEY=your_assemblyai_api_key
GOOGLE_API_KEY=your_google_api_key
CHROMA_DB_PATH=your_path_to_chromadb_folder
```

## 🎯 Usage
### **1️⃣ Run the Streamlit App**
```bash
streamlit run genaifinal.py
```

### **2️⃣ Upload an Audio File & Search**
- Upload a **2-minute** audio recording of a movie/TV series.
- The system will **transcribe** it into text.
- It will then **retrieve the most relevant subtitles** from the database.

## 📚 Core Techniques
- **Data Preprocessing:** Cleaning subtitle text (removing timestamps, special characters).
- **Embedding Techniques:**
  - **TF-IDF** for keyword-based search.
  - **BERT-based SentenceTransformers** for semantic search.
- **Chunking & Overlapping Windows:**
  - To avoid loss of context when embedding large documents.
- **Vector Storage & Retrieval:**
  - Using **ChromaDB** to store subtitle embeddings.
  - **Cosine similarity** for relevance ranking.

## 🔗 References & Resources
- [AssemblyAI](https://www.assemblyai.com/) - Audio Transcription
- [LangChain](https://python.langchain.com/) - ChromaDB Integration
- [SentenceTransformers](https://www.sbert.net/) - Semantic Search Models


## 📜 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
⭐ **If you found this project helpful, don't forget to star the repo!** ⭐

