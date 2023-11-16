import random
import PyPDF2
import pyperclip

def read_words_from_pdf(file_path):
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfFileReader(file)
        text = ""
        for page_num in range(reader.numPages):
            text += reader.getPage(page_num).extractText()
    return [word.strip() for word in text.split()]

def raffle_words(word_list, num_words=12):
    if len(word_list) < num_words:
        raise ValueError("Not enough words in the list to raffle")
    return random.sample(word_list, num_words)

def copy_to_clipboard(text):
    pyperclip.copy(text)
    print("Words copied to clipboard!")

# Path to your PDF file
file_path = 'path_to_your_pdf_file.pdf'

# Read words from the PDF
words = read_words_from_pdf(file_path)

# Raffle 12 unique words
raffled_words = raffle_words(words)

# Join the words into a single string and copy to clipboard
formatted_words = ', '.join(raffled_words)
copy_to_clipboard(formatted_words)

# Print the raffled words
print(raffled_words)
