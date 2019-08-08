import sqlite3,geocoder,math,csv,msvcrt,os.path
from geopy.distance import great_circle
print("LOADING DATABASE...\n")
con = sqlite3.connect(':memory:')
cur = con.cursor()\
      
#CREATE STOPS
cur.execute("CREATE TABLE stops(stop_id,stop_code,stop_name,stop_lat,stop_lon,zone_id,alias,stop_area,stop_desc,lest_x,lest_y,zone_name);")
with open(os.path.join(os.path.dirname(__file__),'stops.csv'), 'r') as fin:
	dr = csv.DictReader(fin)
	to_db = [(i['stop_id'],i['stop_code'],i['stop_name'],i['stop_lat'],i['stop_lon'],i['zone_id'],i['alias'],i['stop_area'],i['stop_desc'],i['lest_x'],i['lest_y'],i['zone_name']) for i in dr]
cur.executemany("INSERT INTO stops (stop_id,stop_code,stop_name,stop_lat,stop_lon,zone_id,alias,stop_area,stop_desc,lest_x,lest_y,zone_name) VALUES (?,?,?,?,?,?,?,?,?,?,?,?);", to_db)
con.commit()
#CREATE STOP_TIMES
cur.execute("CREATE TABLE stop_times(trip_id,arrival_time,departure_time,stop_id,stop_sequence,pickup_type,drop_off_type);")
with open(os.path.join(os.path.dirname(__file__),'stop_times.csv'), 'r') as fin:
	dr = csv.DictReader(fin)
	to_db = [(i['trip_id'],i['arrival_time'],i['departure_time'],i['stop_id'],i['stop_sequence'],i['pickup_type'],i['drop_off_type']) for i in dr]
cur.executemany("INSERT INTO stop_times(trip_id,arrival_time,departure_time,stop_id,stop_sequence,pickup_type,drop_off_type) VALUES (?,?,?,?,?,?,?);", to_db)
con.commit()
#CREATE TRIPS
cur.execute("CREATE TABLE trips(route_id,service_id,trip_id,trip_headsign,trip_long_name,direction_code,shape_id,wheelchair_accessible);")
with open(os.path.join(os.path.dirname(__file__),'trips.csv'), 'r') as fin:
	dr = csv.DictReader(fin)
	to_db = [(i['route_id'],i['service_id'],i['trip_id'],i['trip_headsign'],i['trip_long_name'],i['direction_code'],i['shape_id'],i['wheelchair_accessible']) for i in dr]
cur.executemany("INSERT INTO trips(route_id,service_id,trip_id,trip_headsign,trip_long_name,direction_code,shape_id,wheelchair_accessible) VALUES (?,?,?,?,?,?,?,?);", to_db)
con.commit()
#CREATE ROUTES
cur.execute("CREATE TABLE routes(route_id,agency_id,route_short_name,route_long_name,route_type,route_color,competent_authority);")
with open(os.path.join(os.path.dirname(__file__),'routes.csv'), 'r') as fin:
	dr = csv.DictReader(fin)
	to_db = [(i['route_id'],i['agency_id'],i['route_short_name'],i['route_long_name'],i['route_type'],i['route_color'],i['competent_authority']) for i in dr]
cur.executemany("INSERT INTO routes(route_id,agency_id,route_short_name,route_long_name,route_type,route_color,competent_authority) VALUES (?,?,?,?,?,?,?);", to_db)
con.commit()
print("LOOKING FOR YOUR LOCATION...\n")
g = geocoder.ip('me')
try:
	while True:
		with con:#SEARCH NEAR STOPS
			cur = con.cursor()    
			cur.execute("SELECT DISTINCT stops.stop_id,stops.stop_name,stops.stop_lat,stops.stop_lon FROM stops,stop_times,trips,routes WHERE stops.stop_id=stop_times.stop_id AND stop_times.trip_id=trips.trip_id AND trips.route_id=routes.route_id ORDER BY ((stops.stop_lat-?)*(stops.stop_lat-?)) + ((stops.stop_lon - ?)*(stops.stop_lon - ?)) ASC LIMIT 0 , 4;",(g.lat,g.lat,g.lng,g.lng))
			rows = cur.fetchall()
			for index,row in enumerate(rows):
				print (index,row[1],"\t"+str(int(great_circle((g.lat,g.lng), (row[2],row[3])).meters))+"m")
		select = input("\nValige peatus: ") #NUMBER
		peatus_id = rows[int(select)][0]#stop_id
		with con:#SEARCH TIME
			cur = con.cursor()    
			cur.execute("SELECT routes.route_short_name,stop_times.arrival_time FROM stops,stop_times,trips,routes WHERE stops.stop_id=stop_times.stop_id AND stop_times.trip_id=trips.trip_id AND trips.route_id=routes.route_id AND stops.stop_id=? ORDER BY routes.route_short_name,stop_times.arrival_time ASC;",[peatus_id])
			rows = cur.fetchall()
			for row in rows:
				print("Liin",row[0],"Algus:\t",row[1])
		input("\nENTER - Tagasi. CTRL-C to exit\n")
except KeyboardInterrupt:
	pass
