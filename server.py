import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/cricketapilive/api/cricbuzz-cricket'

mcp = FastMCP('cricbuzz-cricket')

@mcp.tool()
def matches_live() -> dict: 
    '''GET Live Matches'''
    url = 'https://cricbuzz-cricket.p.rapidapi.com/matches/v1/live'
    headers = {'x-rapidapi-host': 'cricbuzz-cricket.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def matches_upcoming() -> dict: 
    '''List Upcoming Matches'''
    url = 'https://cricbuzz-cricket.p.rapidapi.com/matches/v1/upcoming'
    headers = {'x-rapidapi-host': 'cricbuzz-cricket.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def matches_recent() -> dict: 
    '''List Recent Matches'''
    url = 'https://cricbuzz-cricket.p.rapidapi.com/matches/v1/recent'
    headers = {'x-rapidapi-host': 'cricbuzz-cricket.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def schedules_list(lastTime: Annotated[Union[int, float, None], Field(description="For paging purpose, leave empty to load the first page, or an Epoch timestamp value in milliseconds (Ex : 1640883600000) to load the next page. You are interested in the 'startDt' field returned right in this endpoint. Default: 0")] = None) -> dict: 
    '''List scheduled matches'''
    url = 'https://cricbuzz-cricket.p.rapidapi.com/schedule/v1/international'
    headers = {'x-rapidapi-host': 'cricbuzz-cricket.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'lastTime': lastTime,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def series_list(type: Annotated[str, Field(description='One of the followings : international|league|domestic|women')]) -> dict: 
    '''List series'''
    url = 'https://cricbuzz-cricket.p.rapidapi.com/series/v1/international'
    headers = {'x-rapidapi-host': 'cricbuzz-cricket.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'type': type,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def series_list_archives(year: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                         lastId: Annotated[Union[int, float, None], Field(description='For paging purpose, leave empty to load the first page, or the value of id field returned right in this endpoint. Default: 0')] = None) -> dict: 
    '''List archived series'''
    url = 'https://cricbuzz-cricket.p.rapidapi.com/series/v1/archives/international'
    headers = {'x-rapidapi-host': 'cricbuzz-cricket.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'year': year,
        'lastId': lastId,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def series_get_matches(seriesId: Annotated[Union[int, float], Field(description='The value of id field returned in …/series/list or …/series/list-archives endpoints. Default: 3641')]) -> dict: 
    '''Get recent and upcoming matches by series'''
    url = 'https://cricbuzz-cricket.p.rapidapi.com/series/v1/3641'
    headers = {'x-rapidapi-host': 'cricbuzz-cricket.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'seriesId': seriesId,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def series_get_news(seriesId: Annotated[Union[int, float], Field(description='The value of id field returned in …/series/list or …/series/list-archives endpoints. Default: 3636')]) -> dict: 
    '''Get news by series'''
    url = 'https://cricbuzz-cricket.p.rapidapi.com/news/v1/series/3636'
    headers = {'x-rapidapi-host': 'cricbuzz-cricket.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'seriesId': seriesId,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def series_get_squads(seriesId: Annotated[Union[int, float], Field(description='The value of id field returned in …/series/list or …/series/list-archives endpoints. Default: 3718')]) -> dict: 
    '''Get squads by series'''
    url = 'https://cricbuzz-cricket.p.rapidapi.com/series/v1/3718/squads'
    headers = {'x-rapidapi-host': 'cricbuzz-cricket.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'seriesId': seriesId,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def series_get_players(seriesId: Annotated[Union[int, float], Field(description='The value of id field returned in …/series/list or …/series/list-archives endpoints. Default: 3718')],
                       squadId: Annotated[Union[int, float], Field(description='The value of squadId field returned in …/series/get-squads endpoint Default: 15826')]) -> dict: 
    '''Get players by squad and series'''
    url = 'https://cricbuzz-cricket.p.rapidapi.com/series/v1/3718/squads/15826'
    headers = {'x-rapidapi-host': 'cricbuzz-cricket.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'seriesId': seriesId,
        'squadId': squadId,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def series_get_venues(seriesId: Annotated[Union[int, float], Field(description='The value of id field returned in …/series/list or …/series/list-archives endpoints. Default: 3718')]) -> dict: 
    '''Get venues by series'''
    url = 'https://cricbuzz-cricket.p.rapidapi.com/series/v1/3718/venues'
    headers = {'x-rapidapi-host': 'cricbuzz-cricket.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'seriesId': seriesId,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def series_get_points_table(seriesId: Annotated[Union[int, float], Field(description='The value of id field returned in …/series/list or …/series/list-archives endpoints. Default: 3718')]) -> dict: 
    '''Get points table by series'''
    url = 'https://cricbuzz-cricket.p.rapidapi.com/stats/v1/series/3718/points-table'
    headers = {'x-rapidapi-host': 'cricbuzz-cricket.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'seriesId': seriesId,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def series_get_stats_filters(seriesId: Annotated[Union[int, float], Field(description='The value of id field returned in …/series/list or …/series/list-archives endpoints. Default: 3718')]) -> dict: 
    '''Get supported filters'''
    url = 'https://cricbuzz-cricket.p.rapidapi.com/stats/v1/series/3718'
    headers = {'x-rapidapi-host': 'cricbuzz-cricket.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'seriesId': seriesId,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def series_get_stats(statsType: Annotated[str, Field(description="The value of 'value' field returned in …/series/get-stats-filter endpoint")]) -> dict: 
    '''Get stats'''
    url = 'https://cricbuzz-cricket.p.rapidapi.com/stats/v1/series/3718'
    headers = {'x-rapidapi-host': 'cricbuzz-cricket.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'statsType': statsType,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def teams_list(type: Annotated[str, Field(description='international|league|domestic|women')]) -> dict: 
    '''List teams'''
    url = 'https://cricbuzz-cricket.p.rapidapi.com/teams/v1/international'
    headers = {'x-rapidapi-host': 'cricbuzz-cricket.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'type': type,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def teams_get_schedules(teamId: Annotated[Union[int, float], Field(description='The value of teamId field returned in …/teams/list endpoint Default: 2')]) -> dict: 
    '''Get scheduled matches for a team'''
    url = 'https://cricbuzz-cricket.p.rapidapi.com/teams/v1/2/schedule'
    headers = {'x-rapidapi-host': 'cricbuzz-cricket.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'teamId': teamId,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def teams_get_results(teamId: Annotated[Union[int, float], Field(description='The value of teamId field returned in …/teams/list endpoint Default: 2')]) -> dict: 
    '''Get matched results by team'''
    url = 'https://cricbuzz-cricket.p.rapidapi.com/teams/v1/2/results'
    headers = {'x-rapidapi-host': 'cricbuzz-cricket.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'teamId': teamId,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def teams_get_news(teamId: Annotated[Union[int, float], Field(description='The value of teamId field returned in …/teams/list endpoint Default: 2')]) -> dict: 
    '''Get news by team'''
    url = 'https://cricbuzz-cricket.p.rapidapi.com/news/v1/team/2'
    headers = {'x-rapidapi-host': 'cricbuzz-cricket.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'teamId': teamId,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def teams_get_players(teamId: Annotated[Union[int, float], Field(description='The value of teamId field returned in …/teams/list endpoint Default: 2')]) -> dict: 
    '''Get players by team'''
    url = 'https://cricbuzz-cricket.p.rapidapi.com/teams/v1/2/players'
    headers = {'x-rapidapi-host': 'cricbuzz-cricket.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'teamId': teamId,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def teams_get_stats_filters(teamId: Annotated[Union[int, float], Field(description='The value of teamId field returned in …/teams/list endpoint Default: 2')]) -> dict: 
    '''Get supported filters'''
    url = 'https://cricbuzz-cricket.p.rapidapi.com/stats/v1/team/2'
    headers = {'x-rapidapi-host': 'cricbuzz-cricket.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'teamId': teamId,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def teams_get_stats(statsType: Annotated[str, Field(description="The value of 'value' field returned in …/teams/get-stats-filter endpoint")],
                    year: Annotated[Union[int, float, None], Field(description='Specify year to get stats. Ex : 2021 Default: 0')] = None,
                    matchType: Annotated[Union[int, float, None], Field(description='The value of matchTypeId field returned right in this endpoint Default: 0')] = None,
                    team: Annotated[Union[int, float, None], Field(description="The value of 'teamId' field returned right in this endpoint Default: 0")] = None,
                    opponent: Annotated[Union[int, float, None], Field(description="The value of 'teamId' field returned right in this endpoint Default: 0")] = None) -> dict: 
    '''Get stats by team'''
    url = 'https://cricbuzz-cricket.p.rapidapi.com/stats/v1/team/2'
    headers = {'x-rapidapi-host': 'cricbuzz-cricket.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'statsType': statsType,
        'year': year,
        'matchType': matchType,
        'team': team,
        'opponent': opponent,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def venues_get_info(venueId: Annotated[Union[int, float], Field(description='The value of id field returned in …/series/get-venues endpoint Default: 45')]) -> dict: 
    '''Get venue info'''
    url = 'https://cricbuzz-cricket.p.rapidapi.com/venues/v1/45'
    headers = {'x-rapidapi-host': 'cricbuzz-cricket.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'venueId': venueId,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def venues_get_stats(venueId: Annotated[Union[int, float], Field(description='The value of id field returned in …/series/get-venues endpoint Default: 24')]) -> dict: 
    '''Get stats by venue'''
    url = 'https://cricbuzz-cricket.p.rapidapi.com/stats/v1/venue/24'
    headers = {'x-rapidapi-host': 'cricbuzz-cricket.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'venueId': venueId,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def venues_get_matches(venueId: Annotated[Union[int, float], Field(description='The value of id field returned in …/series/get-venues endpoint Default: 45')]) -> dict: 
    '''Get scheduled matches by venue'''
    url = 'https://cricbuzz-cricket.p.rapidapi.com/venues/v1/45/matches'
    headers = {'x-rapidapi-host': 'cricbuzz-cricket.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'venueId': venueId,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def players_list_trending() -> dict: 
    '''List trending players'''
    url = 'https://cricbuzz-cricket.p.rapidapi.com/stats/v1/player/trending'
    headers = {'x-rapidapi-host': 'cricbuzz-cricket.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def players_get_career(playerId: Annotated[Union[int, float], Field(description='The value of id field returned in …/players/list-trending, …/players/search endpoints Default: 8733')]) -> dict: 
    '''Get player career'''
    url = 'https://cricbuzz-cricket.p.rapidapi.com/stats/v1/player/8733/career'
    headers = {'x-rapidapi-host': 'cricbuzz-cricket.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'playerId': playerId,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def players_get_news(playerId: Annotated[Union[int, float], Field(description='The value of id field returned in …/players/list-trending, …/players/search endpoints Default: 8733')]) -> dict: 
    '''Get news by player'''
    url = 'https://cricbuzz-cricket.p.rapidapi.com/news/v1/player/8733'
    headers = {'x-rapidapi-host': 'cricbuzz-cricket.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'playerId': playerId,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def players_get_bowling(playerId: Annotated[Union[int, float], Field(description='The value of id field returned in …/players/list-trending, …/players/search endpoints Default: 8733')]) -> dict: 
    '''Get player's bowling'''
    url = 'https://cricbuzz-cricket.p.rapidapi.com/stats/v1/player/8733/bowling'
    headers = {'x-rapidapi-host': 'cricbuzz-cricket.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'playerId': playerId,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def players_get_batting(playerId: Annotated[Union[int, float], Field(description='The value of id field returned in …/players/list-trending, …/players/search endpoints Default: 8733')]) -> dict: 
    '''Get player's batting'''
    url = 'https://cricbuzz-cricket.p.rapidapi.com/stats/v1/player/8733/batting'
    headers = {'x-rapidapi-host': 'cricbuzz-cricket.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'playerId': playerId,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def players_get_info(playerId: Annotated[Union[int, float], Field(description='The value of id field returned in …/players/list-trending, …/players/search endpoints Default: 6635')]) -> dict: 
    '''Get player info'''
    url = 'https://cricbuzz-cricket.p.rapidapi.com/stats/v1/player/6635'
    headers = {'x-rapidapi-host': 'cricbuzz-cricket.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'playerId': playerId,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def players_search(plrN: Annotated[str, Field(description='')]) -> dict: 
    '''Search player by name'''
    url = 'https://cricbuzz-cricket.p.rapidapi.com/stats/v1/player/search'
    headers = {'x-rapidapi-host': 'cricbuzz-cricket.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'plrN': plrN,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def news_list(type: Annotated[str, Field(description='One of the followings : index|premiumIndex')]) -> dict: 
    '''List latest news'''
    url = 'https://cricbuzz-cricket.p.rapidapi.com/news/v1/index'
    headers = {'x-rapidapi-host': 'cricbuzz-cricket.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'type': type,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def news_detail(newsId: Annotated[Union[int, float], Field(description='The value of story/id field returned in …/news/list …/news/list-by-category …/news/list-by-topic endpoint Default: 122025')]) -> dict: 
    '''Get news detail'''
    url = 'https://cricbuzz-cricket.p.rapidapi.com/news/v1/detail/122025'
    headers = {'x-rapidapi-host': 'cricbuzz-cricket.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'newsId': newsId,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def news_get_categories() -> dict: 
    '''Get all available categories'''
    url = 'https://cricbuzz-cricket.p.rapidapi.com/news/v1/cat'
    headers = {'x-rapidapi-host': 'cricbuzz-cricket.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def news_list_by_category(categoryId: Annotated[Union[int, float], Field(description='Filter news by category, the value of id field returned in …/news/get-categories Default: 5')]) -> dict: 
    '''List latest news by category'''
    url = 'https://cricbuzz-cricket.p.rapidapi.com/news/v1/cat/5'
    headers = {'x-rapidapi-host': 'cricbuzz-cricket.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'categoryId': categoryId,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def news_get_topics() -> dict: 
    '''Get all available topics'''
    url = 'https://cricbuzz-cricket.p.rapidapi.com/news/v1/topics'
    headers = {'x-rapidapi-host': 'cricbuzz-cricket.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def news_list_by_topic(topicId: Annotated[Union[int, float], Field(description='Filter news by topic, the value of id field returned in …/news/get-topics Default: 349')]) -> dict: 
    '''List latest news by topic'''
    url = 'https://cricbuzz-cricket.p.rapidapi.com/news/v1/topics/349'
    headers = {'x-rapidapi-host': 'cricbuzz-cricket.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'topicId': topicId,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def photos_list() -> dict: 
    '''List photo galleries'''
    url = 'https://cricbuzz-cricket.p.rapidapi.com/photos/v1/index'
    headers = {'x-rapidapi-host': 'cricbuzz-cricket.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def photos_get_gallery(galleryId: Annotated[Union[int, float], Field(description='galleryId from photos/list service Default: 5374')]) -> dict: 
    '''Get photo gallery'''
    url = 'https://cricbuzz-cricket.p.rapidapi.com/photos/v1/detail/5374'
    headers = {'x-rapidapi-host': 'cricbuzz-cricket.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'galleryId': galleryId,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_image(p: Annotated[Union[str, None], Field(description='Specify size of image. One of the following : de|det|gthumb|thumb')] = None,
              d: Annotated[Union[str, None], Field(description='high|low')] = None) -> dict: 
    '''This endpoint is used to get image by id'''
    url = 'https://cricbuzz-cricket.p.rapidapi.com/img/v1/i1/c231889/i.jpg'
    headers = {'x-rapidapi-host': 'cricbuzz-cricket.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'p': p,
        'd': d,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def stats_get_icc_rankings(formatType: Annotated[str, Field(description='One of the followings : test|odi|t20 (if isWomen parameter is 1, there will be no odi)')],
                           isWomen: Annotated[Union[str, None], Field(description='Set to 1 to get rankings for women')] = None) -> dict: 
    '''Get ICC rankings'''
    url = 'https://cricbuzz-cricket.p.rapidapi.com/stats/v1/rankings/batsmen'
    headers = {'x-rapidapi-host': 'cricbuzz-cricket.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'formatType': formatType,
        'isWomen': isWomen,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def stats_get_icc_standings(seasonId: Annotated[Union[int, float, None], Field(description='The value of seasonStandings/id field returned right in this endpoint Default: 0')] = None) -> dict: 
    '''Get ICC standings'''
    url = 'https://cricbuzz-cricket.p.rapidapi.com/stats/v1/iccstanding/team/matchtype/1'
    headers = {'x-rapidapi-host': 'cricbuzz-cricket.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'seasonId': seasonId,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def stats_get_record_filters() -> dict: 
    '''Get record filters'''
    url = 'https://cricbuzz-cricket.p.rapidapi.com/stats/v1/topstats'
    headers = {'x-rapidapi-host': 'cricbuzz-cricket.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def stats_get_records(statsType: Annotated[str, Field(description="The value of 'value' field returned in …/stats/get-record-filters endpoint")],
                      year: Annotated[Union[int, float, None], Field(description='Specify year to get records. Ex : 2021 Default: 0')] = None,
                      matchType: Annotated[Union[int, float, None], Field(description='The value of matchTypeId field returned right in this endpoint Default: 0')] = None,
                      team: Annotated[Union[int, float, None], Field(description='The value of teamId field returned right in this endpoint Default: 0')] = None,
                      opponent: Annotated[Union[int, float, None], Field(description='The value of teamId field returned right in this endpoint Default: 0')] = None) -> dict: 
    '''Get records'''
    url = 'https://cricbuzz-cricket.p.rapidapi.com/stats/v1/topstats/0'
    headers = {'x-rapidapi-host': 'cricbuzz-cricket.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'statsType': statsType,
        'year': year,
        'matchType': matchType,
        'team': team,
        'opponent': opponent,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
