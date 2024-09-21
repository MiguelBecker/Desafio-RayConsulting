from googleapiclient.discovery import build

chave_api = "AIzaSyCj6jk6VyK7mrXU-kN6_LDeGTluOFkvcNM"
youtube = build('youtube', 'v3', developerKey=chave_api)
playlist_id = "PLfoNZDHitwjUv0pjTwlV1vzaE0r7UDVDR"

def getVideos(youtube, playlist_id, max_results=20):
    try:
        request = youtube.playlistItems().list(
            part="snippet,contentDetails",
            playlistId=playlist_id,
            maxResults=max_results
        )
        response = request.execute()
        return response['items']
    except Exception as e:
        print(f"Error getVideos: {e}")
        return []

def getViews(youtube, video_ids):
    try:
        video_stats_request = youtube.videos().list(
            part="snippet,statistics",
            id=",".join(video_ids)
        )
        video_stats_response = video_stats_request.execute()
        return video_stats_response['items']
    except Exception as e:
        print(f"Error getViews: {e}")
        return []

def main():
    videos = getVideos(youtube, playlist_id)
    video_ids = [item['contentDetails']['videoId'] for item in videos]
    video_stats = getViews(youtube, video_ids)
    videos_sorted = sorted(video_stats, key=lambda x: int(x['statistics']['viewCount']), reverse=True)
    for idx, video in enumerate(videos_sorted, start=1):
        video_title = video['snippet']['title']
        views = video['statistics']['viewCount']
        print(f"{idx}. Título: {video_title} - Visualizações: {views}")

if __name__ == "__main__":
    main()