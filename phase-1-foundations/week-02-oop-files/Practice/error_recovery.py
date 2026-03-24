import json
import os
import pandas as pd
import logging

# Setup logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('epg_pipeline_log.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(BASE_DIR, '..', '..','week-04-pandas-analysis','epg_schedule_20260311_041046.json')

with open (filepath,'r') as f:
    data = json.load(f)


df = pd.DataFrame(data['valid'])

passed = 0
failed = 0

for _, row in df.iterrows():
    if pd.isna(row['episode_id']):
        logger.warning(f"Missing Episode ID - show: {row['show_name']}")
        failed += 1
    else:
        passed += 1

logger.info(f"Pipeline complete - {passed} shows passed, {failed} shows skipped")

