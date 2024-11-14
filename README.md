 URL Extractor App

This is a simple Python application with a Graphical User Interface (GUI) that allows users to enter a URL, fetch the content of the page, and extract all clickable links. The links are saved to a CSV file. The application uses the `requests` and `BeautifulSoup` libraries for web scraping and `tkinter` for the GUI.

---

## Features

- Fetches all clickable links from a given URL.
- Saves the extracted links into a CSV file.
- User-friendly GUI for easy operation.

---

## Requirements

Make sure you have the following Python libraries installed:

- `requests`
- `beautifulsoup4`
- `tkinter` (This is included with Python)

You can install the required packages using:
```bash
pip install requests beautifulsoup4
```

---

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/irifat602/url-extractor-app.git
   ```
2. Navigate to the project directory:
   ```bash
   cd url-extractor-app
   ```
3. Run the Python script:
   ```bash
   python your_script_name.py
   ```

---

## Creating a Standalone Executable (optional)

You can create a standalone executable file using **PyInstaller**. Follow the instructions below:

### Step 1: Install PyInstaller
Make sure PyInstaller is installed. If not, you can install it using:
```bash
pip install pyinstaller
```

### Step 2: Create the Executable
Navigate to the directory where your script is located and run:
```bash
pyinstaller --onefile your_script_name.py
```
Replace `your_script_name.py` with the name of your Python file.

- This will generate an executable in the `dist` folder.

### Step 3: Additional PyInstaller Options
- To add an icon to your executable:
  ```bash
  pyinstaller --onefile --icon=your_icon.ico your_script_name.py
  ```
  Replace `your_icon.ico` with the path to your icon file.
- To hide the console window (for GUI apps):
  ```bash
  pyinstaller --onefile --noconsole your_script_name.py
  ```

### Step 4: Running Your Executable
- The executable file will be located in the `dist` folder. You can distribute this file as a standalone application.

---

## Notes

- **Cross-Platform Builds**: PyInstaller does not support cross-compilation. You need to build the executable on the target operating system (e.g., use Windows for a Windows executable).
- **Dependencies**: The standalone executable includes the Python interpreter and all dependencies, so the file size may be large.

---

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them with descriptive messages.
4. Submit a pull request.

---

## License

This project is licensed under the MIT License. 

---

## Contact

For any questions or issues, feel free to open an issue on GitHub or contact me at r.rupok@myyahoo.com

---

Feel free to modify the file with your own details, such as your GitHub username, repository link, script name, and contact email. 
