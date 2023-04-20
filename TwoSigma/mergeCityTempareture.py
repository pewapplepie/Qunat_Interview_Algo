'''We have a collection of temperature and humidity readings from multiple cities. We want to combine these records together by joining each temperature reading to the most recent humidity reading in the same city, as of the time of the temperature reading. Both data series are represented as (time, city, reading) triples and are known to be sorted by time.
you can provide sample data like this:
temperature_readings = [
(2, 'NYC', 68),
(6, 'SFO', 73),
(11, 'NYC', 65),
(13, 'SFO', 75),
]
humidity_readings = [
 (1, 'NYC', 57),
 (5, 'SFO', 45),
 (9, 'SFO', 46),
 (10, 'NYC', 59),
 (12, 'SFO', 50),
]
'''