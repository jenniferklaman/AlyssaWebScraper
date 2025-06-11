import csv
import json

def save_to_csv(cleaned_data_list, path):
# Write rows to a CSV file with clear headers 
    if not cleaned_data_list:
        return
    keys = cleaned_data_list[0].keys()
    with open(path, "w", newline='', encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(cleaned_data_list)

def save_to_json(cleaned_data_list, path):
 # Dump data to a readable JSON format
    with open(path, "w", encoding="utf-8") as f:
        json.dump(cleaned_data_list, f, indent=2)


# def save_to_sql(cleaned_data_list, db_path): OPTIONAL
#     # Use sqlite3 to insert/update rows in a renewals table