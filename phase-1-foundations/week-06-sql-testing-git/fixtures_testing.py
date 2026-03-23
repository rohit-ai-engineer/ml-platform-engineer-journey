import pandas as pd
import json
import os
import pytest
import sys

@pytest.fixture

def epg_data():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(BASE_DIR,'..', 'week-04-pandas-analysis', 'epg_schedule_20260311_041046.json')

    with open (filepath,'r') as f:
        data = json.load(f)
    return pd.DataFrame(data['valid'])

# Test 1 - no null episode_ids
def test_no_null_episode_ids(epg_data):
    assert epg_data['episode_id'].isna().sum() == 0

# Test 2 - no duplicate episode_ids
def test_no_duplicate_episode_ids(epg_data):
    assert epg_data['episode_id'].duplicated().sum() == 0

# Test 3 - no null or empty show names
def test_no_null_show_names(epg_data):
    assert epg_data['show_name'].isna().sum() == 0

# Test 4 - all shows have runtime > 0
def test_runtime_positive(epg_data):
    assert epg_data['runtime'].min() > 0

# Test 5 - all shows have a valid airtime format (HH:MM)
def test_shows_validity(epg_data):
    assert epg_data['airtime'].str.match(r'^\d{2}:\d{2}$').all()

# Test 6 - All shows have a recognised type (not an unknown category)
def test_type_validation(epg_data):
    valid_types = ['News', 'Scripted', 'Reality', 'Talk Show', 'Documentary', 'Game Show', 'Sports', 'Panel Show']
    assert epg_data['type'].isin(valid_types).all()

# Test 7 - Total show count is exactly 115
def test_total_show(epg_data):
    assert len(epg_data) == 115