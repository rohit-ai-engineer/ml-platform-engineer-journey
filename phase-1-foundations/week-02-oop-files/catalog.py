# Catalog class - manages a collection of Content objects

from content import Content

class Catalog:
    def __init__(self):
        self.items = []  # Empty list to store Content objects
    
    def add_content(self, content):
        """Add a Content object to the catalog"""
        self.items.append(content)
        print(f"✅ Added: {content.title}")
    
    def exists(self, title):
        """Check if content with this title already exists"""
        for item in self.items:
            if item.title.lower() == title.lower():
                return True
        return False
    
    def remove_content(self, title):
        """Remove content by title"""
        for item in self.items:
            if item.title.lower() == title.lower():
                self.items.remove(item)
                print(f"❌ Removed: {item.title}")
                return
        print(f"⚠️  '{title}' not found in catalog")
    
    def search_by_genre(self, genre):
        """Find all content matching a genre"""
        results = []
        for item in self.items:
            if item.matches_genre(genre):
                results.append(item)
        return results
    
    def display_all(self):
        """Show all content in the catalog"""
        if len(self.items) == 0:
            print("Catalog is empty")
            return
        
        print(f"\n=== Catalog ({len(self.items)} items) ===")
        for item in self.items:
            print(f"- {item.title} ({item.genre}, {item.duration} min)")
    def save_to_file(self, filename="catalog.json"):
        """Save catalog to JSON file"""
        import json
        
        data = []
        for item in self.items:
            data.append({
                'title': item.title,
                'genre': item.genre,
                'duration': item.duration,
                'release_year': item.release_year
            })
        
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)
        
        print(f"💾 Saved {len(self.items)} items to {filename}")
    
    def load_from_file(self, filename="catalog.json"):
        """Load catalog from JSON file"""
        import json
        
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
            
            self.items = []  # Clear current items
            for item_data in data:
                content = Content(
                    item_data['title'],
                    item_data['genre'],
                    item_data['duration'],
                    item_data['release_year']
                )
                self.items.append(content)
            
            print(f"📂 Loaded {len(self.items)} items from {filename}")
        except FileNotFoundError:
            print(f"⚠️  {filename} not found. Starting with empty catalog.")

# Test save/load
catalog = Catalog()

# Load existing data
catalog.load_from_file()

# Add shows only if they don't exist
shows = [
    ("Breaking Bad", "Drama", 47, 2008),
    ("Stranger Things", "Sci-Fi", 50, 2016),
    ("The Office", "Comedy", 22, 2005),
    ("Inception", "Action", 148, 2010)
]

for title, genre, duration, year in shows:
    if not catalog.exists(title):
        show = Content(title, genre, duration, year)
        catalog.add_content(show)

# Save it
catalog.save_to_file()

# Display
catalog.display_all()

