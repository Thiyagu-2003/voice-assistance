# import phonenumbers
# import opencage
# import folium
# from location_bot import number
# from phonenumbers import geocoder
# from opencage.geocoder import OpenCageGeocode


# pepnumber = pepnumbers.parse(number)
# location = geocoder.description_for_number(pepnumber, "en")
# print(location)

# from phonenumbers import carrier
# service_provider = phonenumbers.parse(number)
# print(carrier.name_for_number(service_provider, "en"))

# api_key ='da5a76d0d6984427882e393dd0b2fcb9'
# geocoder = OpenCageGeocode(api_key)
# query = str(location)
# results = geocoder.geocode(query)
# print(results)

# lat = results[0]['geomentry']['lat']
# lng = results[0]['geomentry']['lng']

# print(lat,lng)

# myMap = folium.Map(location=[lat,lng], zoom_start = 9)
# folium.Marker([lat,lng],popup=location).add_to(myMap)

# myMap.save("mylocation.html")



# import phonenumbers
# import folium
# from location_bot import number  # Ensure `number` is defined in `location_bot`
# from phonenumbers import geocoder, carrier
# from opencage.geocoder import OpenCageGeocode

# # Parse the phone number
# parsed_number = phonenumbers.parse(number)

# # Get location from phone number
# location = geocoder.description_for_number(parsed_number, "en")
# print(f"Location: {location}")

# # Get carrier information
# service_provider = carrier.name_for_number(parsed_number, "en")
# print(f"Service Provider: {service_provider}")

# # OpenCage API key
# api_key = 'da5a76d0d6984427882e393dd0b2fcb9'
# geocoder = OpenCageGeocode(api_key)

# # Geocoding location
# results = geocoder.geocode(location)
# if results and len(results) > 0:
#     lat = results[0]['geometry']['lat']
#     lng = results[0]['geometry']['lng']
#     print(f"Latitude: {lat}, Longitude: {lng}")

#     # Create a map
#     my_map = folium.Map(location=[lat, lng], zoom_start=9)
#     folium.Marker([lat, lng], popup=location).add_to(my_map)

#     # Save the map
#     my_map.save("mylocation.html")
#     print("Map saved as 'mylocation.html'.")
# else:
#     print("Geocoding failed. Unable to get latitude and longitude.")




import webbrowser
import phonenumbers
from location_bot import number  # Ensure `number` is defined in `location_bot`
from phonenumbers import geocoder, carrier
from opencage.geocoder import OpenCageGeocode

# Parse the phone number
parsed_number = phonenumbers.parse(number)

# Get location from phone number
location = geocoder.description_for_number(parsed_number, "en")
print(f"Location: {location}")

# Get carrier information
service_provider = carrier.name_for_number(parsed_number, "en")
print(f"Service Provider: {service_provider}")

# OpenCage API key
api_key = 'da5a76d0d6984427882e393dd0b2fcb9'
geocoder = OpenCageGeocode(api_key)

# Geocoding location
results = geocoder.geocode(location)
if results and len(results) > 0:
    lat = results[0]['geometry']['lat']
    lng = results[0]['geometry']['lng']
    print(f"Latitude: {lat}, Longitude: {lng}")

    # Generate Google Maps URL
    google_maps_url = f"https://www.google.com/maps?q={lat},{lng}"
    print(f"Opening Google Maps: {google_maps_url}")

    # Open the URL in the default web browser
    webbrowser.open(google_maps_url)
else:
    print("Geocoding failed. Unable to get latitude and longitude.")
