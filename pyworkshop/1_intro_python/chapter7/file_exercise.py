import json

def main():
    with open("cities.json") as cities_file:
        try:
            cities_data = json.load(cities_file)

            print("Largest cities in the US by population:")
            for index, entry in enumerate(cities_data):
                print(f"{index + 1}: {entry['name']} - {entry['pop']}")
list
        except json.decoder.JSONDecodeError as error:
            print("Sorry, there was an error decoding that json file:")
            print(f"\t {error}")

    print("The file is now closed.")

if __name__ == "__main__":
    main()