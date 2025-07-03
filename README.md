# BooksCollector

## Project Description

`BooksCollector` is a class for managing a book collection. The class allows you to add books, assign genres to them, filter books by genre or age category, and manage a favorites system.
In addition, the project includes unit tests for all class methods to ensure their correct functionality.

---

## Class Description: BooksCollector

### Attributes:
- `books_genre` — a dictionary where the keys are book titles and the values are their genres.
- `favorites` — a list containing favorite books.
- `genre` — a list of available book genres: `['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']`. (`['Fantasy', 'Horror', 'Detectives', 'Cartoons', 'Comedies'].`)
- `genre_age_rating` — a list of genres with age restrictions: `['Ужасы', 'Детективы']`.(`['Horror', 'Detectives']`)

---

### Class Methods:

#### 1. **add_new_book(name)**  
Adds a new book to the collection.  
- **Conditions:**
  - The book title must not exceed 40 characters.
  - If the book already exists in the collection, it won't be added again.

#### 2. **set_book_genre(name, genre)**  
Sets the genre for a book.
- **Conditions:**
  - The book must already exist in the collection.
  - The genre must be one of the available genres in the `genre` list.

#### 3. **get_book_genre(name)**  
Returns the genre of a specific book.
- If the book is not in the collection, returns `None`.

#### 4. **get_books_with_specific_genre(genre)**  
Returns a list of books with the specified genre.
- **Condition:** The genre must be one of the supported genres.

#### 5. **get_books_genre()**  
Returns the current dictionary of all books with their genres.

#### 6. **get_books_for_children()**  
Returns a list of books appropriate for children.
- **Condition:** The book's genre must not have an age restriction (i.e., genres from `genre_age_rating` will be excluded).

#### 7. **add_book_in_favorites(name)**  
Adds a book to the list of favorites.
- **Conditions:**
  - The book must exist in the collection.
  - The same book cannot be added to favorites more than once.

#### 8. **delete_book_from_favorites(name)**  
Removes a book from the favorites list if it is present.

#### 9. **get_list_of_favorites_books()**  
Returns the current list of favorite books.

---

## Unit Tests Description

Tests are written using `unittest` and cover the functionality of the `BooksCollector` class.  

### Tested Methods:

**test_init_sets_up_empty_and_default_values**
    Upon initialization, all collections should be empty, and default genres  

**test_add_new_book_with_valid_name_adds_to_books_genre**
   Verifies that a book with a valid name is added to `books_genre`.

**test_add_new_book_invalid_name_does_not_adds_to_books_genre**
   Verifies that a book with an invalid name is not added to `books_genre`.

**test_add_duplicate_book_to_books_genre_does_not_add**
    Verifies that a duplicate book title is not added to `books_genre`.

**test_add_new_book_accepts_name_with_length_1_and_40**
    Verifies that book names with boundary lengths (1 and 40 characters) are accepted.

**test_set_book_genre_with_valid_genre_succeeds**
    Verifies that assigning a valid genre to an existing book succeeds.

**test_set_book_invalid_genre_is_not_set**
    Verifies that an invalid genre is not assigned to a book.

**test_get_book_genre_returns_genre_for_existing_book**
    Verifies that `get_book_genre` returns the correct genre for a given book.

**test_get_books_with_specific_genre_returns_comedy_books**
    Tests that only books with the specified genre are returned.

**test_get_books_genre_returns_full_dict**
    Verifies that `get_books_genre` returns the complete dictionary of books and genres.

**test_get_books_for_children_returns_only_non_adult_genres**
    Verifies that `get_books_for_children` returns only books with child-appropriate genres.

**test_add_book_in_favorites_adds_book**
    Tests that a book is correctly added to the favorites list.

**test_add_book_in_favorites_prevents_duplicates**
    Verifies that duplicates are not added to favorites.

**test_add_book_in_favorites_ignores_unknown_books**
    Verifies that books not in `books_genre` are not added to favorites.

**test_delete_book_from_favorites_removes_book**
    Test that a book is correctly removed from favorites.

**test_get_list_of_favorites_books_returns_current_list**
    Test that the favorites list is returned correctly.

---
