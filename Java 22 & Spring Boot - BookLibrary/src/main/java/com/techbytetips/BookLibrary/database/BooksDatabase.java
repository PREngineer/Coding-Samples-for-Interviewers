package com.techbytetips.BookLibrary.database;

import org.springframework.data.jpa.repository.JpaRepository;

import com.techbytetips.BookLibrary.models.Book;

public interface BooksDatabase extends JpaRepository<Book,String>{
}