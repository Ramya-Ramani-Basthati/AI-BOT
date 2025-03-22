import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords, wordnet
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag
from difflib import get_close_matches

# Download necessary NLTK resources
nltk.download('punkt_tab')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger_eng')
nltk.download('wordnet')

# Initialize lemmatizer and stopwords
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

# Function to map POS tags to WordNet format
def get_wordnet_pos(tag):
    if tag.startswith('J'):
        return wordnet.ADJ  
    elif tag.startswith('V'):
        return wordnet.VERB  
    elif tag.startswith('N'):
        return wordnet.NOUN  
    elif tag.startswith('R'):
        return wordnet.ADV  
    else:
        return wordnet.NOUN  

# Function to preprocess and lemmatize text
def clean_and_lemmatize(text):
    if pd.isna(text) or not isinstance(text, str):  # Handle missing values
        return ""
    
    tokens = word_tokenize(text)  # Tokenization
    filtered_tokens = [word.lower() for word in tokens if word.isalnum() and word.lower() not in stop_words]  # Remove stopwords & special characters
    pos_tags = pos_tag(filtered_tokens)  # POS tagging
    lemmatized_tokens = [lemmatizer.lemmatize(word, get_wordnet_pos(tag)) for word, tag in pos_tags]  # Lemmatization
    
    return "-".join(lemmatized_tokens)  # Join words with hyphen

# Load the processed CSV file
file_path = "Processed_Questions.csv"  # Ensure correct file path
df = pd.read_csv(file_path)

# Convert processed questions into a dictionary (processed_question -> answer)
qa_dict = dict(zip(df["Processed_Question"], df["Answer"]))

# Function to retrieve the best-matching answer
def get_answer(user_input):
    processed_input = clean_and_lemmatize(user_input)  # Apply same preprocessing
    matches = get_close_matches(processed_input, qa_dict.keys(), n=1, cutoff=0.6)  # Find closest match
    
    if matches:
        return qa_dict[matches[0]]  # Return matched answer
    else:
        return "Sorry, I don't have an answer for that question."

# *User Interaction Loop*
print("\n🤖 Welcome to the Chatbot! Type 'exit' to end the conversation.\n")

while True:
    user_question = input("🧑 You: ")  # Get user input
    
    if user_question.lower() == "exit":
        print("🤖 Chatbot: Goodbye! Have a great day! 👋\n")
        break
    
    response = get_answer(user_question)  # Retrieve response
    print(f"🤖 Chatbot: {response}\n")  # *Display the answer*
