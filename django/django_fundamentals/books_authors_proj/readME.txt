1-Create the Book class model
Create 5 books with the following names: C Sharp, Java, Python, PHP, Ruby:

	Book.objects.create(title='c',desc='this is a book')
	Book.objects.create(title='java',desc='this is a book')
	Book.objects.create(title='python',desc='this is a book')
	Book.objects.create(title='PHP',desc='this is a book')
	Book.objects.create(title='ruby',desc='this is a book')

2-Create the Author class model/
Create 5 different authors: Jane Austen, Emily Dickinson, Fyodor Dostoevsky, William Shakespeare, Lau Tzu
	Author.objects.create(first_name='Jane',last_name='Austen')
	Author.objects.create(first_name='Emily',last_name='Dickinson')
	Author.objects.create(first_name='Fyodor',last_name='Dostoevsky')
	Author.objects.create(first_name='William',last_name='Shakespeare')
	Author.objects.create(first_name='Lau',last_name='Tzu')

3-Query: Change the name of the C Sharp book to C#:

	book1_to_update = Book.objects.get(title='c')
	book1_to_update.title='c#'
	book1_to_update.save()


4-Query: Change the first name of the 4th author to Bill:
	author_update = Author.objects.get(id=4)
	author_update.first_name ='Bill'
	author_update.save()

5-Query: Assign the first author to the first 2 books:

	author_one = Author.objects.get(id=1)
	book_1 = Book.objects.get(id=1)
	book_2 = Book.objects.get(id=2)
	author_one.books.add(book_1)
	author_one.books.add(book_2)

6-Query: Assign the second author to the first 3 books:

	author_2 = Author.objects.get(id=2)
	book_1 = Book.objects.get(id=1)
	book_2 = Book.objects.get(id=2)
	book_3 = Book.objects.get(id=3)
	book_4 = Book.objects.get(id=4)

	author_2.books.add(book_1)
	author_2.books.add(book_2)
	author_2.books.add(book_3)
	author_2.books.add(book_4)



7-Query: Assign the third author to the first 4 books:


	author_three = Author.objects.get(id=3)
	book_1 = Book.objects.get(id=1)
	book_2 = Book.objects.get(id=2)
	book_3 = Book.objects.get(id=3)
	book_4 = Book.objects.get(id=4)

	author_three.books.add(book_1)
	author_three.books.add(book_2)
	author_three.books.add(book_3)
	author_three.books.add(book_4)

8-Query: Assign the fourth author to the first 5 books (or in other words, all the books)


	author_fourth = Author.objects.get(id=4)

	book_1 = Book.objects.get(id=1)
	book_2 = Book.objects.get(id=2)
	book_3 = Book.objects.get(id=3)
	book_4 = Book.objects.get(id=4)
	book_5 = Book.objects.get(id=5)

	author_fourth.books.add(book_1)
	author_fourth.books.add(book_2)
	author_fourth.books.add(book_3)
	author_fourth.books.add(book_4)
	author_fourth.books.add(book_5)

9-Query: Retrieve all the authors for the 3rd book:
	

	book3 = Book.objects.get(id=3)
	authors3book = Author.objects.filter(id=3)
	author_book3= Author.objects.filter(books=book3)

10-Query: Remove the first author of the 3rd book:

	author1book3= Author.objects.get(id=3)
	book3 = Book.objects.get(id=3)
	author1book3.books.remove(book3)

11-Query: Add the 5th author as one of the authors of the 2nd book


	author5 = Author.objects.get(id=5)
	book2=Book.objects.get(id=2)
	book2.author.add(author5)
	author5.books.add(book2)

12-Query: Find all the books that the 3rd author is part of:

	author3 = Author.objects.get(id=3)
	author3.books.all()

13-Query: Find all the authors that contributed to the 5th book:

	author5 = Author.objects.get(id=5)
	author5.books.all()
