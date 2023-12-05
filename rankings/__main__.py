import logging
import time

from scraper import get_issf_ranking_html, parse_issf_ranking_html, EVENT_CODES
from db import Base, Rankings, Session, engine


logging.basicConfig(
    filename="scraper.log",
    level=logging.INFO,
    format="%(asctime)s: %(name)s - %(levelname)s - %(message)s "
    "(Filename: %(filename)s  Line: %(lineno)d  Function: %(funcName)s)",
    datefmt="%m/%d/%Y %I:%M:%S %p",
)


def main():
    """Main entry point for the scraper."""
    logging.info("Starting ISSF World Rankings scraper")
    Base.metadata.create_all(bind=engine)

    for event_code in EVENT_CODES:
        logging.info(f"Getting world rankings for event code: {event_code}")
        event, soup = get_issf_ranking_html(event_code)
        rankings = parse_issf_ranking_html(event, soup)

        with Session() as session:
            with session.begin():
                for ranking in rankings:
                    session.add(Rankings(**ranking))
                    logging.info(f"Added world rankings for {event_code} to database")
        time.sleep(0.5)
    logging.info("ISSF World Rankings scraper finished")


if __name__ == "__main__":
    main()
