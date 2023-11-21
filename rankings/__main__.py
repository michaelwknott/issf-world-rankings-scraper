import time

from scraper import get_issf_ranking_html, parse_issf_ranking_html, EVENT_CODES
from db import Base, Rankings, Session, engine


def main():
    """Main entry point for the scraper."""
    Base.metadata.create_all(bind=engine)

    for event_code in EVENT_CODES:
        event, soup = get_issf_ranking_html(event_code)
        rankings = parse_issf_ranking_html(event, soup)

        with Session() as session:
            with session.begin():
                for ranking in rankings:
                    session.add(Rankings(**ranking))
        time.sleep(0.5)


if __name__ == "__main__":
    main()
