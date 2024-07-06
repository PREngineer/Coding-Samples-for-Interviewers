package com.techbytetips.BookLibrary.Responses;

import java.util.HashMap;
import java.util.Map;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;

/*
  * BookLibraryResponseHandler - This class is responsible for the creation of the responses from the API
  */
public class BookLibraryResponseHandler {
 
  /*
   * singleBookResponse - A response for a single book request
   * @param message - The message to provide
   * @param httpStatus - The http status code
   * @param responseObject - The data to return
   * @return responseEntity - The entity representing the response
   */
  public static ResponseEntity<Object> singleBookResponse( String message, HttpStatus httpStatus, Object responseObject){

    // Populate the custom response
    Map<String,Object> response = new HashMap<>();
    response.put("message", message);
    response.put("httpStatus", httpStatus);
    response.put("book", responseObject);

    // Return the response
    return new ResponseEntity<>( response, httpStatus );

  }

  /*
   * allBooksResponse - A response for an all books request
   * @param message - The message to provide
   * @param httpStatus - The http status code
   * @param responseObject - The data to return
   * @return responseEntity - The entity representing the response
   */
  public static ResponseEntity<Object> allBooksResponse( String message, HttpStatus httpStatus, Object responseObject){

    // Populate the custom response
    Map<String,Object> response = new HashMap<>();
    response.put("message", message);
    response.put("httpStatus", httpStatus);
    response.put("books", responseObject);

    // Return the response
    return new ResponseEntity<>( response, httpStatus );

  }

  /*
   * simpleMessageResponse - A response with a simple message
   * @param message - The message to provide
   * @param httpStatus - The http status code
   * @return responseEntity - The entity representing the response
   */
  public static ResponseEntity<Object> simpleMessageResponse( String message, HttpStatus httpStatus){

    // Populate the custom response
    Map<String,Object> response = new HashMap<>();
    response.put("message", message);
    response.put("httpStatus", httpStatus);

    // Return the response
    return new ResponseEntity<>( response, httpStatus );

  }

}