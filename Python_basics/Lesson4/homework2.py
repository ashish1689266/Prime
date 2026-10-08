# Create a class book with the following attributes
# title, author, list of reviews
# And add methods to
# add a new review
# count reviews
# display all reviews
class book:
    
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.reviews = []
        self.count = 0

    def add_review(self, new_review):
        self.reviews.append(new_review)
        self.count += 1
        print(f"Review Added for the book '{self.title}'")

    def review_count(self):
        print(f"The count of reviews for '{self.title}' is {self.count}")

    def display_reviews(self):
        i = 1
        for review in self.reviews:
            print(f"{i}. {review}")
            i += 1

b1 = book("Wings of Fire", "APJ Abdul Kalam")
b1.add_review("Very good book")
b1.add_review("Great Person")
b1.add_review("Very inspiring")
b1.review_count()
b1.display_reviews()
print()
b2 = book("Discovery of India", "Jawahar Lal Nehru")
b2.add_review("Very good book")
b2.add_review("Great Person")
b2.add_review("Very inspiring")
b2.review_count()
b2.display_reviews()
    
    