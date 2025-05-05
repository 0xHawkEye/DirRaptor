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
git clone https://github.com/yourusername/DirRaptor.git
cd DirRaptor
