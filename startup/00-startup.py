import sys
from pathlib import Path

paths = [
    path
    for path in Path(
        "/nsls2/data/sst/ucal/shared/config/bluesky/collection_packages"
    ).glob("*")
    if path.is_dir()
]
for path in paths:
    sys.path.append(str(path))

import nslsii
import ucal
from ucal.startup import *
from ucal.plans.alignment import load_saved_manipulator_calibration
from bluesky.callbacks import LiveTable

nslsii.configure_base(get_ipython().user_ns, "ucal", publish_documents_with_kafka=True)

loadfile = beamline_config.get("loadfile", None)
if loadfile is not None and loadfile != "":
    if beamline_config.get("bar", "") == "Standard 4-sided bar":
        load_standard_four_sided_bar(loadfile)
        sampleholder.print_samples()

print("Loading last saved manipulator calibration")
RE(load_saved_manipulator_calibration())

# sd SupplementalData preprocessor is automatically loaded and
# subscribed to RunEngine by nslsii.configure_base
#sd.baseline.append(eslit)

# Fix LiveTable display
#LiveTable._FMT_MAP["number"] = "g"
