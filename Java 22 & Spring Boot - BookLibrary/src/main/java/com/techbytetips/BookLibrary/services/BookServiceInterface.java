package com.techbytetips.BookLibrary.services;

import java.util.List;

import com.techbytetips.BookLibrary.models.Book;

public interface BookServiceInterface {
  
  /*
   * Define the methods for the service
   */
  public String createBook( Book book );
  public String updateBook( Book book );
  public String deleteBook( String ID );
  public Book getBook( String ID );
  public List<Book> getAllBooks();

}