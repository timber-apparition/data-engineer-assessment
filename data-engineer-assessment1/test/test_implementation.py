import pytest
import pandas

from src.implementation import *

RIDE_DATA_PATH = 'data/indego-trips-2022-q2.csv'
STATION_DATA_PATH = 'data/indego-stations-2023-04-01.csv'


@pytest.fixture(scope="session")
def test_load_ride_data():
    ride_recs = load_ride_data(RIDE_DATA_PATH)
    assert len(ride_recs.index) == 257350


def test_load_station_data():
    station_recs = load_station_data(STATION_DATA_PATH)
    assert len(station_recs.index) == 233


# definition for optional data check
# def _check_enriched_data(enriched_data, rec):
#    record_check = enriched_data.filter(enriched_data.rec_id == expected['rec_id'])
#    assert len(record_check.index) == 1
#    assert record_check.first().asDict() == expected


def test_enrich_events():
    enriched_data = enrich_data(RIDE_DATA_PATH, STATION_DATA_PATH)

    """Call below for optional schema check"""
    # assert enriched_data.schema == ENRICHED_DATA_SCHEMA

    assert len(enriched_data.index) == 17122

    """Code Below is for optional Data Check"""
    # enriched_data_check = []

    # for rec in enriched_data_check:
    #    _check_enriched_event(enriched_data, rec)
