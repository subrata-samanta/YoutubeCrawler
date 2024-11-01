# 🎥 YouTube Video Downloader and Comment Fetcher

A Python-based tool for searching, downloading, and analyzing mental health-related videos on YouTube. This project uses YouTube’s API to search for videos based on keywords, downloads them, fetches comments, processes emojis, and exports results to CSV files. 🌟

## Features

- 🔍 **Video Search**: Searches for videos on YouTube based on specified keywords.
- ⬇️ **Video Download**: Downloads the highest resolution of each video.
- 💬 **Comment Retrieval**: Fetches comments for each video.
- 😊 **Emoji Processing**: Converts emojis in comments to text.
- 📊 **CSV Export**: Exports video and comment data to CSV files for further analysis.

## Prerequisites

- 🐍 **Python 3.7+**
- 🔑 **YouTube API Key**: Required to access YouTube data.
- 📚 **Google API Client Library**: For YouTube API integration.
- 🔒 **Dotenv Library**: For securely loading environment variables.

## Installation

1. **Clone the repository** by downloading or using version control to retrieve the project files. 
2. **Navigate to the project directory**.
3. **Install dependencies** listed in `requirements.txt`.
4. **Set up the `.env` file**:
   - Create a `.env` file in the project directory.
   - Add your YouTube API key to the file using the following format:
     ```plaintext
     DEVELOPER_KEY=your_youtube_api_key
     ```

## Usage

1. **Update the list of keywords** in the `__main__` section of `main.py`:
    ```python
    keywords = [
        "emotional video", "sad video", "depression video", "overcoming loneliness",
        # add more keywords as needed
    ]
    ```
2. **Run the program** by executing `main.py`.
3. **Output**:
   - Downloads the videos to the specified `download_path`. 📂
   - Saves video comments and metadata to a CSV file for each keyword. 🗃️

## Project Structure

- 🛠️ **`YouTubeClient`**: Manages YouTube API initialization and video search.
- 📥 **`VideoDownloader`**: Handles downloading YouTube videos.
- 💬 **`CommentFetcher`**: Fetches comments for each video.
- 😊 **`EmojiProcessor`**: Converts emojis to text.
- 📊 **`CSVExporter`**: Exports data to CSV.

## Configuration

All file paths and settings can be modified in the `__main__` block:

download_path = "C:\\downloads"
csv_file_path = os.path.join(download_path, f"youtube_video_comments-{keyword}.csv")

# 🛠️ Example Workflow

### 🔍 Search and Download
The program searches for videos based on a provided list of keywords. For each keyword, it retrieves video details from YouTube and downloads the videos in the highest resolution available. 📥

### 💬 Fetch Comments
After each video is downloaded, the program fetches comments for the video using the YouTube Data API. It gathers top comments based on a specified maximum number and includes additional details, such as like count. 👍

### 📊 Export Data
- Combines video metadata and comments into a single DataFrame.
- Converts emojis in comments to their textual representation.
- Exports the final processed data to a CSV file in the specified download path, making it ready for further analysis. 🗃️

# 📦 Dependencies
- `google-api-python-client`: For interacting with the YouTube API.
- `pytube`: For downloading videos from YouTube.
- `pandas`: For data handling and CSV export.
- `python-dotenv`: For loading environment variables.
- `emoji`: For handling emoji processing.

Install these dependencies by following the instructions in `requirements.txt`. 📜

# ⚙️ Environment Variables
- **DEVELOPER_KEY**: Add your YouTube API key to a `.env` file to authenticate with the YouTube Data API. 🔑

# 🛠️ Troubleshooting
- ⚠️ **API Quotas**: YouTube API has usage limits. Ensure your quota can support the number of searches and comment fetches.
- 📂 **Download Path**: Verify that the download path has write permissions.
- 📝 **Keyword Limit**: Too many keywords may exceed your daily quota or cause API call timeouts.

# 📄 License
This project is licensed under the MIT License. See the LICENSE file for details. 📃

# 🤝 Contributing
Contributions are welcome! Feel free to open issues or submit pull requests to add features or improve code quality. 🌟
