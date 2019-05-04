#!/usr/bin/python

# This sample executes a search request for the specified search term.
# Sample usage:
#   python search.py --q=surfing --max-results=10
# NOTE: To use the sample, you must provide a developer key obtained
#       in the Google APIs Console. Search for "REPLACE_ME" in this code
#       to find the correct place to provide that key..

import argparse

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from third import socks
import socket
# Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
# tab of
#   https://cloud.google.com/console
# Please ensure that you have enabled the YouTube Data API for your project.
DEVELOPER_KEY = 'AIzaSyCN_ntN3JgDHFxQ6quU7XcrQACxn4xmldI'
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

def youtube_search(options):
  socks.setdefaultproxy(socks.PROXY_TYPE_HTTP, "127.0.0.1",8388)
  socket.socket = socks.socksocket
  youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    developerKey=DEVELOPER_KEY)

  # Call the search.list method to retrieve results matching the specified
  # query term.
  search_response = youtube.search().list(
    q=options["q"],
    part='id,snippet',
    maxResults=options["max_results"]
  ).execute()

  videos = []
  channels = []
  playlists = []

  # Add each result to the appropriate list, and then display the lists of
  # matching videos, channels, and playlists.
  for search_result in search_response.get('items', []):
    if search_result['id']['kind'] == 'youtube#video':
      videos.append({'video_title':search_result['snippet']['title'],
                     'videoId':search_result['id']['videoId']});
      #videos.append('%s (%s)' % (search_result['snippet']['title'],
      #                           search_result['id']['videoId']))
    elif search_result['id']['kind'] == 'youtube#channel':
      channels.append({
        'video_title':search_result['snippet']['title'],
        'channelId':search_result['id']['channelId']
      });
      #channels.append('%s (%s)' % (search_result['snippet']['title'],
      #                             search_result['id']['channelId']))
    elif search_result['id']['kind'] == 'youtube#playlist':
      playlists.append({
        'video_title':search_result['snippet']['title'],
        'playlistId':search_result['id']['playlistId']
      });
      #playlists.append('%s (%s)' % (search_result['snippet']['title'],
      #                              search_result['id']['playlistId']))

  #print ('Videos:\n', '\n'.join(videos), '\n')
  #print ('Channels:\n', '\n'.join(channels), '\n')
  #print ('Playlists:\n', '\n'.join(playlists), '\n')
  result = {'Videos':videos,'Channels':channels, 'Playlists':playlists};
  return result

#if __name__ == '__main__':
#  parser = argparse.ArgumentParser()
#  parser.add_argument('--q', help='Search term', default='Google')
#  parser.add_argument('--max-results', help='Max results', default=25)
#  args = parser.parse_args()
#  
#  try:
#    youtube_search(args)
#  except HttpError as e:
#    print('An HTTP error %d occurred:\n%s' % (e.resp.status, e.content))
#  except BaseException as e:
#    print('An  error %d occurred:\n%s' % (e.resp.status, e.content))