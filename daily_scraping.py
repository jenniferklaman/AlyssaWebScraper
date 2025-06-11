def schedule_tasks():
    schedule.every().day.at("08:00").do(run_scraper_and_update_dashboard)
    while True:
        schedule.run_pending()
        time.sleep(60)

def run_scraper_and_update_dashboard():
    driver = setup_driver()
    login_to_portal(driver)
    navigate_to_renewals(driver)
    raw_data = scrape_renewal_table(driver)
    cleaned_data = parse_fields(raw_data)
    save_to_json(cleaned_data)
    check_for_alerts(cleaned_data)
    driver.quit()
