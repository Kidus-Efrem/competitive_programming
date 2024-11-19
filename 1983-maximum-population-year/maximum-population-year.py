class Solution:
    def maximumPopulation(self, logs):
        # Initialize an array to keep track of population changes
        year_count = [0] * 101  # From 1950 to 2050 (inclusive)

        # Populate the array based on birth and death years
        for birth, death in logs:
            year_count[birth - 1950] += 1  # Increment population for birth year
            year_count[death - 1950] -= 1  # Decrement population for death year

        # Calculate the population for each year
        max_population = 0
        max_year = 1950
        current_population = 0

        for year in range(101):
            current_population += year_count[year]
            if current_population > max_population:
                max_population = current_population
                max_year = 1950 + year

        return max_year
