from googleapiclient.discovery import build

api_key = 'AIzaSyCR6YE5qgzaTmw6hR8m9GUi4QLb7WE4iGE'

youtube = build('youtube', 'v3', developerKey=api_key)

request = youtube.channels().list(part='statistics', forUsername='sentdex')

response = request.execute()

print(response)
