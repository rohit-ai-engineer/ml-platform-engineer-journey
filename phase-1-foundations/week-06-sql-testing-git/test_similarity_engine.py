import pandas as pd
import json
import pytest
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'week-05-numpy')) 
from mini_project_content_similarity_engine import find_similar_show,features_normalized #type: ignore

@pytest.fixture

def epg_data():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(BASE_DIR,'..', 'week-04-pandas-analysis', 'epg_schedule_20260311_041046.json')

    with open (filepath,'r') as f:
        data = json.load(f)
    return pd.DataFrame(data['valid'])

def test_returns_three_results(epg_data):
    result = find_similar_show('Way Too Early', epg_data, features_normalized)
    assert len(result) == 3

def test_show_not_found(epg_data):
    result = find_similar_show('NonExistentShow', epg_data, features_normalized)
    assert "not found" in result 

def test_scores_valid_range(epg_data):
    result = find_similar_show('Way Too Early', epg_data, features_normalized)
    for x in result:
        assert -1 <= x[1] <= 1