
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def calculate_text_similarity(
    resume_text,
    job_description
):
    """
    Calculate textual similarity between
    resume content and job description
    using TF-IDF and cosine similarity.
    """

    # --------------------------------------------------------
    # Validate input
    # --------------------------------------------------------

    if not resume_text or not job_description:

        return 0.0


    # --------------------------------------------------------
    # Prepare documents
    # --------------------------------------------------------

    documents = [
        resume_text,
        job_description
    ]


    # --------------------------------------------------------
    # Convert text into TF-IDF vectors
    # --------------------------------------------------------

    vectorizer = TfidfVectorizer(
        stop_words="english",
        lowercase=True,
        max_features=5000
    )


    try:

        tfidf_matrix = vectorizer.fit_transform(
            documents
        )

    except ValueError:

        return 0.0


    # --------------------------------------------------------
    # Calculate cosine similarity
    # --------------------------------------------------------

    similarity_matrix = cosine_similarity(
        tfidf_matrix[0:1],
        tfidf_matrix[1:2]
    )


    similarity_score = (
        similarity_matrix[0][0]
        * 100
    )


    # --------------------------------------------------------
    # Return percentage
    # --------------------------------------------------------

    return round(
        similarity_score,
        2
    )

