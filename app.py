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


project_folder = os.path.expanduser('~/isbnscanner')  # adjust as appropriate
load_dotenv(os.path.join(project_folder, '.env'))

# Initialize the Flask application
app = Flask(__name__)
# A secret key is required for flashing messages
app.secret_key = 'some_secret_key_for_development'

# The auto deploy route
WEBHOOK_SECRET = os.getenv('WEBHOOK_SECRET')
if not WEBHOOK_SECRET:
    raise ValueError("Error: WEBHOOK_SECRET environment variable not set.")

# Get the deploy script path from an environment variable
DEPLOY_SCRIPT_PATH = os.getenv('DEPLOY_SCRIPT_PATH')
if not DEPLOY_SCRIPT_PATH:
    raise ValueError("Error: DEPLOY_SCRIPT_PATH environment variable not set.")

@app.route('/update_server', methods=['POST'])
def webhook():
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


def load_books(filename='books.csv'):
    """Loads books from a CSV file into a list of Book objects."""
    books = []
    try:
        with open(filename, mode='r', encoding='utf-8') as infile:
            # DictReader reads rows as dictionaries, which is perfect for our Book model
            reader = csv.DictReader(infile)
            for row in reader:
                books.append(Book(**row))
    except FileNotFoundError:
        # In a real app, you might want more robust error handling
        print(f"Error: The file {filename} was not found.")
    return books

# Load the books into memory when the application starts
BOOKS = load_books()

@app.route('/')
def index():
    """Renders the main page with the ISBN input form."""
    return render_template('index.html')

@app.route('/zoek', methods=['POST'])
def zoek():
    """Handles the book search logic."""
    submitted_isbn = request.form.get('isbn', '').strip()

    # --- Validation ---
    # 1. Check if the ISBN has the correct length
    if len(submitted_isbn) != 13:
        flash('Ongeldig ISBN. Een ISBN-nummer moet 13 karakters lang zijn.', 'error')
        return redirect(url_for('index'))

    # --- Search ---
    # 2. Look for the book in our list
    found_book = None
    for book in BOOKS:
        if book.isbn == submitted_isbn:
            found_book = book
            break

    # --- Result ---
    # 3. Handle found or not found cases
    if found_book:
        # If found, show the result page
        return render_template('resultaat.html', book=found_book)
    else:
        # If not found, show an error on the main page
        flash(f'Boek met ISBN {submitted_isbn} niet gevonden.', 'error')
        return redirect(url_for('index'))

if __name__ == '__main__':
    # Runs the app in debug mode for development
    app.run(debug=True)
