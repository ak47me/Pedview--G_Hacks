# importing geopy library and Nominatim class
from geopy.geocoders import Nominatim

# calling the Nominatim tool and create Nominatim class
loc = Nominatim(user_agent="Geopy Library")

# entering the location name
getLoc = loc.geocode("ETLC Edmonton Alberta")

# check if the location was found
if getLoc:
    # printing address
    print(getLoc.address)

    # printing latitude and longitude
    print("Latitude = ", getLoc.latitude, "\n")
    print("Longitude = ", getLoc.longitude)
else:
    print("Location not found")