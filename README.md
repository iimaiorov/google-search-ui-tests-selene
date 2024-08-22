# Google Search UI Test Automation with Selene

## Project Description

This project is designed for automating the testing of the Google search user interface (UI) using the Selene library in Python. The included tests validate the correctness of the search functionality when entering various queries.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/iimaiorov/google-search-ui-tests-selene .git
   ```
2. Navigate to the project directory:
   ```bash
   cd google-search-ui-tests-selene 
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the tests using the following command:
```bash
pytest
```

## Project Structure

- **tests/**: Directory containing tests.
  - `test_google_should_search_selen.py`: Test for searching "yashaka/selen".
  - `test_google_should_search_nothing.py`: Test for searching with an invalid query.
- **requirements.txt**: File for installing necessary dependencies.
- **README.md**: Project information.
