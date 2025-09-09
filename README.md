# Ubuntu Image Fetcher

A Python-based image downloading tool with Ubuntu-inspired messaging that allows you to fetch images from URLs and save them locally.

## 🌟 Features

- **Smart Image Detection**: Automatically validates that URLs point to actual images
- **Duplicate Prevention**: Skips downloading if the image already exists locally
- **Multiple URL Support**: Download multiple images at once by providing comma-separated URLs
- **Error Handling**: Robust error handling for network issues and invalid URLs
- **Organized Storage**: Automatically creates and organizes images in a `Fetched_Images` directory
- **Ubuntu Philosophy**: Embraces the Ubuntu spirit with community-focused messaging

## 📋 Requirements

- Python 3.6 or higher
- `requests` library

## 🚀 Installation

1. Clone or download this repository
2. Navigate to the project directory:
   ```bash
   cd week6
   ```
3. Install the required dependencies:
   ```bash
   pip install requests
   ```

## 💻 Usage

### Running the Script

Navigate to the `ubuntu_requests` directory and run the script:

```bash
cd ubuntu_requests
python image_fetcher.py
```

### Interactive Mode

The script will prompt you to enter image URLs:

```
Welcome to the Ubuntu Image Fetcher
A tool for mindfully collecting images from the web

Enter image URL(s) (comma separated if multiple): 
```

### Examples

**Single Image:**
```
Enter image URL(s): https://example.com/image.jpg
```

**Multiple Images:**
```
Enter image URL(s): https://example.com/image1.jpg, https://example.com/image2.png, https://example.com/image3.gif
```

## 📁 Project Structure

```
week6/
├── ubuntu_requests/
│   ├── image_fetcher.py          # Main script
│   └── Fetched_Images/           # Downloaded images directory
│       └── [downloaded images]
├── README.md                     # This file
└── .gitignore                   # Git ignore file
```

## 🔧 How It Works

1. **URL Validation**: The script fetches the URL and checks the `Content-Type` header to ensure it's an image
2. **Filename Extraction**: Extracts the filename from the URL path
3. **Directory Creation**: Creates the `Fetched_Images` directory if it doesn't exist
4. **Duplicate Check**: Verifies if the image already exists to avoid duplicates
5. **Download & Save**: Downloads and saves the image with appropriate success/error messages

## 📝 Output Messages

- `✓ Successfully fetched: filename.jpg` - Image downloaded successfully
- `✓ Image saved to Fetched_Images/filename.jpg` - Confirmation of save location
- `✗ Skipped (Not an image): url` - URL doesn't point to an image
- `⚠ Skipped (Already exists): filename.jpg` - Image already exists locally
- `✗ Connection error: error_message` - Network or connection issues
- `✗ An error occurred: error_message` - General error handling

## 🛠️ Error Handling

The script handles various error scenarios:

- **Network Issues**: Connection timeouts, DNS resolution failures
- **Invalid URLs**: Non-existent URLs or server errors
- **Non-Image Content**: URLs that don't point to image files
- **File System Issues**: Permission errors or disk space problems

## 🤝 Ubuntu Philosophy

This tool embodies the Ubuntu philosophy of "I am because we are" by:
- Providing a mindful approach to collecting web resources
- Strengthening community connections through shared resources
- Promoting responsible and considerate web scraping practices

## 📄 License

This project is part of a Python learning assignment and is intended for educational purposes.

## 🔄 Version History

- **v1.0**: Initial release with basic image fetching functionality
- Features include URL validation, duplicate prevention, and error handling

## 🤔 Troubleshooting

**Issue**: `ModuleNotFoundError: No module named 'requests'`
**Solution**: Install the requests library using `pip install requests`

**Issue**: Permission denied when saving images
**Solution**: Ensure you have write permissions in the current directory

**Issue**: Images not downloading despite valid URLs
**Solution**: Check your internet connection and verify the URLs are accessible

---

*"Connection strengthened. Community enriched."* - Ubuntu Image Fetcher