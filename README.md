# AI-BOT
The chatbot performs the following tasks:

Data Preprocessing:
Loads the CSV file containing questions and answers.
Applies tokenization, stopword removal, POS tagging, and lemmatization to process the questions.
Stores the processed questions with their respective answers in a new CSV file.

User Interaction:
Prompts the user to enter a question.
Processes the user's input using the same NLP techniques.
Searches for a matching processed question in the CSV file.
Retrieves and displays the corresponding answer or informs the user if no match is found.

1.Prerequisites
Python 3.11 or later
Required packages:
pandas
nltk

2. Install Required Packages
Run the following command to install dependencies:
pip install pandas nltk

3. Download NLTK Resources
Ensure the following NLTK packages are downloaded:
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')

4. Place Required Files
Place Gudlavalleru.csv in the same directory as your Python scripts.

🚀 Usage Instructions
Step 1: Run Module1.py
This script processes the input CSV and generates Processed_Questions.csv.
python Module1.py
Step 2: Run Module2.py
This script allows the user to ask questions and retrieves the corresponding answers.
python Module2.py

🧠 How It Works
Module 1: Prepares a CSV with processed questions by:
Tokenizing questions.
Removing stopwords and special characters.
Applying POS tagging and lemmatization.
Joining lemmatized tokens with a hyphen.

Module 2: Handles user queries by:
Applying the same preprocessing steps to the user's question.
Searching for a match in the processed questions.
Returning the corresponding answer or a "No match found" message.

📝 Example Input/Output
Input:
User: Where is Gudlavalleru Engineering College located?
Output:
Answer: Gudlavalleru Engineering College is located in Gudlavalleru, Krishna District, Andhra Pradesh, India.


