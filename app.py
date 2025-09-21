import csv
from flask import Flask, render_template, request, redirect, url_for, flash, abort
# for the github webhook
import hmac
import hashlib
import subprocess
import os
from dotenv import load_dotenv
# for the app
from models import Book
from services import BookService


project_folder = os.path.expanduser('~/isbnscanner')  # adjust as appropriate
load_dotenv(os.path.join(project_folder, '.env'))

# Initialize the Flask application
app = Flask(__name__)
# A secret key is required for flashing messages
app.secret_key = 'some_secret_key_for_development'

# The auto deploy route
WEBHOOK_SECRET = os.getenv('WEBHOOK_SECRET')
DEPLOY_SCRIPT_PATH = os.getenv('DEPLOY_SCRIPT_PATH')

def load_books(filename='books-bib-all.csv'):
    """Loads books from a CSV file into a list of Book objects."""
    books = []
    try:
        # Construct the absolute path to the CSV file
        base_dir = os.path.abspath(os.path.dirname(__file__))
        file_path = os.path.join(base_dir, filename)
        with open(file_path, mode='r', encoding='utf-8') as infile:
            # DictReader reads rows as dictionaries, which is perfect for our Book model
            reader = csv.DictReader(infile, delimiter=';')
            for row in reader:
                clean_row = {str(k).strip().lower(): v for k, v in row.items()}
                isbn = clean_row.get('isbn')
                auteur = clean_row.get('auteur')
                titel = clean_row.get('titel')
                books.append(Book(isbn, auteur, titel))

    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
    return BookService(books)

BOOK_SERVICE = load_books()

@app.route('/')
def index():
    return render_template('index.html', nr_of_books=BOOK_SERVICE.total_nr_of_books())

@app.route('/zoek', methods=['POST'])
def zoek():
    input = request.form.get('isbn', '')
    print(input)
    submitted_isbn = input.strip().replace(',', '').replace(' ', '')
    found_book = BOOK_SERVICE.find_by_isbn(submitted_isbn)

    if not found_book:
        flash(f'Boek met ISBN {submitted_isbn} niet gevonden.', 'error')

    return render_template('index.html', nr_of_books=BOOK_SERVICE.total_nr_of_books(), book=found_book)

@app.route('/update_server', methods=['POST'])
def webhook():
    if not WEBHOOK_SECRET:
        abort(500, description="WEBHOOK_SECRET environment variable not set.")
    if not DEPLOY_SCRIPT_PATH:
        abort(500, description="DEPLOY_SCRIPT_PATH environment variable not set.")

    # Verify the request is from GitHub and the signature is valid
    signature_header = request.headers.get('X-Hub-Signature-256')
    if not signature_header:
        abort(403)

    hash_algorithm, signature = signature_header.split('=')
    mac = hmac.new(WEBHOOK_SECRET.encode('utf-8'), msg=request.data, digestmod=hashlib.sha256)
    if not hmac.compare_digest(mac.hexdigest(), signature):
        abort(403)

    # If the push is to the 'main' branch, run the deploy script
    if request.json.get('ref') == 'refs/heads/main':
        try:
            subprocess.run([DEPLOY_SCRIPT_PATH], check=True)
            return 'Server update initiated successfully.', 200
        except subprocess.CalledProcessError as error:
            return f'Script execution failed: {error}', 500

    return 'Push was not to the main branch.', 200


if __name__ == '__main__':
    app.run(debug=True)
