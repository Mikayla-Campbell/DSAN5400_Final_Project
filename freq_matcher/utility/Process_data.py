import os
import logging
import gdown

def download_data(url: str, local_path: str) -> None:
    os.makedirs(os.path.dirname(local_path), exist_ok=True)

    if os.path.exists(local_path) and os.path.getsize(local_path) > 0:
        logging.info(f"File already exists and is non-empty at {local_path}. Skipping download.")
        return

    try:
        logging.info(f"Downloading file from {url} to {local_path}...")
        output = gdown.download(url, local_path, quiet=False)

        if output is None:
            raise ValueError("gdown.download returned None (check URL format or file permissions)")

        if not os.path.exists(local_path) or os.path.getsize(local_path) == 0:
            raise ValueError("File was downloaded but is empty")

        logging.info(f"Download complete: {local_path}")

    except Exception as e:
        logging.error(f"Failed to download or save the file: {e}")
        raise
