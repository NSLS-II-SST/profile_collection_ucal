import nslsii
import ucal_common as ucal
from ucal_common.startup import *
from bluesky.callbacks import LiveTable
nslsii.configure_base(get_ipython().user_ns, "ucal")

loadfile = beamline_config.get('loadfile', None)
if loadfile is not None:
    if beamline_config.get('bar', '') == 'Standard 4-sided bar':
        load_standard_four_sided_bar(loadfile)
        sampleholder.print_samples()
# sd SupplementalData preprocessor is automatically loaded and
# subscribed to RunEngine by nslsii.configure_base
sd.baseline.append(eslit)

# Fix LiveTable display
LiveTable._FMT_MAP['number'] = 'g'
