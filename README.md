# Metadata Extractor (EXIF)

## Overview

Metadata Extractor is a Python-based cybersecurity and digital forensics project developed as part of an internship.

The application extracts EXIF metadata from image files and displays useful information such as camera details, capture time, software used, and GPS data (if available).

---

## Features

- Read EXIF metadata
- Display camera make and model
- Display image capture date
- Display image resolution
- Display software information
- Display GPS information (if available)
- Error handling

---

## Technologies Used

- Python 3.x
- Pillow (PIL)

---

## Requirements

Install Pillow:

```bash
pip install Pillow
```

---

## Project Structure

```
MetadataExtractor/
│
├── metadata_extractor.py
├── sample.jpg
├── README.md
└── requirements.txt
```

---

## Run

```bash
python metadata_extractor.py
```

---

## Example

```
Enter image path:
sample.jpg
```

The program displays available EXIF metadata.

---

## Future Improvements

- Export metadata to CSV
- Export metadata to JSON
- Batch processing
- Folder scanning
- GUI using Tkinter

---

## Author

Avinash Mandal

Cyber Security Internship Project
