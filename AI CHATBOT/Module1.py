import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords, wordnet
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag
import os

# Download necessary NLTK resources (run once)
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')

# Initialize lemmatizer
lemmatizer = WordNetLemmatizer()

# Load stopwords
stop_words = set(stopwords.words('english'))

# Function to map NLTK POS tags to WordNet POS tags
def get_wordnet_pos(tag):
    if tag.startswith('J'):
        return wordnet.ADJ  # Adjective
    elif tag.startswith('V'):
        return wordnet.VERB  # Verb
    elif tag.startswith('N'):
        return wordnet.NOUN  # Noun
    elif tag.startswith('R'):
        return wordnet.ADV  # Adverb
    else:
        return wordnet.NOUN  # Default to noun

# Function to process text (tokenization, stopword removal, POS tagging, lemmatization, hyphen join)
def clean_and_lemmatize(text):
    if pd.isna(text):  # Handle missing values
        return ""
    
    tokens = word_tokenize(text)  # Tokenization
    filtered_tokens = [word.lower() for word in tokens if word.isalnum() and word.lower() not in stop_words]  # Remove stopwords & special characters
    pos_tags = pos_tag(filtered_tokens)  # POS tagging
    lemmatized_tokens = [lemmatizer.lemmatize(word, get_wordnet_pos(tag)) for word, tag in pos_tags]  # Lemmatization
    
    return "-".join(lemmatized_tokens)  # Join words with hyphen

# Load the CSV file
file_path = "Gudlavalleru.csv"  # Ensure correct file path
df = pd.read_csv(file_path)

# Check for correct column names
if "Question" not in df.columns or "Answer" not in df.columns:
    raise ValueError("CSV must contain 'Question' and 'Answer' columns!")

# Apply function to process the "Question" column
df["Processed_Question"] = df["Question"].apply(clean_and_lemmatize)

# Select relevant columns: Processed Question & Original Answer
df_output = df[["Processed_Question", "Answer"]]  # Assuming "Answer" column contains answers

# Define the output file path
output_file = os.path.join(os.getcwd(), "Processed_Questions.csv")  # Saves in the current working directory

# Store results in a new CSV file
df_output.to_csv(output_file, index=False)

print(f"✅ Processed QA file saved at: {output_file}")
