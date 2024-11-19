class Solution:
    def largestAltitude(self, gain):
        # Initialize the starting altitude and the maximum altitude
        altitude = 0
        max_altitude = 0

        # Iterate through the `gain` array
        for g in gain:
            altitude += g  # Update the current altitude
            max_altitude = max(max_altitude, altitude)  # Update the maximum altitude
        
        return max_altitude
