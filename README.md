# TopicModeling_Modified-BERTopic
Summary: Implemented a modified BERTopic algorithm by utilizing configurations and text segmentation for an undergraduate thesis project, with acceptance at the 2025 9th International Conference on Natural Language Processing and Information Retrieval (NLPIR).

This project applies BERTopic, a transformer-based topic modeling technique, to analyze YouTube video transcripts. The goal is to extract fine-grained, interpretable topics from each video and uncover meaningful patterns within the content. This work is part of a research study on the Pinoybaiting phenomenon, aiming to better understand themes embedded in videos related to Philippine culture.

**Data Collection**
* YouTube videos were collected using targeted queries related to Filipino culture (e.g., reactions, travel, food).
* Transcripts were extracted if available, otherwise generated using Whisper (speech-to-text model)

**Transcript Segmentation**
* The implementation utilized Google Gemini (Gemini 2.0 Flash) as a tool to generate segments from the video transcripts.
* Each transcript is split into context-aware segments (instead of treating the entire video as one document).
* Segmentation is based on:
  * Conversational flow
  * Topic/context shifts
* This enables multiple topics per video, overcoming the one-topic-per-document limitation.

**Text Preprocessing**
* Minimal preprocessing to preserve semantic meaning:
  * Removal of special characters and noise
  * Whitespace normalization
  * Custom stopword handling

**Model Fitting & Hyperparameter Tuning**

**The BERTopic model was configured and optimized using the following components:**

* Embedding Model
  * A multilingual SentenceTransformer was used to convert text into embeddings, enabling support for English, Filipino, and mixed-language transcripts.
* UMAP (Dimensionality Reduction)
  * Reduces high-dimensional embeddings into a lower-dimensional space for clustering.
  * A fixed random_state=42 was used to ensure reproducibility.
* HDBSCAN (Clustering)
  * Identifies dense clusters in the reduced space to form topic groups based on semantic similarity.
* Representation Model
  * Combines:
    * KeyBERTInspired which extracts semantically relevant keywords per topic
    * Maximal Marginal Relevance (MMR) which reduces redundancy and improves keyword diversity
* Vectorizer Model
  * A customized CountVectorizer with:
  * N-gram range of (1, 3) (unigrams, bigrams, trigrams)
* c-TF-IDF
  * Enhances topic representation by emphasizing distinctive terms and reducing common noise words.
* Topic Probabilities
  * Enabled to compute probability distributions per document, supporting outlier detection and reassignment.
* Topic Reduction (nr_topics)
  * Automatically merges similar topics based on similarity thresholds to improve coherence.
 
**Visualization using Streamlit**
