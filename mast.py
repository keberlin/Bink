from datetime import datetime
import csv
from dataclasses import dataclass
from collections import Counter


@dataclass
class Mast:
    property_name: str
    property_address_1: str
    property_address_2: str
    property_address_3: str
    property_address_4: str
    unit_name: str
    tenant_name: str
    lease_start_date: datetime.date
    lease_end_date: datetime.date
    lease_years: int
    current_rent: float

    def __post_init__(self, *args, **kwargs):
        self.lease_start_date = datetime.strptime(self.lease_start_date, "%d %b %Y").date()
        self.lease_end_date = datetime.strptime(self.lease_end_date, "%d %b %Y").date()
        self.lease_years = int(self.lease_years)
        self.current_rent = float(self.current_rent)


masts = []


def load_from_csv(filename):
    # Load all mast data from a csv encoded data file
    with open(filename, "r") as file:
        reader = csv.reader(file)
        for i, line in enumerate(reader):
            if i == 0:
                continue
            masts.append(Mast(*line))


def sort_by_current_rent():
    # Sort the list using current rent in ascending order
    return sorted(masts, key=lambda x: x.current_rent)


def filter_by_lease_years(years):
    # Filter out just the masts with 'years' lease years
    return list(filter(lambda x: x.lease_years == years, masts))


def tenant_name_count():
    # Get a count of masts for each tenant name
    return Counter([(x.tenant_name) for x in masts])


def filter_by_lease_start_date(start, end):
    # List all masts with a lease start date between 'start' and 'end'
    return list(filter(lambda x: start <= x.lease_start_date <= end, masts))
