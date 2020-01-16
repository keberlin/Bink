from datetime import datetime
import argparse

from mast import (
    Mast,
    load_from_csv,
    sort_by_current_rent,
    filter_by_lease_years,
    tenant_name_count,
    filter_by_lease_start_date,
)


parser = argparse.ArgumentParser(description="Process cellular mast data.")
parser.add_argument(
    "--sort-current-rent",
    action="store_true",
    default=False,
    help="display first 5 masts with the lowest current rent",
)
parser.add_argument(
    "--filter-by-lease-years", action="store_true", default=False, help="display masts with lease years of 25",
)
parser.add_argument(
    "--tenant-name-count", action="store_true", default=False, help="display a count of masts for each tenant name",
)
parser.add_argument(
    "--filter-by-lease-start-date",
    action="store_true",
    default=False,
    help="display masts with a lease start date between 1st June 1999 and 31st August 2007",
)
parser.add_argument("--all", action="store_true", default=False, help="display all options")
args = parser.parse_args()


# Load up all cellular mast data
load_from_csv("Dataset.csv")


if args.sort_current_rent or args.all:
    # Sort the list using current rent in ascending order
    masts = sort_by_current_rent()
    print("First 5 masts sorted by current rent in ascending order:")
    for mast in masts[:5]:
        print(mast)
    print()


if args.filter_by_lease_years or args.all:
    # Filter out just the masts with 25 lease years
    masts = filter_by_lease_years(25)
    print("Masts with 25 lease years:")
    for mast in masts:
        print(mast)
    total = sum([(x.current_rent) for x in masts])
    print("Total rent:", total)
    print()


if args.tenant_name_count or args.all:
    # Get a count of masts for each tenant name
    counts = tenant_name_count()
    for key, value in counts.items():
        print("Tenant: {} has {} mast(s)".format(key, value))
    print()


if args.filter_by_lease_start_date or args.all:
    # List all masts with a lease start date between 1st June 1999 and 31st August 2007
    start = datetime.strptime("01 Jun 1999", "%d %b %Y").date()
    end = datetime.strptime("31 Aug 2007", "%d %b %Y").date()
    masts = filter_by_lease_start_date(start, end)
    print("Masts with a lease start date between 1st June 1999 and 31st August 2007:")
    for mast in masts:
        print(
            "Mast: {}, tenant: {} has a lease start date of {}".format(
                mast.property_name, mast.tenant_name, datetime.strftime(mast.lease_start_date, "%d/%m/%Y"),
            )
        )
    print()
