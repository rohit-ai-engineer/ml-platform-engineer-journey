import requests
import json

# Free movie API (no signup needed for basic use)
BASE_URL = "https://www.omdbapi.com/"
API_KEY = "trilogy"  # Demo key (limited requests)

def search_movie(title):
    """Search for a movie by title"""
    params = {
        'apikey': API_KEY,
        't': title  # t = title search
    }
    
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        movie = response.json()
        
        if movie.get('Response') == 'True':
            return movie
        else:
            print(f"❌ Movie not found: {movie.get('Error')}")
            return None
    else:
        print(f"❌ API Error: {response.status_code}")
        return None
    
    
def save_movies_to_file(movies, filename="movies.json"):
    """Save movie data to JSON file"""
    with open(filename, 'w') as f:
        json.dump(movies, f, indent=2)
    print(f"💾 Saved {len(movies)} movies to {filename}")

def load_movies_from_file(filename="movies.json"):
    """Load movie data from JSON file"""
    try:
        with open(filename, 'r') as f:
            movies = json.load(f)
        print(f"📂 Loaded {len(movies)} movies from {filename}")
        return movies
    except FileNotFoundError:
        print(f"⚠️  {filename} not found")
        return []
def search_movie_by_year(title, year):
    """Search for a movie by title and year"""
    params = {
        'apikey': API_KEY,
        't': title,
        'y': year  # y = year parameter
    }
    
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        movie = response.json()
        if movie.get('Response') == 'True':
            return movie
        else:
            print(f"❌ Movie not found: {movie.get('Error')}")
            return None
    else:
        print(f"❌ API Error: {response.status_code}")
        return None
def filter_by_rating(movies, min_rating):
    """Return movies with rating >= min_rating"""
    filtered = []
    for movie in movies:
        try:
            rating = float(movie.get('imdbRating', 0))
            if rating >= min_rating:
                filtered.append(movie)
        except ValueError:
            # Some movies have 'N/A' as rating
            pass
    return filtered
def export_report(movies, filename="movie_report.txt"):
    """Export a text report of the collection"""
    with open(filename, 'w') as f:
        f.write("="*50 + "\n")
        f.write("MOVIE COLLECTION REPORT\n")
        f.write("="*50 + "\n\n")
        f.write(f"Total Movies: {len(movies)}\n\n")
        
        for i, movie in enumerate(movies, 1):
            f.write(f"{i}. {movie['Title']} ({movie['Year']})\n")
            f.write(f"   Rating: {movie['imdbRating']}/10\n")
            f.write(f"   Genre: {movie['Genre']}\n")
            f.write(f"   Director: {movie.get('Director', 'N/A')}\n")
            f.write("\n")
        
        f.write("="*50 + "\n")
    
    print(f"📄 Report exported to {filename}")

# Main program
movies_collection = []

while True:
    print("\n--- Movie Collector ---")
    print("1. Search and add movie")
    print("2. Show all movies")
    print("3. Save to file")
    print("4. Load from file")
    print("5. Remove a movie")
    print("6. Filter by rating")
    print("7. Export report")
    print("8. Exit")
    
    choice = input("Choose option: ")
    
    if choice == "1":
        title = input("Enter movie title: ")
        year_input = input("Enter year (or press Enter to skip): ")
        
        if year_input:
            movie = search_movie_by_year(title, year_input)
        else:
            movie = search_movie(title)
        
        if movie:
            movies_collection.append(movie)
            print(f"✅ Added: {movie['Title']} ({movie['Year']})")
    
    elif choice == "2":
        if movies_collection:
            print(f"\n📚 Collection ({len(movies_collection)} movies):")
            for m in movies_collection:
                print(f"- {m['Title']} ({m['Year']}) - {m['imdbRating']}/10")
        else:
            print("Collection is empty")
    
    elif choice == "3":
        save_movies_to_file(movies_collection)
    
    elif choice == "4":
        movies_collection = load_movies_from_file()
    
    elif choice == "5":  # NEW - REMOVE
        if movies_collection:
            print("\n📚 Current Collection:")
            for i, m in enumerate(movies_collection, 1):
                print(f"{i}. {m['Title']} ({m['Year']})")
            
            try:
                num = int(input("Enter number to remove (0 to cancel): "))
                if num > 0 and num <= len(movies_collection):
                    removed = movies_collection.pop(num - 1)
                    print(f"❌ Removed: {removed['Title']}")
                elif num != 0:
                    print("Invalid number")
            except ValueError:
                print("Invalid input")
        else:
            print("Collection is empty")

    elif choice == "6":  # NEW OPTION
        min_rating = float(input("Minimum rating (0-10): "))
        high_rated = filter_by_rating(movies_collection, min_rating)
        
        if high_rated:
            print(f"\n⭐ Movies rated {min_rating}+ ({len(high_rated)} found):")
            for m in high_rated:
                print(f"- {m['Title']} ({m['Year']}) - {m['imdbRating']}/10")
        else:
            print(f"No movies found with rating >= {min_rating}")
    elif choice == "7":  # NEW - EXPORT
        if movies_collection:
            export_report(movies_collection)
        else:
            print("Collection is empty")
    
    elif choice == "8":  # EXIT MOVED HERE
        print("👋 Goodbye!")
        break
    
    else:
        print("Invalid choice")