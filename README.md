Application to load and process cellular mast data.

Usage: python app.py [--sort-current-rent] [--filter-by-lease-years] [--tenant-name-count] [--filter-lease-start-date] [--all]
    sort-current-rent       - output the first 5 masts with the lowest current rent
    filter-by-lease-years   - output all the masts with lease years of 25
    tenant-name-count       - output a count of masts for each tenant name
    filter-lease-start-date - output all masts with a lease start date between 1st June 1999 and 31st Aaugust 2007
    all                     - output all the above

The application has the following files:
    mast.py - for defining the structure of a mast along with its component parts and functions to perform their manipulation and filtering
    app.py - the main application file to handle command line arguments and logic
    test_mast.py - pytest compatible file for running tests for mast.py functions

Feedback:
    I've kept the code as simple as possible. The dataset csv file is loaded into a global variable which is not ideal
and would not hold up within a multithreaded environment. It would be better to store the mast details within a database
in a commercial setup.
    Each of the functions are very specific and could be made more general if needed. Eg the sort by current rent could
have the sort key passed in and be able to sort on any of a mast's properties.
    The output uses the default __repr__ function for the Mast class which lists all its attributes and their values.
