# Stating our colors and countries
colors = ['Green', 'Yellow', 'Black', 'Magenta', 'White', 'Cyan', 'Red']
countries = ['France', 'Germany', 'Italy', 'Spain', 'Greece', 'Turkey']

# Neighboring countries of each country
neighbors = {}
neighbors['France'] = ['Germany', 'Italy', 'Spain']
neighbors['Germany'] = ['France']
neighbors['Spain'] = ['Italy', 'Greece', 'France']
neighbors['Italy'] = ['France', 'Spain']
neighbors['Turkey'] = ['Greece']
neighbors['Greece'] = ['Spain', 'Turkey']

colors_of_countries = {}

# Check if a color is good or not for a given country
def promising(country, color):
    for neighbor in neighbors.get(country): 
        color_of_neighbor = colors_of_countries.get(neighbor)
        # If neighbor is of the same color, we cannot use it
        if color_of_neighbor == color:
            return False
    # If color doesn't match any neighbor, we are good to use that color
    return True

# Color gets assigned to a country
def get_color_for_country(country):
    for color in colors:
        # Check if the color is promising for the current country
        if promising(country, color):
            return color

# Print the result
def main():
    for country in countries:
        # Get the color for the current country
        colors_of_countries[country] = get_color_for_country(country)
    print(colors_of_countries)

# Call main 
main()
