import sys

def main():
    coordinates_tuple = (42.376, -71.115)
    coordinates_list = [42.376, -71.115]
    print(f"{sys.getsizeof(coordinates_tuple)}")
    print(f"{sys.getsizeof(coordinates_list)}")

    '''latitude, longitude = coordinates
    print(f"Latitude: {latitude}")
    print(f"Latitude: {longitude}")'''
    '''print(f"Latitude: {coordinates[0]}")
    print(f"Longitude: {coordinates[1]}")'''

main()

#tuple的功能并无新意，见bee。其好处是内存占用更小