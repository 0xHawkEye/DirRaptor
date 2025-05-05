# DirRaptor 🦖

**DirRaptor** is a high-speed, multithreaded directory brute-forcer designed for penetration testing and security research. It helps security professionals and researchers discover hidden directories and files on a web server using a specified wordlist. The tool supports real-time progress updates, handles retries on failure, and allows for customizable configuration through command-line arguments.

---

## 🚀 Features
- **Multithreaded Scanning**: Use multiple threads to speed up the directory scanning process.
- **Status Code Filtering**: Only report directories that return specified HTTP status codes (e.g., `200`, `403`).
- **Retry on Failure**: Automatically retries failed requests up to 3 times with customizable timeout.
- **Custom User-Agent**: Mimics a real browser to avoid detection by anti-bot measures.
- **Progress Bar**: Displays a real-time progress bar with speed and estimated time using `tqdm`.
- **Output to File**: Optionally saves found directories and their status codes to a specified output file.

---

## 🛠 Requirements

- **Python 3.6+** is required.
- **Required Python libraries**:
  - `requests`: To make HTTP requests.
  - `tqdm`: For the progress bar.

---

## 🧑‍💻 Installation

### 1. **Clone the Repository**

To get started with **DirRaptor**, clone this repository to your local machine:

```bash
git clone https://github.com/AyushKr41/DirRaptor.git
cd DirRaptor
```
### 2. **Install Dependencies**

You can install the required dependencies using the following command:

```bash
pip install requests tqdm
```

---

## 📄 Usage

### Running the Script
To run DirRaptor, use the following command:
```bash
python dirraptor.py <base_url> <path_to_wordlist> --threads <number_of_threads> --status <status_codes> --output <output_file>
```
### Arguments:

- `<base_url>`:The base URL of the target website `(e.g., https://example.com)`
- `<path_to_wordlist>`: Path to your directory wordlist file (e.g., `wordlist.txt`)
- `--threads <number_of_threads>`: Number of threads to use for scanning (default: `4` threads). More threads can speed up the scan.
- `--status <status_codes>`: A comma-separated list of HTTP status codes to report. For example, `200,403,404`. Default is `200,403`.
- `--output <output_file>`: Optionally specify a file to save found directories and their corresponding status codes (e.g., `found_directories.txt`).

### Example Command:
```bash
python dirraptor.py https://example.com wordlist.txt --threads 10 --status 200,403,401 --output found_directories.txt
```
This will:
- Scan the target website `https://example.com` using the `wordlist.txt` file.
- Use 10 threads for faster scanning.
- Report directories that return HTTP status codes `200`, `403`, or `401`.
- Save the results (found directories and their status codes) into the file `found_directories.txt`.

---

## 📚 How It Works

### 1. Target URL and Wordlist:
- The script takes a base URL (e.g., `https://example.com`) and a wordlist (list of potential directory names) as input.
- The tool then appends each directory from the wordlist to the base URL, forming the full URL to be tested.

### 2. Multithreaded Scanning:
- DirRaptor uses multiple threads to speed up the scanning process. Each thread works on a subset of directories from the wordlist.
- This parallelism helps significantly reduce the time it takes to scan large lists of directories.

### 3. Status Code Filtering:
- The script checks the HTTP response code for each directory (e.g., `200 OK`, `403 Forbidden`, `404 Not Found`).

- You can specify which status codes you are interested in, and DirRaptor will only report directories that return those codes.

### 4. Progress Tracking:
- A real-time progress bar is displayed in the terminal, showing how many directories have been checked, the total number of directories, and the speed of the scan.

- It uses tqdm for a smooth progress display.

### 5. Output to File:
- Optionally, the tool can save the found directories to a text file, along with the HTTP status code they returned.

---

## 🛠 Handling Errors and Retries
**DirRaptor** has built-in retry logic to handle temporary errors, such as connection timeouts or remote disconnections:
- If a request fails due to a network error or server disconnection, the script will automatically retry the request up to 3 times.
- You can adjust the retry settings and timeout duration if needed.

--- 

## 💡 Example Output
When you run the script, you will see output similar to this:

```bash
Scanning:  42%|███████████████▎                     | 420/1000 [00:05<00:07, 80.00it/s]
[+] Found (200): https://example.com/admin
[+] Found (403): https://example.com/private
[!] Thread-9 error: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
```
- The **progress bar** shows how far along the scan is.
- Directories that return specified status codes (e.g., 200, 403) will be printed.
- Any errors, such as connection issues, will be logged.

---

## 📄 Output File Example
If you specified an output file (e.g., found_directories.txt), the results will be saved in the following format:

```bash
https://example.com/admin (200)
https://example.com/private (403)
```

---

## 🧑‍💻 Contributing
If you'd like to contribute to DirRaptor, feel free to fork the repository, make changes, and submit a pull request.

---

## ✨ Credits
- **tqdm**: For the real-time progress bar.
- **requests**: For making the HTTP requests.

---

## 💬 Contact
For questions, suggestions, or issues, feel free to open an issue or reach out via **`rajayush4422@gmail.com`**.
