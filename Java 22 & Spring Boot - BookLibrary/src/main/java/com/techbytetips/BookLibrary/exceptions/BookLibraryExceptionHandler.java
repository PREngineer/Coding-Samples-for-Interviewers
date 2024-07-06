package com.techbytetips.BookLibrary.exceptions;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.ControllerAdvice;
import org.springframework.web.bind.annotation.ExceptionHandler;

// Handles all exceptions
@ControllerAdvice
public class BookLibraryExceptionHandler {
  
  /*
   * handleBookNotFoundException - Returns a proper response when a book is not found
   * @param BookNotFoundException - The exception to handle
   * @return ResponseEntity<Object> - The response
   */
  // Handle the BookNotFoundException type
  @ExceptionHandler( value = {BookNotFoundException.class} )
  public ResponseEntity<Object> handleBookNotFoundException( BookNotFoundException bookNotFoundException ){

    // Generate the payload to return
    // Include the message, cause and not found as the http status code
    BookLibraryException bookLibraryException = new BookLibraryException(
                                                      bookNotFoundException.getMessage(), 
                                                      bookNotFoundException.getCause(), 
                                                      HttpStatus.NOT_FOUND);
    // Prepare and return the response
    return new ResponseEntity<>( bookLibraryException, HttpStatus.NOT_FOUND );
  
  }

}
