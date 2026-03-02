# Metadata Validator - Week 1 Project
# Checks streaming metadata for quality issues

import csv

print ("=== Metadata Validator ===")
print ()

# Open and read the CSV file
filename = "sample_metadata.csv"

with open(filename, 'r') as file:
    reader = csv.DictReader(file)

    print(f"validating {filename}...")
    print()

    row_num = 1
    issues_found = 0

    for row in reader:
        row_num += 1  # Start from 2 (row 1 is headers)

        # Check for missing title
        if not row['title'] or row['title'].strip() == '':
            print(f"❌ Row {row_num}: Missing title")
            issues_found += 1

        # Check for missing genre
        if not row['genre'] or row['genre'].strip() == '':
            print(f"⚠️  Row {row_num}: Missing genre for '{row['title']}'")
            issues_found += 1

        # Check for missing or invalid duration
        try:
            duration = int(row['duration'])
            if duration <= 0:
                print(f"❌ Row {row_num}: Invalid duration ({duration}) for '{row['title']}'")
                issues_found += 1
        except ValueError:
            print(f"❌ Row {row_num}: Missing or invalid duration for '{row['title']}'")
            issues_found += 1

        # Check for missing release year
        if not row['release_year'] or row['release_year'].strip() == '':
            print(f"⚠️  Row {row_num}: Missing release year for '{row['title']}'")
            issues_found += 1


print()
print("--- Validation Complete ---")
print(f"Total issues found: {issues_found}")

if issues_found == 0:
    print("✅ All metadata looks good!")
else:
    print(f"🔍 Please fix {issues_found} issue(s)")

