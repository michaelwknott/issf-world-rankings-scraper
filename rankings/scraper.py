import logging
import re
from datetime import datetime, date

from bs4 import BeautifulSoup
import requests


EVENT_CODES = [
    "ARM",
    "R3PM",
    "ARW",
    "R3PW",
    "APM",
    "RFPM",
    "APW",
    "SPW",
    "TRM",
    "SKM",
    "TRW",
    "SKW",
]


def get_issf_ranking_html(event):
    """Get and return html content of ISSF world rankings page for a given event.

    Args:
        event (str): ISSF event code.

    Returns:
        tuple: Tuple containing event code and BeautifulSoup object containing html
            content.
    """
    logging.info(f"Requesting html for event: {event}")
    headers = {
        "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
        "origin": "https://www.issf-sports.org",
        "referer": "https://www.issf-sports.org/",
        "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N)"
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36",
    }
    url = (
        f"https://www.issf-sports.org"
        f"/competitions/worldranking/complete_ranking_by_event_yearly.ashx"
        f"?evlinkid={event}"
    )

    try:
        response = requests.get(url, headers=headers)
    except requests.exceptions.RequestException as e:
        logging.error(f"Request response error: {e}")
        raise SystemExit(e)

    logging.info(f"Request response status code: {response.status_code}")

    return event, BeautifulSoup(response.content, "html.parser")


def parse_issf_ranking_html(event_name, response_object):
    """Parse html content of ISSF world rankings page for a given event.

    Args:
        event_name (str): ISSF event name.
        response_object (BeautifulSoup): BeautifulSoup object containing html content.

    Returns:
        list: List of dictionaries containing parsed rankings data.
    """
    logging.info(f"Parsing html for event: {event_name}")
    soup = response_object

    version_text = soup.select_one(".versiontext").text
    if version_text is None:
        logging.error("Parsing error: the version_text css selector is None")
        raise SystemExit(
            "Exiting scraper due to the version_text css selector returning None"
        )
    version_date_string = re.sub("[^0-9]", "", version_text)
    version_date = datetime.strptime(version_date_string, "%d%m%Y").date()

    html_tables = soup.find_all("table")
    if html_tables == []:
        logging.error("Parsing error: table tags not found in html")
        raise SystemExit("Exiting scraper as table tags were not found in html")
    html_rankings_table = html_tables[0]
    html_rankings_rows = html_rankings_table.find_all("tr")

    parsed_rankings = []

    for row in html_rankings_rows[1:]:  # skip header row
        data = (td.get_text(strip=True) for td in row.find_all("td"))
        (
            rank,
            rating,
            name,
            _,
            nation,
            year_of_birth,
        ) = data  # assign empty string, created from national flag image, to _
        individual_rank = {
            "event": event_name,
            "rank": rank,
            "rating": rating,
            "name": name,
            "nation": nation,
            "year_of_birth": year_of_birth,
            "date": date.today(),
            "version_date": version_date,
        }
        parsed_rankings.append(individual_rank)

    return parsed_rankings


if __name__ == "__main__":
    for event_code in ["ARM"]:
        event, soup = get_issf_ranking_html(event_code)
        rankings = parse_issf_ranking_html(event, soup)
