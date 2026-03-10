import requests
from datetime import datetime

# TVmaze API - get today's schedule for a country
def fetch_schedule(country_code="US", date=None):
    """
    Fetch TV schedule from TVmaze API
    
    Args:
        country_code: Country code (US, GB, etc.)
        date: Date in YYYY-MM-DD format (defaults to today)
    
    Returns:
        List of scheduled shows
    """
    if date is None:
        date = datetime.now().strftime("%Y-%m-%d")
    
    url = f"https://api.tvmaze.com/schedule?country={country_code}&date={date}"
    
    print(f"Fetching schedule for {country_code} on {date}...")
    
    response = requests.get(url)
    
    if response.status_code == 200:
        schedule = response.json()
        print(f"✅ Fetched {len(schedule)} shows")
        return schedule
    else:
        print(f"❌ Error: {response.status_code}")
        return []
    
def extract_show_info(raw_show):
    """
    Extract key fields from raw API response
    
    Returns a clean dict with only the fields we care about
    """
    try:
        show_data = raw_show.get('show') or {}

        return {
            'episode_id': raw_show.get('id'),
            'episode_name': raw_show.get('name'),
            'show_name': show_data.get('name'),
            'network': (show_data.get('network') or {}).get('name'),
            'airdate': raw_show.get('airdate'),
            'airtime': raw_show.get('airtime'),
            'runtime': raw_show.get('runtime'),
            'type': show_data.get('type'),
            'genres': show_data.get('genres', []),
            'status': show_data.get('status')
        }
    except Exception as e:
        print(f"⚠️  Error extracting show info: {e}")
        return None
def validate_show(show):
    """
    Validate that required fields exist and are valid
    
    Returns: (is_valid, list_of_issues)
    """
    issues = []
    
    # Check required fields
    required_fields = ['episode_id', 'show_name', 'airdate', 'airtime']
    
    for field in required_fields:
        if not show.get(field):
            issues.append(f"Missing required field: {field}")
    
    # Check runtime is reasonable
    runtime = show.get('runtime')
    if runtime:
        if runtime < 0:
            issues.append(f"Invalid runtime: {runtime} (negative)")
        elif runtime > 300:
            issues.append(f"Suspicious runtime: {runtime} minutes (>5 hours)")
    
    # Check airdate format (should be YYYY-MM-DD)
    airdate = show.get('airdate')
    if airdate:
        try:
            datetime.strptime(airdate, "%Y-%m-%d")
        except ValueError:
            issues.append(f"Invalid airdate format: {airdate}")
    
    is_valid = len(issues) == 0
    return is_valid, issues

def process_schedule(raw_schedule):
    """
    Process entire schedule - extract, validate, categorize
    
    Returns: dict with valid shows, invalid shows, and stats
    """
    valid_shows = []
    invalid_shows = []
    
    for raw_show in raw_schedule:
        # Extract clean data
        show = extract_show_info(raw_show)
        
        if show is None:
            continue
        
        # Validate
        is_valid, issues = validate_show(show)
        
        if is_valid:
            valid_shows.append(show)
        else:
            show['validation_issues'] = issues
            invalid_shows.append(show)
    
    return {
        'valid': valid_shows,
        'invalid': invalid_shows,
        'total_processed': len(raw_schedule),
        'valid_count': len(valid_shows),
        'invalid_count': len(invalid_shows)
    }

import json
from datetime import datetime

def save_to_json(result, filename=None):
    """Save processed schedule to JSON file"""
    if filename is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"epg_schedule_{timestamp}.json"
    
    with open(filename, 'w') as f:
        json.dump(result, f, indent=2)
    
    print(f"\n💾 Saved to {filename}")
    return filename

# # Test it
# schedule = fetch_schedule("INVALID_COUNTRY")

# # Print first show to see the data structure
# if schedule:
#     print("\n--- Sample Show ---")
#     print(schedule[0])

# Test extraction
# raw_schedule = fetch_schedule("US")

# if raw_schedule:
#     # Test on first show
#     raw_first_show = raw_schedule[0]
#     clean_show = extract_show_info(raw_first_show)
    
#     print("\n--- Raw vs Clean ---")
#     print(f"Raw show has {len(raw_first_show)} fields (messy!)")
#     print(f"Clean show has {len(clean_show)} fields (just what we need)")
#     print("\nClean show:")
#     print(clean_show)


# Test validation
# raw_schedule = fetch_schedule("US")

# if raw_schedule:
#     # Test on first 5 shows
#     for i in range(5):
#         raw_show = raw_schedule[i]
#         clean_show = extract_show_info(raw_show)
        
#         if clean_show:
#             is_valid, issues = validate_show(clean_show)
            
#             if is_valid:
#                 print(f"✅ Show {i+1}: {clean_show['show_name']} - VALID")
#             else:
#                 print(f"❌ Show {i+1}: {clean_show.get('show_name', 'Unknown')} - INVALID")
#                 for issue in issues:
#                     print(f"   - {issue}")

# Test validation with intentionally bad data
# print("\n--- Testing Validation with Bad Data ---")

# bad_shows = [
#     {
#         'episode_id': None,  # Missing required field
#         'show_name': 'Test Show',
#         'airdate': '2026-03-11',
#         'airtime': '20:00'
#     },
#     {
#         'episode_id': 123,
#         'show_name': 'Test Show 2',
#         'airdate': '2026-13-99',  # Invalid date
#         'airtime': '20:00'
#     },
#     {
#         'episode_id': 456,
#         'show_name': 'Test Show 3',
#         'airdate': '2026-03-11',
#         'airtime': '20:00',
#         'runtime': -10  # Negative runtime
#     },
#     {
#         'episode_id': 789,
#         'show_name': 'Marathon Show',
#         'airdate': '2026-03-11',
#         'airtime': '20:00',
#         'runtime': 500  # Suspiciously long
#     }
# ]

# for i, show in enumerate(bad_shows, 1):
#     is_valid, issues = validate_show(show)
    
#     if is_valid:
#         print(f"✅ Bad Show {i}: VALID (shouldn't happen!)")
#     else:
#         print(f"❌ Bad Show {i}: INVALID (as expected)")
#         for issue in issues:
#             print(f"   - {issue}")


# === FULL PIPELINE TEST ===

print("="*50)
print("EPG DATA PIPELINE - FULL RUN")
print("="*50)

# Step 1: Fetch
raw_schedule = fetch_schedule("US")

if not raw_schedule:
    print("Failed to fetch schedule")
    exit()

# Step 2: Process
result = process_schedule(raw_schedule)

# Step 3: Display Results
print(f"\n📊 Processing Results:")
print(f"Total shows: {result['total_processed']}")
print(f"Valid: {result['valid_count']} ({result['valid_count']/result['total_processed']*100:.1f}%)")
print(f"Invalid: {result['invalid_count']} ({result['invalid_count']/result['total_processed']*100:.1f}%)")

# Show sample valid shows
if result['valid']:
    print(f"\n✅ Sample Valid Shows (first 3):")
    for show in result['valid'][:3]:
        print(f"  - {show['show_name']} on {show['network']} at {show['airtime']}")

# Show invalid shows if any
if result['invalid']:
    print(f"\n❌ Invalid Shows Found ({len(result['invalid'])}):")
    for show in result['invalid']:
        print(f"  - {show.get('show_name', 'Unknown')}")
        for issue in show['validation_issues']:
            print(f"      • {issue}")

save_to_json(result)