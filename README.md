# SendEmailsToCSVList
# Automated Email Sender

This project is a Python script that automatically sends personalized emails with attached bills to a list of contacts. It utilizes the `yagmail` library for sending emails and reads contact information from a CSV file.

## Features

- Automatically send personalized emails to multiple recipients.
- Attach bill files to each email based on file paths specified in the CSV.
- Simple setup with environment variables for email credentials.

## Prerequisites

Before you begin, ensure you have met the following requirements:
- Python 3.x installed on your machine.
- Required Python libraries: `yagmail`, `python-dotenv`, `pandas`.

## Installation

1. Clone the repository:
    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2. Install the required Python libraries:
    ```bash
    pip install yagmail python-dotenv pandas
    ```

3. Set up your environment variables:
    - Create a `.env` file in the project directory.
    - Add your email credentials to the `.env` file:
      ```
      EMAIL_SENDER=your_email@example.com
      EMAIL_PASSWORD=your_email_password
      ```

4. Prepare your contacts CSV file (`contacts.csv`):
    - Ensure it contains the following columns: `email`, `name`, `amount`.

## Usage

1. Run the Python script:
    ```bash
    python main.py
    ```

2. The script will read the contact information from the `contacts.csv` file and send emails with the specified attachments.

## Example

Here’s a sample content for `contacts.csv`:
```csv
email,name,amount
john.doe@example.com,John Doe,100
jane.doe@example.com,Jane Doe,200
