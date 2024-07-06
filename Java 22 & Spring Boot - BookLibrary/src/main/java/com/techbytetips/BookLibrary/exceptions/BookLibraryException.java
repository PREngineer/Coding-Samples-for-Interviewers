package com.techbytetips.BookLibrary.exceptions;

import org.springframework.http.HttpStatus;

public class BookLibraryException {
  
  /*
   * Class Attributes
   */
  private final String message;
  private final Throwable throwable;
  private final HttpStatus httpStatus;

  /*
   * BookException - Constructor
   * @param message - The message to return
   * @param throwable - The cause of this exception
   * @param httpStatus - The HTTP status code
   */
  public BookLibraryException(String message, Throwable throwable, HttpStatus httpStatus) {
    this.message = message;
    this.throwable = throwable;
    this.httpStatus = httpStatus;
  }

  /*
   * getMessage - Retrieves the exception's message
   * @return String - The message
   */
  public String getMessage() {
    return message;
  }

  /*
   * getThrowable - Retrieves the exception's cause
   * @return Throwable - The cause
   */
  public Throwable getThrowable() {
    return throwable;
  }

  /*
   * getHttpStatus - Retrieves the exception's HTTP status code
   * @return HTTPStatus - The HTTP status code
   */
  public HttpStatus getHttpStatus() {
    return httpStatus;
  }  

}
