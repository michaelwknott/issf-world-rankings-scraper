import csv
from datetime import datetime

from db import Base, Rankings, Session, engine


def main():
    """Main entry point for the data importer script."""
    Base.metadata.create_all(bind=engine)

    with Session() as session:
        with session.begin():
            with open("src/data/issf_world_rankings.csv") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    row["rank"] = int(row["rank"])
                    row["rating"] = int(row["rating"])
                    row["year_of_birth"] = int(row["year_of_birth"])
                    row["date"] = datetime.strptime(row["date"], "%Y-%m-%d").date()
                    row["version_date"] = datetime.strptime(
                        row["version_date"], "%Y-%m-%d"
                    ).date()
                    session.add(Rankings(**row))


if __name__ == "__main__":
    main()
