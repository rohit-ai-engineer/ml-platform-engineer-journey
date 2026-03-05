# Content class - represents a streaming show or movie

class Content:
    def __init__(self, title, genre, duration, release_year):
        self.title = title
        self.genre = genre
        self.duration = duration
        self.release_year = release_year
    
    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Genre: {self.genre}")
        print(f"Duration: {self.duration} minutes")
        print(f"Released: {self.release_year}")
        print()
    def is_movie(self):
        """Returns True if duration suggests it's a movie (>80 min)"""
        return self.duration > 80
    
    def get_type(self):
        """Returns 'Movie' or 'Episode' based on duration"""
        if self.is_movie():
            return "Movie"
        else:
            return "Episode"
    
    def matches_genre(self, genre):
        """Check if this content matches a given genre"""
        return self.genre.lower() == genre.lower()

