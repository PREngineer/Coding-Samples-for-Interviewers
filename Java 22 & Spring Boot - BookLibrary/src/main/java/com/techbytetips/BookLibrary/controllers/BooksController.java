package com.techbytetips.BookLibrary.controllers;

import org.springframework.web.bind.annotation.RestController;

import com.techbytetips.BookLibrary.Responses.BookLibraryResponseHandler;
import com.techbytetips.BookLibrary.models.Book;
import com.techbytetips.BookLibrary.services.implementations.BookService;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;

// Define as a REST controller
@RestController
@RequestMapping("/Books")
public class BooksController {
  
  // Create an instance of the Service
  BookService bookService;
  
  // Controller Constructor
  public BooksController( BookService bookService ) {
    this.bookService = bookService;
  }

  /*
   * getAllBooks - Retrieve all the books from the database (/Books)
   * @return List<Book> - A list of books
   */
  @GetMapping()
  public ResponseEntity<Object> getAllBooks() {
    // Prepare the response and return it
    return BookLibraryResponseHandler.allBooksResponse( "All books provided", HttpStatus.OK, bookService.getAllBooks() );
  }

  /*
   * getBook - Retrieve a specific book from the database (/Books/{bookID})
   * @param bookID - The book's id
   * @return Book - The book
   */
  @GetMapping( "{bookID}" )
  public ResponseEntity<Object> getBook( @PathVariable("bookID") String bookID ) {

    // Prepare the response and return it
    return BookLibraryResponseHandler.singleBookResponse( "Book provided", HttpStatus.OK, bookService.getBook( bookID ) );
  }

  /*
   * addBook - Adds a book to the database
   * @param Book - The book to save
   * @return String - A message
   */
  /*
    Test with the following from Postman
   {
    "id": "1", 
    "title": "Submitted Book",
    "authorFirstName": "Jorge",
    "authorLastName": "Pabón",
    "publisher": "TechByteTips",
    "publicationDate": "07/03/2024",
    "isbn": "038-01234569875",
    "language": "Spanish",
    "series": "The Cloud",
    "seriesNumber": "1",
    "synopsis": "Jorge programs in Spring Boot."
   }
   */
  @PostMapping
  public ResponseEntity<Object> addBook(@RequestBody Book book ){
    // Add book to library
    bookService.createBook( book );

    // Return a simple message
    return BookLibraryResponseHandler.simpleMessageResponse( "Book added to the library!", HttpStatus.OK );
  }

  /*
   * updateBook - Updates the book/s information in the database (/Books)
   * @param Book - The book to update
   * @return String - A message
   */
  /*
    Test with the following from Postman
   {
    "id" : "1",
    "title": "First Submitted Book",
    "authorFirstName": "Jorge",
    "authorLastName": "Pabón",
    "publisher": "TechByteTips",
    "publicationDate": "07/03/2024",
    "isbn": "038-01234569876",
    "language": "Spanish",
    "series": "The Cloud",
    "seriesNumber": "1",
    "synopsis": "Jorge programs in Spring Boot."
  }
   */
  @PutMapping
  public ResponseEntity<Object> updateBook(@RequestBody Book book ){
    // Update book in library
    bookService.updateBook( book );
    
    // Return a simple message
    return BookLibraryResponseHandler.simpleMessageResponse( "Book updated in the library!", HttpStatus.OK );
  }

  /*
   * deleteBook - Deletes a book from the database (/Books/{ID})
   * @param bookID - The book's ID
   * @return String - A message
   */
  @DeleteMapping( "{bookID}" )
  public ResponseEntity<Object> deleteBook(@PathVariable("bookID") String bookID ){
    // Delete book from library
    bookService.deleteBook( bookID );

    // Return a simple message
    return BookLibraryResponseHandler.simpleMessageResponse( "Book deleted from the library!", HttpStatus.OK );
  }

}