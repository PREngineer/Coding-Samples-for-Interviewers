package com.techbytetips.BookLibrary.services.implementations;

import java.util.List;

import org.springframework.stereotype.Service;

import com.techbytetips.BookLibrary.database.BooksDatabase;
import com.techbytetips.BookLibrary.exceptions.BookNotFoundException;
import com.techbytetips.BookLibrary.models.Book;
import com.techbytetips.BookLibrary.services.BookServiceInterface;

// Implementation of the Service (Business Logic)
@Service
public class BookService implements BookServiceInterface{

  // Rely on the Jpa database implementation
  BooksDatabase booksDB;

  public BookService(BooksDatabase booksDB) {
    this.booksDB = booksDB;
  }

  /*
   * createBook - Saves the book in the database
   * @param book - The book to save
   * @return String - Message
   */
  @Override
  public String createBook(Book book) {
    booksDB.save( book );
    
    return "Book added to library!";
  }

  /*
   * updateBook - Updates the book in the database
   * @param book - The new book data
   * @return String - Message
   */
  @Override
  public String updateBook(Book book) {
    booksDB.save( book );

    return "Book updated in library!";
  }

  /*
   * deleteBook - Deletes the book from the database
   * @param book - The book's ID
   * @return String - Message
   */
  @Override
  public String deleteBook(String ID) {
    booksDB.deleteById( ID );

    return "Book deleted from library!";
  }

  /*
   * getBook - Retrieves the book from the database
   * @param book - The book's ID
   * @return Book - The object representing the book
   */
  @Override
  public Book getBook(String ID) {
    // If we don't find the book
    if( booksDB.findById( ID ).isEmpty() ){
      // Throw exception
      throw new BookNotFoundException( "The requested book does not exist in the library!" );
    }

    // Return the book
    return booksDB.findById( ID ).get();
  }

  /*
   * Book - Retrieve all the books from the database
   * @return List<Book> - A list of books
   */
  @Override
  public List<Book> getAllBooks() {
    return booksDB.findAll();
  }
  
}