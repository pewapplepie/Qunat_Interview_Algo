import csv
import glob

# Fill this in based on your own knowledge, or, based on the output of 'analyze_stats.py'
NUM_ROWS = 1_000_000

sensor_filenames = sorted(glob.glob('./txtfiles/sensor*.csv'))

# Sort: trim leading 6 chars, 'sensor', and trailing 4 chars, '.csv', leaving just the number in the middle
sensor_filenames = sorted(sensor_filenames, key=lambda x: int(x[6:-4]))
#
# Get handles to all files, and create input CSV readers
sensor_readers = []
for sensor_fname in sensor_filenames:
    f = open(sensor_fname, newline='')
    sensor_readers.append(csv.reader(f))

print(sensor_readers)
#
# Create output CSV writer
f = open('merged_sensors.csv', 'w', newline='')
writer = csv.writer(f)

# Discard all sensor headers
for reader in sensor_readers:
    next(reader)

# Build up output header and write
output_header = ['timestamp']
for sensor_fname in sensor_filenames:
    print('writing')
    sensor_name = sensor_fname[:-4]  # trim off '.csv'
    output_header.append(sensor_name)
writer.writerow(output_header)

row_count = 0
while row_count < NUM_ROWS:
    row_count += 1
    values = []
    timestamps = []
    for reader in sensor_readers:
        row = next(reader)

        ts, val = row
        timestamps.append(int(ts))
        values.append(val)

    if row_count % 1000 == 0:
        print(f'Merged {row_count} rows')

    avg_ts = int(sum(timestamps) / len(timestamps))
    writer.writerow([avg_ts] + values)
    if row_count == 50:
        break