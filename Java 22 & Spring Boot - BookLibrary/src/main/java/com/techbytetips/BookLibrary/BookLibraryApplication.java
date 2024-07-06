/*
 * Project: Sample Java 22 + Spring Boot API application
 * By:      Jorge Pabón (pianistapr@hotmail.com)
 * Created: July/3/2024
 */

package com.techbytetips.BookLibrary;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

// Define our Spring Boot Application
@SpringBootApplication
public class BookLibraryApplication {

	public static void main(String[] args) {

    // Run the Book Library class as the application
		SpringApplication.run( BookLibraryApplication.class, args );

	}

}