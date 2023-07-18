# README #

Interview problem for Data Engineer Role

## Setup ##

- Set up the virtualenv by running `setup.sh` Note: Powershell should be able to run this script if properly configured/updated. MacOS/Linux should have no issue :)
- Activate the virtualenv by running `source venv/bin/activate` or `venv\Scripts\activate` if on Windows.

## Running Tests ##

In test directory, run `pytest -s`


### Instructions ###

#### Overview #####
Your solution should be implemented in `src/implementation.py` (you may create other files if necessary). 
Please you may import third-party libraries, but prepared to explain why.
The assignment should be completed using Pandas.

#### Problem Details ####
This assigment works with open source data from Indego Bike Share of Philadelphia.
There are two datasets that your application will take as input: Ride Data and Station Data.
Please create a branch with your initials and the date to work with. 

Your solution should do the following using pandas:

Step 1: Load ride data from provided CSV.
Step 2: Load station data from provided CSV. Warning, this data is a little messy.

Step 3: Combine Ride and Station Data. Then filter the dataset to only rows for trip by Indego365 passholders on electric bikes.

Step 4: Write out the enhanced ride dataset in JSON format to a file with the following schema:
            `trip_id, duration, start_time, end_time, start_station_name, end_station_name, trip_route_category, passholder_type, bike_type` Note: Some of these need to be 
                                                                                                                                                   inferred by the join in step 3.
        Each record should be a new line.

##### Final #####
Once your solution passes the basic tests you may create a PR for you solution. This PR will not be mereged, but used to review your solution.

or

if that was too easy, here is extra credit (not necessary):

- Enforce the schema above via the unit tests and make sure the records conform. See code stubs in `test/test_implementation.py`
- Spot check some records via the unit tests to make sure there are some expected sane values. See code stubs in `test/test_implementation.py`
- Implement a solution using a local in memory DB and SQL instead of Pandas

Either way please be prepeared to review your PR, run the tests, and output the JSON file during a techncial interview.

Thanks!



