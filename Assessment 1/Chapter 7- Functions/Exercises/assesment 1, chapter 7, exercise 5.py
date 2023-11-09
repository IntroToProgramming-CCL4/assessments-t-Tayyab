# Define the function describe_city with the city and country parameters
def describe_city(city, country='unknown country'):
    # Print a simple sentence describing the city and its country
    print(city, "is in", country)

# Call the function for three different cities
describe_city("Paris")  # Call with only the city specified (uses default country)
describe_city("Dubai", "United Arab Emirates")  # Call with both city and country specified
describe_city("Lahore", "Pakistan")  # Call with both city and country specified

