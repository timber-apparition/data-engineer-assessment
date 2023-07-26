import pandas as pd


def load_ride_data(ride_data_path):
    """Parse ride data into a DataFrame"""

    # YOUR CODE HERE
    ride_data = pd.read_csv(ride_data_path)
    return ride_data


def load_station_data(station_data_path):
    """Parse station data into a DataFrame"""

    # YOUR CODE HERE
    raw = pd.read_csv(station_data_path)
    # drop all na columns
    station_data = raw[['Station_ID', 'Station_Name', 'Day of Go_live_date', 'Status']]
    return station_data


def enrich_data(ride_data_path, station_data_path):
    """Create enriched dataset using ruless defined in README Step #3"""

    # YOUR CODE HERE
    rd = load_ride_data(ride_data_path)
    sd = load_station_data(station_data_path)
    # merge ride with station by start staion
    df3 = rd.merge(sd.rename({'Station_ID': 'start_Station_ID', 'Station_Name': 'start_station_name',
                              'Day of Go_live_date': 'start_Day of Go_live_date', 'Status': 'start_Status'}, axis=1),
                   left_on='start_station', right_on='start_Station_ID', how='left')
    # merge in end station info
    df4 = df3.merge(sd.rename({'Station_ID': 'end_Station_ID', 'Station_Name': 'end_station_name',
                               'Day of Go_live_date': 'end_Day of Go_live_date', 'Status': 'end_Status'}, axis=1),
                    left_on='start_station', right_on='end_Station_ID', how='left')
    enriched_data = df4[(df4['passholder_type'] == 'Indego365') & (df4['bike_type'] == 'electric')]
    return enriched_data


def data_to_json(enriched_data):
    """Write data to JSON file using ruless defined in README Step #4"""

    # YOUR CODE HERE
    new_ed = enriched_data[['trip_id', 'duration', 'start_time', 'end_time', 'start_station_name', 'end_station_name',
                            'trip_route_category', 'passholder_type', 'bike_type']]
    new_ed.to_json('../test/data/enriched_data.json', orient='records', lines=True)


import duckdb


# extra credit sql solution
def sql_solution(ride_data_path, station_data_path):
    con = duckdb.connect(database=":memory:", read_only=False)

    query = f'''
            select trip_id, duration,start_time,end_time,ss.Station_Name as start_station_name,
                   es.station_name as end_station_name,trip_route_category, passholder_type, bike_type
            from read_csv_auto('{ride_data_path}', HEADER=TRUE, ALL_VARCHAR=1) rd
            left join read_csv_auto('{station_data_path}', HEADER=TRUE, ALL_VARCHAR=1) ss
                      on rd.start_station =ss.Station_ID 
            left join read_csv_auto('{station_data_path}', HEADER=TRUE, ALL_VARCHAR=1) es
                      on rd.start_station =es.Station_ID
            where passholder_type = 'Indego365' and  bike_type = 'electric'

    '''
    con.execute(query)
    sql_data = con.fetchdf()
    return sql_data


if __name__ == '__main__':
    ed = enrich_data('../test/data/indego-trips-2022-q2.csv', '../test/data/indego-stations-2023-04-01.csv')
    data_to_json(ed)
    sql_data = sql_solution('../test/data/indego-trips-2022-q2.csv', '../test/data/indego-stations-2023-04-01.csv')
    print(sql_data)