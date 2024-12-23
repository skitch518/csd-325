def format_location(city, country, language, population=None):
  f_location = f"{city}, {country}"
  f_location = f_location.title() 

  try:
    if population is not None:
      population = int(population)
      f_location += f' - Population: {population:,}'
      if language:
        language = language.title()
        f_location += f" {language}"
        return f_location
  except ValueError:
    print(f"Population must be an integer: ")
  if language:
    language = language.title() 
    f_location += f" {language}"
    return f_location
  else:  
    return f_location 


print("Enter 'q' at any time to quit.")
while True:
  city = input("\nPlease enter a city name: ")
  if city == 'q':
     break
  country = input("Please enter a country name: ")
  if country == 'q':
    break
  population = input("Please enter population: ")
  if population == 'q':
     break  
  language = input("Please enter the spoken language: ")
  if language == 'q':
    break
  formatted_location = format_location(city, country, population)
  print(f"\nFormatted City, Country: {formatted_location}.")