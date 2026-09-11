# Data Extraction and Secure Validation

## Project Overview

This project identifies and extracts different types of information from raw text using Python and regular expressions. The program reads data from the input file then saves the extracted information in JSON format.

## Data Types Extracted

The program extracts:
- Email addresses
- Credit card numbers
- URLs
- Phone numbers

## ALU Email Validation

The program specifically recognizes three ALU domains:
- @alueducation.com
- @alumni.alueducation.com
- @si.alueducation.com
Emails using different domains are not considered ALU email addresses.

## Security Considerations

- The input file is treated as untrusted data.
- The program does not execute commands, scripts, or instructions contained in the input.

- Credit card numbers are not written to the output in full. Only the first four and last four digits are retained while the middle digits are masked.

- Malformed input is ignored when it does not match the expected patterns.

- The extraction process only reads the input as text and produces structured JSON output.

## Project Structure

alu-regex-data-extraction_pkeza1-rgb/
├── input/
│   └── raw-text.txt
├── src/
│   └── main.py
├── output/
│   └── sample-output.json
└── README.md

## How To Run

To run the program, execute the Python file located inside the `src` folder:

```bash
python3 src/main.py
```

To display the extracted output:

```bash
cat output/sample-output.json
```

## Output

The extracted data is stored in `output/sample-output.json`.
