import spacy
import requests
from utils import cosine_similarity

# Load the pre-trained spaCy model for English
nlp = spacy.load("en_core_web_md")

# Fetch standardized phrases from Google Drive
response = requests.get("https://docs.google.com/uc?export=download&id=1u1bjuGBwopljZ_SvN9o_Bj4et4tsNhUC")
standard_phrases = response.text.split('\n')

def analyze_text(text):
    # Convert the input text into a spaCy document object
    doc = nlp(text)
    suggestions = []

    # Iterate over each sentence in the document
    for sent in doc.sents:
        # Get the vector representation of the sentence
        sent_vec = sent.vector
        # Compare the sentence vector with each standardized phrase vector
        for phrase in standard_phrases:
            phrase_vec = nlp(phrase).vector
            similarity = cosine_similarity(sent_vec, phrase_vec)
            # If the similarity score is above the threshold (0.7), add the suggestion
            if similarity > 0.7:
                suggestions.append((sent.text, phrase, similarity))

    return suggestions

if __name__ == "__main__":
    # Prompt the user to input text for analysis
    text = input("Enter the text for analysis: ")
    suggestions = analyze_text(text)
    # Display the original text, the suggested replacement, and the similarity score
    for original, replacement, score in suggestions:
        print(f"Original: {original}\nSuggestion: {replacement}\nScore: {score}\n")
