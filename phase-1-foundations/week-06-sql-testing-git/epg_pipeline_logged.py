import logging
import pandas as pd
import json
import os

# Setup logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('epg_pipeline.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Load data
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(BASE_DIR, '..', 'week-04-pandas-analysis', 'epg_schedule_20260311_041046.json')

logger.info("Pipeline started")

with open(filepath, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data['valid'])

logger.info(f"Data loaded - {len(df)} shows")

# Check each show
for _, row in df.iterrows():
    if pd.isna(row['network']):
        logger.warning(f"Missing network - show: {row['show_name']}")
    if pd.isna(row['episode_id']):
        logger.error(f"Missing episode_id - show: {row['show_name']}")

logger.info("Pipeline complete")