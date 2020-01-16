from datetime import datetime
import unittest

from mast import (
    Mast,
    load_from_csv,
    sort_by_current_rent,
    filter_by_lease_years,
    tenant_name_count,
    filter_by_lease_start_date,
)


class TestMast(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        load_from_csv("Dataset.csv")

    def test_sort_current_rent(self):
        masts = sort_by_current_rent()
        self.assertEqual(masts[0].property_name, "Potternewton Crescent")
        self.assertEqual(masts[0].current_rent, 6600.0)
        self.assertEqual(masts[4].property_name, "Seacroft Gate (Chase) - Block 2")
        self.assertEqual(masts[4].current_rent, 12750.0)

    def test_filter_by_lease_years(self):
        masts = filter_by_lease_years(25)
        self.assertEqual(masts[0].property_name, "Seacroft Gate (Chase) - Block 2")
        self.assertEqual(masts[0].tenant_name, "Vodafone Ltd.")
        self.assertEqual(masts[0].lease_years, 25)
        self.assertEqual(masts[3].property_name, "Seacroft Gate (Chase) - Block 2")
        self.assertEqual(masts[3].tenant_name, "Hutchinson3G Uk Ltd&Everything Everywhere Ltd")
        self.assertEqual(masts[3].lease_years, 25)
        total = sum([(x.current_rent) for x in masts])
        self.assertEqual(total, 46500.0)

    def test_tenant_count(self):
        counts = tenant_name_count()
        self.assertEqual(len(counts), 15)
        self.assertEqual(counts["Arqiva Ltd"], 1)
        self.assertEqual(counts["Everything Everywhere Ltd&Hutchison 3G UK Ltd"], 8)

    def test_filter_by_lease_start_date(self):
        start = datetime.strptime("01 Jun 1999", "%d %b %Y").date()
        end = datetime.strptime("31 Aug 2007", "%d %b %Y").date()
        masts = filter_by_lease_start_date(start, end)
        self.assertEqual(masts[0].property_name, "Potternewton Crescent")
        self.assertEqual(masts[0].tenant_name, "Arqiva Ltd")
        self.assertEqual(
            masts[0].lease_start_date, datetime.strptime("24 Jun 1999", "%d %b %Y").date(),
        )
        self.assertEqual(masts[4].property_name, "Seacroft Gate (Chase) - Block 2")
        self.assertEqual(masts[4].tenant_name, "Hutchinson3G Uk Ltd&Everything Everywhere Ltd")
        self.assertEqual(
            masts[4].lease_start_date, datetime.strptime("21 Aug 2007", "%d %b %Y").date(),
        )
