import json

from requests import Response

import const
import requests
from backend.schedule import ScheduleDTO, ScheduleDTOBuilder

"""
: raise requests.HTTPError: if the HTTP request returned an unsuccessful status code
: raise requests.RequestException: if the request failed for any reason
"""


def fetch_schedule_from_interpark(start_date: str) -> Response:
    url = const.REQUEST_URL + start_date

    api_response = requests.get(
        url,
        headers={
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/124.0.0.0 Safari/537.36'
        }
    )
    api_response.raise_for_status()

    return api_response


"""
: raise IOError: if an I/O operation fails (e.g. file not exists)
"""


def write_schedule_in_json(schedules: list[ScheduleDTO]) -> None:
    json_data = {
        const.FIELD_CASTINGS: []
    }

    for schedule in schedules:
        json_data[const.FIELD_CASTINGS].append(schedule.to_dict())

    with open(const.SCHEDULE_JSON_FILE, 'w') as file:
        json.dump(json_data, file, ensure_ascii=False, indent=4)


"""
: raise KeyError: if the key is not found in the dictionary
: raise JsonDecodeError: if the JSON data is not valid
"""


def parse_schedule(api_response: Response) -> list[ScheduleDTO]:
    raw_data = api_response.json()
    raw_schedules = raw_data['data']['dataList']
    schedules = []

    for raw_schedule in raw_schedules:
        schedules.append(ScheduleDTOBuilder.build(raw_schedule))

    return schedules
