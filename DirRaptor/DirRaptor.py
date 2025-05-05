import requests
import threading
import argparse
import sys
from tqdm import tqdm

# Global variables for thread synchronization
checked_directories = 0
lock = threading.Lock()
progress_bar = None

def explore_directories(base_url, directory_list, thread_id, num_threads, status_codes, output_file):
    global checked_directories

    for i in range(len(directory_list)):
        if i % num_threads == thread_id:  # Distribute directories among threads
            directory = directory_list[i].strip()
            url = f"{base_url.rstrip('/')}/{directory}"

            try:
                response = requests.get(url, timeout=5)
                code = response.status_code
            except requests.RequestException as e:
                with lock:
                    print(f"\n[!] Thread-{thread_id} error: {e}")
                continue

            with lock:
                checked_directories += 1
                if progress_bar:
                    progress_bar.update(1)

            if code in status_codes:
                msg = f"[+] Found ({code}): {url}"
                with lock:
                    print(msg)
                    if output_file:
                        with open(output_file, 'a') as f:
                            f.write(f"{url} ({code})\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='DirRaptor - Recursive Web Directory Bruteforcer 🦖')
    parser.add_argument('url', type=str, help='Base URL (e.g., https://example.com)')
    parser.add_argument('wordlist', type=str, help='Path to directory wordlist')
    parser.add_argument('--threads', type=int, default=4, help='Number of threads (default: 4)')
    parser.add_argument('--status', type=str, default='200,403', help='Comma-separated status codes to report (default: 200,403)')
    parser.add_argument('--output', type=str, help='Output file to save found directories (optional)')
    args = parser.parse_args()

    base_url = args.url
    num_threads = args.threads
    status_codes = list(map(int, args.status.split(',')))
    output_file = args.output

    try:
        with open(args.wordlist, 'r') as f:
            directories = f.read().splitlines()
    except Exception as e:
        print(f"[!] Failed to read wordlist: {e}")
        sys.exit(1)

    total_directories = len(directories)
    progress_bar = tqdm(total=total_directories, desc="Scanning", ncols=100)

    threads = []
    for i in range(num_threads):
        thread = threading.Thread(
            target=explore_directories,
            args=(base_url, directories, i, num_threads, status_codes, output_file)
        )
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    progress_bar.close()
    print("\n[✓] Scanning complete.")
