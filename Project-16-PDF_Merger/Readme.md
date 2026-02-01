# 📑 PDF Merger

This Python script automatically merges all PDF files located in a specified directory into a single PDF file.

## 🚀 Features

- **Directory Scan:** Scans all files in the provided folder path.
- **Auto-Sort:** Sorts files alphabetically before merging to ensure correct page order.
- **Error Handling:** Automatically skips non-PDF files or corrupted files without crashing the program (`try-except` block).
- **Smart Naming:** Automatically appends the `.pdf` extension to the output filename if omitted.

## 🛠️ Installation

1.  Ensure you have Python installed.
2.  Install the required library:
    ```bash
    pip install -r requirements.txt
    ```
    _(Or manually: `pip install pypdf`)_

## 💻 Usage

1.  Run the script:
    ```bash
    python main.py
    ```
2.  **Enter Path:** Paste the full path of the folder containing your PDF files (the script automatically handles quotes).
3.  **Enter Filename:** Type a name for your new merged file (e.g., `AllNotes`).

The program will process the files and save the merged PDF in the same directory.

---

_Developed by BerkeKaracan_
