# Use LLM to analyse call transcript

## Overview
This project uses gtp 4.0 to analyse the customer side of the call transcript to Identify the sentiment (positive, negative, neutral) of the call and determine call outcome (issue resolved, follow-up action needed)

## Features
- Supports different document types (forms, catalogs, financial reports)
- Extracts text, images, tables, and charts with captions
- Organizes output in a structured folder system
- Provides JSON files linking extracted elements

## Setup

### Prerequisites
- Python 3.12.6
- pip (Python package installer)

### Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/pdf-extraction-app.git
   ```

2. Create and activate a virtual environment:
    ```bash
    py -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### Running the Application
- To run the application:
    ```bash
    py app.py
    ```
