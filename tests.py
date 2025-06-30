import pytest

from main import BooksCollector

@pytest.fixture
def collector():
    return BooksCollector()

class TestBooksCollector:

    def test_init_sets_up_empty_and_default_values(self, collector):
        assert collector.books_genre == {}
        assert collector.favorites == []
        assert collector.genre == ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
        assert collector.genre_age_rating == ['Ужасы', 'Детективы']

    def test_add_new_book_with_valid_name_adds_to_books_genre(self, collector,):
        collector.add_new_book('Война и Мир')
        assert collector.books_genre == {'Война и Мир': ''}

    @pytest.mark.parametrize('book_name, expected', [
        ('', {}),
        ('A' * 50, {})
    ])
    def test_add_new_book_invalid_name_does_not_adds_to_books_genre(self, collector, book_name, expected):
        collector.add_new_book(book_name)
        assert collector.books_genre == expected

    def test_add_duplicate_book_to_books_genre_does_not_add(self, collector):
        collector.add_new_book('Война и Мир')
        collector.add_new_book('Война и Мир')
        assert len(collector.books_genre) == 1

    @pytest.mark.parametrize('book_name', ['B', 'B' * 40])
    def test_add_new_book_accepts_name_with_length_1_and_40(self, collector, book_name):
        collector.add_new_book(book_name)
        assert book_name in collector.books_genre
        assert collector.books_genre[book_name] == ''

    def test_set_book_genre_with_valid_genre_succeeds(self, collector):
        collector.add_new_book('Война и Мир')
        collector.set_book_genre('Война и Мир','Детективы')
        assert collector.books_genre == {'Война и Мир':'Детективы'}

    def test_set_book_invalid_genre_is_not_set(self, collector):
        collector.add_new_book('Маленький принц')
        collector.set_book_genre('Маленький принц', 'Боевик')
        assert collector.books_genre == {'Маленький принц':''}

    def test_get_book_genre_returns_genre_for_existing_book(self, collector):
        collector.add_new_book('Война и Мир')
        collector.set_book_genre('Война и Мир','Детективы')
        assert collector.get_book_genre('Война и Мир') == 'Детективы'

    def test_get_books_with_specific_genre_returns_comedy_books(self, collector):
        collector.add_new_book('Gladiator')
        collector.set_book_genre('Gladiator', 'Ужасы')
        collector.add_new_book('The Godfather')
        collector.set_book_genre('The Godfather', 'Комедии')
        collector.add_new_book('Fight Club')
        collector.set_book_genre('Fight Club', 'Комедии')
        assert sorted(collector.get_books_with_specific_genre('Комедии')) == sorted(['Fight Club', 'The Godfather'])

    def test_get_books_genre_returns_full_dict(self, collector):
        collector.add_new_book('The Matrix')
        collector.set_book_genre('The Matrix', 'Детективы')
        assert collector.get_books_genre() == collector.books_genre

    def test_get_books_for_children_returns_only_non_adult_genres(self, collector):
        collector.add_new_book('Gladiator')
        collector.set_book_genre('Gladiator','Ужасы')
        collector.add_new_book('The Godfather')
        collector.set_book_genre('The Godfather','Комедии')
        collector.add_new_book('Finding Nemo')
        collector.set_book_genre('Finding Nemo','Мультфильмы')
        assert sorted(collector.get_books_for_children()) == sorted(['The Godfather', 'Finding Nemo'])

    def test_add_book_in_favorites_adds_book(self, collector):
        collector.add_new_book('The Matrix')
        collector.add_book_in_favorites('The Matrix')
        assert len(collector.favorites) == 1
        assert collector.favorites == ['The Matrix']

    def test_add_book_in_favorites_prevents_duplicates(self, collector):
        collector.add_new_book('The Matrix')
        collector.add_book_in_favorites('The Matrix')
        collector.add_book_in_favorites('The Matrix')
        assert len(collector.favorites) == 1
        assert collector.favorites == ['The Matrix']

    def test_add_book_in_favorites_ignores_unknown_books(self, collector):
        collector.add_new_book('The Matrix')
        collector.add_book_in_favorites('Coco')
        assert len(collector.favorites) == 0
        assert collector.favorites == []

    def test_delete_book_from_favorites_removes_book(self, collector):
        collector.add_new_book('The Matrix')
        collector.add_new_book('Coco')
        collector.add_book_in_favorites('The Matrix')
        collector.add_book_in_favorites('Coco')
        collector.delete_book_from_favorites('The Matrix')
        assert len(collector.favorites) == 1
        assert collector.favorites == ['Coco']

    def test_get_list_of_favorites_books_returns_current_list(self, collector):
        collector.add_new_book('The Lion King')
        collector.add_book_in_favorites('The Lion King')
        assert collector.get_list_of_favorites_books() == collector.favorites