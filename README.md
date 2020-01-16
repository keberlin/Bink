Application to load and process cellular mast data.

Usage: python app.py [--sort-current-rent] [--filter-by-lease-years] [--tenant-name-count] [--filter-lease-start-date] [--all]
    sort-current-rent       - output the first 5 masts with the lowest current rent
    filter-by-lease-years   - output all the masts with lease years of 25
    tenant-name-count       - output a count of masts for each tenant name
    filter-lease-start-date - output all masts with a lease start date between 1st June 1999 and 31st Aaugust 2007

The application has 2 files:
  mast.py - for defining the structure of a mast along with its component parts and functions to perform their manipulation and filtering
  app.py - the main application file to handle command line arguments and logic
