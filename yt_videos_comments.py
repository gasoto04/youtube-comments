import requests
import os
import pandas as pd
#Import YouTubeDataAPI
from youtube_api import YouTubeDataAPI
from youtube_api.youtube_api_utils import *
import datetime

def get_videos_after_ndays(api_key, query, start_date, n_days):
    yt = YouTubeDataAPI(api_key)
    date_format = '%Y-%m-%d'

    date_start = datetime.datetime.strptime(start_date, date_format)
    videos_df = []
    for day in range(0, n_days):
        date = date_start + datetime.timedelta(days=day)
        df = pd.DataFrame(yt.search(q=query, max_results=500, search_type="video", order_by="viewCount",
                                    relevance_language='en',
                                    published_after=datetime.datetime.timestamp(datetime.datetime.combine(date, datetime.datetime.min.time())),
                                    published_before=datetime.datetime.timestamp(datetime.datetime.combine(date, datetime.datetime.max.time()))
                                   ))
        df['day'] = day + 1
        df['day_published'] = date
        videos_df.append(df)
        print(day, date, len(df))
    df_videos_all = pd.concat(videos_df)
    # We now know the videos that are there, but we are missing their characteristics
    day_list = list(df_videos_all['day'])
    day_published_list = list(df_videos_all['day_published'])
    video_list = list(df_videos_all['video_id'])
    df_videos_all = pd.DataFrame(yt.get_video_metadata(video_list)) # Getting the metadata of all
    df_videos_all['day'] = day_list
    df_videos_all['day_published'] = day_published_list
    df_videos_all.dropna(subset=['video_comment_count'], inplace=True) # Delete the ones with no comments
    df_videos_all['publish_date'] = pd.to_timedelta(df_videos_all['video_publish_date'], unit='s') + pd.to_datetime('1970-1-1')
    df_videos_all.set_index('video_id', inplace=True)
    return df_videos_all

def get_comments_all_videos(api_key, df_videos, get_replies=False):
    yt = YouTubeDataAPI(api_key)
    cxv_list = []
    df_videos['video_id'] = df_videos.index
    video_list = list(df_videos['video_id'])
    for video_id in video_list:
        df_comments = pd.DataFrame(yt.get_video_comments(video_id, get_replies=get_replies))
        cxv_list.append(df_comments)
        df_comments['day'] = df_videos.loc[video_id, 'day']
        df_comments['day_published'] = df_videos.loc[video_id, 'day_published']

    df_comments_all = pd.concat(cxv_list)
    df_comments_all['publish_date'] = pd.to_timedelta(df_comments_all['comment_publish_date'],
                                                      unit='s') + pd.to_datetime('1970-1-1')
    return df_comments_all