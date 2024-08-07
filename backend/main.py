
from backend.bundle_builder import combine_bundle_js
from backend.schedule_fetcher import *
from backend.utils import get_kst_today


# build schedule json file
today = get_kst_today()
interpark_schedules = fetch_schedule_from_interpark(today)
write_schedule_in_json(interpark_schedules)

# build bundle.js file
combine_bundle_js()

