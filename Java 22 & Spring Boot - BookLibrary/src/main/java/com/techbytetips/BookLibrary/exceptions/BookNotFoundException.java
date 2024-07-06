package com.techbytetips.BookLibrary.exceptions;

public class BookNotFoundException extends RuntimeException {
  
  /*
   * BookNotFoundException - Constructor
   * @param message - The exception message
   */
  public BookNotFoundException( String message ){
    super( message );
  }

  /*
   * BookNotFoundException - Constructor with throwable cause
   * @param message - The exception message
   * @param cause - The exception cause
   */
  public BookNotFoundException( String message, Throwable cause ){
    super( message, cause );
  }



}