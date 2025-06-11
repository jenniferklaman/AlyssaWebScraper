from scraper.web_scraper import setup_driver, login_to_portal, navigate_to_renewals, scrape_renewal_table
from data_cleaning import parse_fields
from storage.storage import save_to_json
from alerts.alerts import check_for_alerts

def run_scraper_pipeline():
    driver = setup_driver()
    login_to_portal(driver)
    navigate_to_renewals(driver)
    raw_data = scrape_renewal_table(driver)
    cleaned_data = parse_fields(raw_data)
    save_to_json(cleaned_data, path="data/renewal_data.json")
    check_for_alerts(cleaned_data)
    driver.quit()

if __name__ == "__main__":
    run_scraper_pipeline()
