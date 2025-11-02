import heapq
import sys

class CityNavigation:
    def __init__(self, locations):
        self.locations = locations
        self.graph = {location: [] for location in locations}
        self.location_names = {
            0: "Home", 1: "School", 2: "Mall", 3: "Hospital",
            4: "Park", 5: "Station", 6: "Airport"
        }
    
    def add_route(self, start, end, distance, time):
        # Store both distance and time
        self.graph[start].append((end, distance, time))
        self.graph[end].append((start, distance, time))
    
    def dijkstra_shortest_path(self, source, criterion='distance'):
        """Dijkstra's algorithm for shortest paths"""
        n = len(self.locations)
        dist = [sys.maxsize] * n
        prev = [-1] * n
        dist[source] = 0
        
        # Priority queue: (distance, vertex)
        pq = [(0, source)]
        
        while pq:
            current_dist, u = heapq.heappop(pq)
            
            # Skip if we found a better path already
            if current_dist > dist[u]:
                continue
            
            for v, distance, time in self.graph[u]:
                # Choose criterion
                if criterion == 'distance':
                    weight = distance
                else:  # time
                    weight = time
                
                new_dist = current_dist + weight
                
                if new_dist < dist[v]:
                    dist[v] = new_dist
                    prev[v] = u
                    heapq.heappush(pq, (new_dist, v))
        
        return dist, prev
    
    def get_path(self, prev, target):
        """Reconstruct path from previous array"""
        path = []
        while target != -1:
            path.append(target)
            target = prev[target]
        return path[::-1]
    
    def display_navigation(self, source, criterion='distance'):
        """Display navigation results"""
        dist, prev = self.dijkstra_shortest_path(source, criterion)
        
        print(f"\nSHORTEST PATHS FROM {self.location_names[source]} (by {criterion}):")
        print("=" * 65)
        print(f"{'Destination':<15} {'Distance':<10} {'Time':<10} {'Path'}")
        print("-" * 65)
        
        for i in range(len(self.locations)):
            if i != source:
                path = self.get_path(prev, i)
                path_names = [self.location_names[p] for p in path]
                
                # Find actual distance and time for this path
                total_distance = 0
                total_time = 0
                for j in range(len(path) - 1):
                    u, v = path[j], path[j + 1]
                    for neighbor in self.graph[u]:
                        if neighbor[0] == v:
                            total_distance += neighbor[1]
                            total_time += neighbor[2]
                            break
                
                if criterion == 'distance':
                    display_value = total_distance
                else:
                    display_value = total_time
                
                print(f"{self.location_names[i]:<15} {total_distance:<10} {total_time:<10} {' → '.join(path_names)}")

# Application Implementation
def city_navigation_application():
    # Create city with 7 locations
    locations = [0, 1, 2, 3, 4, 5, 6]
    city = CityNavigation(locations)
    
    # Add routes: (start, end, distance_km, time_minutes)
    routes = [
        (0, 1, 2, 5),   # Home - School
        (0, 2, 5, 10),  # Home - Mall
        (1, 2, 1, 3),   # School - Mall
        (1, 3, 4, 8),   # School - Hospital
        (2, 4, 3, 7),   # Mall - Park
        (3, 4, 2, 5),   # Hospital - Park
        (3, 5, 6, 12),  # Hospital - Station
        (4, 5, 2, 4),   # Park - Station
        (5, 6, 8, 15),  # Station - Airport
        (2, 6, 12, 20)  # Mall - Airport
    ]
    
    for start, end, distance, time in routes:
        city.add_route(start, end, distance, time)
    
    print("CITY NAVIGATION SYSTEM USING DIJKSTRA'S ALGORITHM")
    print("=" * 65)
    print("Available Locations:")
    for idx, name in city.location_names.items():
        print(f"  {idx}. {name}")
    
    print("\nRoute Network (Distance in km, Time in minutes):")
    for start, end, distance, time in routes:
        print(f"  {city.location_names[start]} ↔ {city.location_names[end]}: {distance}km, {time}min")
    
    # Find shortest paths by distance
    city.display_navigation(0, 'distance')
    
    # Find shortest paths by time
    city.display_navigation(0, 'time')
    
    # Complexity analysis
    print("\n" + "=" * 65)
    print("COMPLEXITY ANALYSIS:")
    print("Time Complexity: O((V + E) log V)")
    print("Space Complexity: O(V + E)")
    print("\nWhere:")
    print("V = Number of vertices (locations) =", len(locations))
    print("E = Number of edges (routes) =", len(routes))
    print("\nBreakdown:")
    print("- Each vertex processed once: O(V)")
    print("- Each edge processed once: O(E)")
    print("- Heap operations (insert/extract): O(log V) per operation")
    print("- Total operations: O((V + E) log V)")

if __name__ == "__main__":
    city_navigation_application()