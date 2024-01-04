# issf-world-rankings-scraper
This project is a Python application that scrapes the ISSF World Rankings data.

## About the Project
This project, `issf-world-rankings-scraper`, is a Python application designed to scrape the International Shooting Sport Federation (ISSF) World Rankings data. The data is collected from the official [ISSF website](https://www.issf-sports.org/competitions/worldranking/complete_ranking_by_event_yearly.ashx) and stored in a PostgreSQL database for further analysis and usage.

The application is built with Python using libraries such as Requests for handling HTTP requests, BeautifulSoup for parsing HTML, SQLAlchemy for managing database interactions, and Psycopg2 as the PostgreSQL database adapter. The application is containerized using Docker for easy setup and distribution. GitHub Actions is used to automate deployment.

The goal of this project is to make ISSF World Rankings data more accessible and usable for data analysis, thereby providing valuable insights into an athletes performance progression.

## Running the Application Locally

### Prerequisites
* [Docker](https://www.docker.com/)
* [Docker Compose](https://docs.docker.com/compose/)
* [Python](https://www.python.org/)

### Notes
* The web scraper is designed to run on a remote server with a PostgreSQL database. To run the application locally using Docker-Compose, you will need to create a `.env` file in the root directory of the project and add the following environment variables:
  * `DB_URL=postgresql://<username>:<password>@<host>:<port>/<database>`
  * `POSTGRES_PASSWORD=<password>`
* The web scraper is configured to run on a schedule using Cron. The schedule is set to run every Sunday at 17:21 UTC. To update the schedule, edit the cron schedule (`17 21 * * 7`) in the `entrypoint.sh` file: 
  * `echo "17 21 * * 7 export DB_URL=$DB_URL_VALUE; cd /issf_world_rankings/rankings && /usr/local/bin/python __main__.py >> /issf_world_rankings/rankings/cronlogfile.log 2>&1" | crontab -`
  * For more information on how to configure the cron schedule, see [Crontab Guru](https://crontab.guru/)

### Installation to Local Machine
1. Clone the repository
   ```sh
   git clone git@github.com:michaelwknott/issf-world-rankings-scraper.git
   ```
1. Create a virtual environment
   ```sh
   python -m venv .venv --prompt .
   ```
1. Activate the virtual environment
   ```sh
   source .venv/bin/activate
   ```
1. Install the dependencies
   ```sh
   python -m pip install -r requirements.txt
   ```
1. Ensure `.env` file is created in the root directory of the project (see Notes above)
1. Run the application
   ```sh
   docker-compose up -d
   ```
1. Using `docker-compose up -d` will run the web scraper on the schedule set in the `entrypoint.sh` file. To run the web scraper manually, run the following command:
   ```sh
   docker-compose exec issf-world-rankings python rankings/__main__.py
   ```
1. Check the logs to ensure the scraper has run successfully. Update the date and time in the command below to match the date and time of the log file you want to view.
   ```sh
   docker-compose exec issf-world-rankings bash -c "cat logs/scraper_yyyy-mm-dd_hh-mm-ss.log"
   ```
1. To access the PostgreSQL database, use the following command:
   ```sh
   docker-compose exec issf-dev-postgres psql -U postgres -d postgres
   ```
1. SQL queries can be run against the database using the PostgreSQL command line interface. For example, to view the number of rows in the `rankings` table, use the following command:
   ```sh
   SELECT COUNT(*) FROM rankings;
   ```
1. To stop the application, use the following command:
   ```sh
   docker-compose down
   ```

### Useful Docker Commands
1. To view the Docker images, use the following command:
   ```sh
   docker-compose images
   ```
1. To view the Docker containers currently running, use the following command:
   ```sh
   docker-compose ps
   ```
1. If you need to access the web scraper in the Docker container, run the following command:
   ```sh
   docker-compose exec issf-world-rankings bash
   ```
