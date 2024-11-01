# YouTube Video Downloader and Comment Fetcher

A Python-based tool for searching, downloading, and analyzing mental health-related videos on YouTube. This project uses YouTube’s API to search for videos based on keywords, downloads them, fetches comments, processes emojis, and exports results to CSV files.

## Features

- **Video Search**: Searches for videos on YouTube based on specified keywords.
- **Video Download**: Downloads the highest resolution of each video.
- **Comment Retrieval**: Fetches comments for each video.
- **Emoji Processing**: Converts emojis in comments to text.
- **CSV Export**: Exports video and comment data to CSV files for further analysis.

## Prerequisites

- **Python 3.7+**
- **YouTube API Key**: Required to access YouTube data.
- **Google API Client Library**: For YouTube API integration.
- **Dotenv Library**: For securely loading environment variables.

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
   - Downloads the videos to the specified `download_path`.
   - Saves video comments and metadata to a CSV file for each keyword.

## Project Structure

- **`YouTubeClient`**: Manages YouTube API initialization and video search.
- **`VideoDownloader`**: Handles downloading YouTube videos.
- **`CommentFetcher`**: Fetches comments for each video.
- **`EmojiProcessor`**: Converts emojis to text.
- **`CSVExporter`**: Exports data to CSV.

## Configuration

All file paths and settings can be modified in the `__main__` block:
```python
download_path = "C:\\downloads"
csv_file_path = os.path.join(download_path, f"youtube_video_comments-{keyword}.csv")
