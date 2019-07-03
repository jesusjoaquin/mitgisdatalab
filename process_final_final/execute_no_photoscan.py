# Obtain the yaw, pitch, and roll => output csv
exec(open('./ypr_extraction.py').read())

# Obtain lat, long, and flying height => output csv
exec(open('./llh_extraction.py').read())

# Combine the above two datasets
exec(open('./merge_data.py').read())

# Find the footprints
exec(open('./get_footprint.py').read())

