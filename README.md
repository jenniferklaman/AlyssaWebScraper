# AlyssaWebScraperXD:
### For Alyssa and work friends to automate something i dont fucking know.

## Notes Google Doc: 
https://docs.google.com/document/d/11K5CPvWPZ-761XSf8xqpagfHusrX0d1JNm1lz2NGISQ/edit?usp=sharing

## Stack:
| Layer                   | Tool                                  | Purpose                                                                                   |
| ----------------------- | ------------------------------------- | ----------------------------------------------------------------------------------------- |
| **Web Scraping**        | **Selenium (Python)**                 | Automate browser actions and scrape renewal data from internal or external websites       |
| **Data Processing**     | **Pandas** / built-in `csv`, `json`   | Clean, transform, and store scraped data in CSV or JSON format                            |
| **Database (optional)** | `SQLite3` / `JSON`                    | Store renewal records for easy querying and persistent access                             |
| **Alerts**              | `schedule`, `smtplib`                 | Automatically send reminders or alerts when deadlines approach                            |
| **UI Layer**            | **Streamlit**                         | Render an interactive dashboard for underwriters and managers to track metrics and trends |
| **Deployment**          | **Streamlit Cloud** or PythonAnywhere | Host the dashboard for internal users to access securely                                  |
| **Documentation**       | `README.md`, `docs/user_guide.md`     | Help non-technical users understand how to use the tool and customize it                  |

## Logic Flow (Preliminary): 
Script starts → initializes directories and Selenium browser

Navigates to portal → logs in if needed, selects filters (e.g., report date)

Scrapes data → extracts rows from the renewals table

Parses fields → ensures correct format (dates, names, status)

Saves data → to JSON or CSV file (or database)

Checks for deadlines → sends alerts if any quotes are due soon

UI loads data → displays filtered info by employee, broker, state, etc.

Managers use dashboard → for projections and downloadable summaries

Users interact → apply filters, add comments, etc.

Process repeats daily or on user demand

# Set Up and How to Run Stuff:
---

## VENV SETUP & RUNNING INSTRUCTIONS

- Make sure Python 3.9+ is installed: https://www.python.org/downloads/
- Check version: `python --version` or `python3 --version`

### Set up your virtual environment:

1. Create the environment:
   ```bash
   python -m venv venv
   ```
2. Activate it:
   - On **Windows**:
     ```bash
     venv\Scripts\activate
     ```
   - On **Mac/Linux**:
     ```bash
     source venv/bin/activate
     ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Run the components:

- Run the scraper:
  ```bash
  python run.py
  ```

- Run the Streamlit dashboard:
  ```bash
  streamlit run ui/streamlit_app.py
  ```

4. When done, deactivate:
   ```bash
   deactivate
   ```

---

# Documentation for Devs to Look at
## Selenium with Python: 
https://www.selenium.dev/documentation/

## Selectors Reference (CSS/XPath):
https://www.w3schools.com/cssref/css_selectors.asp
https://www.w3schools.com/xml/xpath_syntax.asp

## Data Parsing, Cleaning, and Storage:
Pandas (for CSV/JSON processing):
https://pandas.pydata.org/docs/

Python json module (standard lib):
https://docs.python.org/3/library/json.html

Python csv module (standard lib):
https://docs.python.org/3/library/csv.html

SQLite (optional SQL storage):
https://docs.python.org/3/library/sqlite3.html

## UI Docs:
### Streamlit (recommended):

Streamlit Docs:
https://docs.streamlit.io/

Streamlit Gallery (UI inspiration):
https://streamlit.io/gallery

Streamlit Cloud Deployment:
https://docs.streamlit.io/streamlit-cloud/get-started

## Alerting Logic:
schedule module (Python job scheduler):
https://schedule.readthedocs.io/en/stable/

Email with smtplib:
https://realpython.com/python-send-email/

## Project Management & Docs: 
Markdown Reference (for docs):
https://www.markdownguide.org/basic-syntax/

Swagger (for API if you want to build one):
https://swagger.io/tools/swagger-ui/

