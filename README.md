# Resume-Parser

This project is a Resume Parser tool that extracts key information such as a candidate's name, skills, and work experience from plain text resumes. It is built using Python and leverages the **spaCy** library for natural language processing.

## Features

- **Extract Name:** Identifies the candidate's name based on patterns.
- **Extract Skills:** Recognizes technical and programming skills explicitly mentioned in the resume.
- **Extract Work Experience:** Identifies work experience details based on predefined patterns.
- **Batch Processing:** Processes multiple resumes stored in a folder.
- **Customizable Patterns:** Allows flexibility to refine or extend patterns for name, skills, and experience extraction.

## Prerequisites

- Python 3.x
- spaCy library
- A pre-trained spaCy model (e.g., `en_core_web_sm`)

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```

2. Navigate to the project directory:
   ```bash
   cd resume-parser
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Download the spaCy model:
   ```bash
   python -m spacy download en_core_web_sm
   ```

## Usage

1. Place the resumes in `.txt` format in a folder.

2. Run the script:
   ```bash
   python Resume_Parser.py
   ```

3. Enter the folder path when prompted:
   ```bash
   Enter the path to the folder containing resume files: /path/to/folder
   ```

4. The tool will process each resume and display the extracted information (Name, Skills, Experience) in the terminal.

5. The parsed data will be returned as a Python dictionary for further use.

## Example

Assume you have a folder `/resumes` with the following text files:
- `resume1.txt`
- `resume2.txt`

When the tool processes these files, the output will look something like this:

```
Candidate: John Doe
Skills: Python, Java, HTML
Experience: 5 years of software development experience

==============================

Candidate: Jane Smith
Skills: JavaScript, CSS, Swift
Experience: Extensive experience in mobile app development

==============================
```

## Customization

- **Name Patterns:** Modify the `name_pattern` in the `extract_information` function to adapt to different naming conventions.
- **Skills:** Add or refine the `programming_skills` list to include additional technologies or domains.
- **Experience Patterns:** Update the `experience_pattern` to extract specific experience formats.

## Limitations

- The tool is designed to work with plain text resumes. PDFs or other formats need to be converted to `.txt`.
- Extraction patterns may need refinement to handle various resume structures and styles effectively.

## Future Improvements

- Support for additional resume formats (e.g., PDF, Word).
- Advanced NLP techniques for better accuracy.
- Integration with a database to store extracted data.
- GUI for non-technical users.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your improvements or bug fixes.


