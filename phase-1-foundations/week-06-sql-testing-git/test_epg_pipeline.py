import pandas as pd
import json
import os
import pytest
import sys

# Load the data once - used by all tests
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(BASE_DIR,'..', 'week-04-pandas-analysis', 'epg_schedule_20260311_041046.json')

with open (filepath,'r') as f:
    data = json.load(f)

df = pd.DataFrame(data['valid'])

# Test 1 - no null episode_ids
def test_no_null_episode_ids():
    assert df['episode_id'].isna().sum() == 0

# Test 2 - no duplicate episode_ids
def test_no_duplicate_episode_ids():
    assert df['episode_id'].duplicated().sum() == 0

# Test 3 - no null or empty show names
def test_no_null_show_names():
    assert df['show_name'].isna().sum() == 0

# Test 4 - all shows have runtime > 0
def test_runtime_positive():
    assert df['runtime'].min() > 0

# Test 5 - all shows have a valid airtime format (HH:MM)
def test_shows_validity():
    assert df['airtime'].str.match(r'^\d{2}:\d{2}$').all()

# Test 6 - All shows have a recognised type (not an unknown category)
def test_type_validation():
    valid_types = ['News', 'Scripted', 'Reality', 'Talk Show', 'Documentary', 'Game Show', 'Sports', 'Panel Show']
    assert df['type'].isin(valid_types).all()

# Test 7 - Total show count is exactly 115
def test_total_show():
    assert len(df) == 115