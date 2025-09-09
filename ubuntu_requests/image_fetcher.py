import requests
import os
from urllib.parse import urlparse

def fetch_image(url):
    try:
        # Fetch the image
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise error for bad status codes

        # Check if response is an image
        content_type = response.headers.get("Content-Type", "")
        if "image" not in content_type:
            print(f"✗ Skipped (Not an image): {url}")
            return

        # Extract filename from URL
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)

        if not filename:  # Fallback if URL has no filename
            filename = "downloaded_image.jpg"

        # Ensure directory exists
        os.makedirs("Fetched_Images", exist_ok=True)
        filepath = os.path.join("Fetched_Images", filename)

        # Check for duplicate
        if os.path.exists(filepath):
            print(f"⚠ Skipped (Already exists): {filename}")
            return

        # Save the image
        with open(filepath, "wb") as f:
            f.write(response.content)

        print(f"✓ Successfully fetched: {filename}")
        print(f"✓ Image saved to {filepath}")

    except requests.exceptions.RequestException as e:
        print(f"✗ Connection error: {e}")
    except Exception as e:
        print(f"✗ An error occurred: {e}")


def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")

    urls = input("Enter image URL(s) (comma separated if multiple): ").split(",")

    for url in urls:
        url = url.strip()
        if url:  # Skip empty inputs
            fetch_image(url)

    print("\nConnection strengthened. Community enriched.")


if __name__ == "__main__":
    main()
