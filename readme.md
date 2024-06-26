

# Automated Legal Document Analysis Software
![](<python/image/JURIS IQ.png>)
This is an automated legal document analysis software built using Streamlit. The software allows users to upload text files, scans the text for legal parameters, and provides an analysis based on standard global best practices for legal document analysis. Such analysis can not only help a lawyer but also benefit a common man, in a way of getting a preliminary understanding of any legal document.


## Features

- **File Upload**: Allows users to upload `.txt` and `.docx` files from the sidebar.
- **Document Content Display**: Displays the content of the uploaded document.
- **Legal Parameters Analysis**: Scans the document for specific legal parameters like "Agreement," "Termination," "Confidentiality," and "Warranty" clauses.
- **Sentiment Analysis**: Performs sentiment analysis on the entire document text.
- **Keyword Search**: Allows users to search for specific keywords within the document.
- **Named Entity Recognition**: Extracts and displays named entities from the document.(Excluded from this version)

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/kshula/JurisIQ.git
    cd python
    ```

2. Install the required libraries:

    ```sh
    pip install streamlit spacy textblob python-docx
    ```

3. Download the spaCy language model:

    ```sh
    python -m spacy download en_core_web_sm
    ```

## Usage

1. Run the Streamlit app:

    ```sh
    streamlit run main.py
    ```

2. Open your web browser and navigate to the URL provided by Streamlit (usually `http://localhost:8501`).

3. Use the sidebar to upload a text file (`.txt` or `.docx`).

4. The document content will be displayed, and the analysis results will be shown in different sections:
    - **Legal Parameters Analysis**: Displays detected legal clauses.
    - **Sentiment Analysis**: Shows the sentiment polarity and subjectivity.
    - **Keyword Search**: Allows searching for specific keywords within the document.
    - **Named Entities**: Lists named entities extracted from the document.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or new features.

## Contact

For questions or suggestions, please contact [Kampamba Shula](mailto:kampambashula@gmail.com).

