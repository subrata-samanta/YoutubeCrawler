import googleapiclient.discovery
from pytubefix import YouTube, Search
from pytubefix.cli import on_progress
from pytubefix.contrib.search import Filter
import pandas as pd
import os
import emoji
from dotenv import load_dotenv

load_dotenv()  # Load environment variables

class YouTubeClient:
    def __init__(self):
        api_service_name = "youtube"
        api_version = "v3"
        self.youtube = googleapiclient.discovery.build(
            api_service_name, api_version, developerKey=os.getenv("DEVELOPER_KEY")
        )

    def build_search_filters(self):
        """Build search filters for YouTube shorts."""
        return {
            'type': Filter.get_type("Shorts"),
            'sort_by': Filter.get_sort_by("Relevance")
        }

    def search_videos_by_keyword(self, keyword, max_results=1):
        """Search YouTube videos based on a keyword and return video details as a DataFrame."""
        filters = self.build_search_filters()
        results = Search(keyword, filters=filters)

        video_details = [
            {
                "video_id": video.video_id,
                "title": video.title,
                "watch_url": video.watch_url,
                "views": video.views,
                "likes": video.likes,
                "keywords": video.keywords
            }
            for video in results.shorts[:max_results]
        ]

        return pd.DataFrame(video_details)


class VideoDownloader:
    def __init__(self, download_path="C:\\downloads"):
        self.download_path = download_path

    def download_video(self, video_url):
        """Download a YouTube video by its URL."""
        yt = YouTube(video_url, on_progress_callback=on_progress)
        ys = yt.streams.get_highest_resolution()
        file_path = ys.download(output_path=self.download_path)
        print(f"Downloaded: {yt.title}")
        return file_path

    def download_videos(self, video_details):
        """Download a list of YouTube videos based on the DataFrame of video details."""
        for video in video_details['watch_url']:
            self.download_video(video)


class CommentFetcher:
    def __init__(self, youtube_client):
        self.youtube = youtube_client.youtube

    def get_comments(self, video_id, max_comments=200):
        """Fetch comments for a YouTube video by its ID and return as a DataFrame."""
        comments = []
        request = self.youtube.commentThreads().list(part="snippet", videoId=video_id, maxResults=100)

        while request and len(comments) < max_comments:
            response = request.execute()
            for item in response['items']:
                if len(comments) >= max_comments:
                    break
                comment = item['snippet']['topLevelComment']['snippet']
                comments.append([comment['likeCount'], comment['textOriginal'], comment['videoId']])

            nextPageToken = response.get('nextPageToken')
            if not nextPageToken:
                break
            request = self.youtube.commentThreads().list(part="snippet", videoId=video_id, maxResults=100, pageToken=nextPageToken)

        return pd.DataFrame(comments, columns=['like_count', 'text', 'video_id'])

    def fetch_comments_for_videos(self, video_ids, max_comments=200):
        """Fetch and combine comments for multiple videos."""
        all_comments = pd.DataFrame()
        for video_id in video_ids:
            comments_df = self.get_comments(video_id, max_comments)
            all_comments = pd.concat([all_comments, comments_df], ignore_index=True)
        return all_comments


class EmojiProcessor:
    @staticmethod
    def convert_emojis_to_text(df, column='text'):
        """Convert emojis in a specified DataFrame column to text representation."""
        df[column] = df[column].apply(lambda x: emoji.demojize(x) if isinstance(x, str) else x)
        return df


class CSVExporter:
    @staticmethod
    def save_to_csv(df, file_path):
        """Save a DataFrame to a CSV file."""
        df.to_csv(file_path, index=False, encoding='utf-8')
        print(f"Exported data to {file_path}")


def main(keyword, download_path, csv_file_path):
    """Main function to search videos, download, fetch comments, and export results."""
    youtube_client = YouTubeClient()
    downloader = VideoDownloader(download_path)
    comment_fetcher = CommentFetcher(youtube_client)
    max_results = 1

    # Search and download videos
    video_details_df = youtube_client.search_videos_by_keyword(keyword, max_results)
    downloader.download_videos(video_details_df)

    # Fetch comments for each video
    all_comments = comment_fetcher.fetch_comments_for_videos(video_details_df['video_id'])

    # Merge video details with comments and process emojis
    final_df = video_details_df.merge(all_comments, on='video_id', how='left')
    final_df = EmojiProcessor.convert_emojis_to_text(final_df)

    # Export final DataFrame to CSV
    CSVExporter.save_to_csv(final_df, csv_file_path)


if __name__ == "__main__":
    keywords = [
        "emotional video", "sad video", "breakup video", "depression video", "lost hope",
        "anxiety relief video", "stress relief video", "overcoming loneliness", "coping with grief",
        "struggle with self-esteem", "self-compassion", "heartbreak recovery", "dealing with failure",
        "hopeful recovery story", "self-care journey", "coping with change", "mental health awareness",
        "life challenges video", "self-healing journey", "inner peace video", "mental health struggles",
        "uplifting story", "overcoming mental health", "supportive video", "finding happiness video",
        "mindfulness and peace"
    ]

    download_path = "C:\\downloads"
    for keyword in keywords:
        print(f"Processing keyword: {keyword}")
        csv_file_path = os.path.join(download_path, f"youtube_video_comments-{keyword}.csv")
        main(keyword, download_path, csv_file_path)
