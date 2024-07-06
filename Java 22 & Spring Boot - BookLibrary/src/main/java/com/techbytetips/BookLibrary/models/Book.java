package com.techbytetips.BookLibrary.models;

import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import jakarta.persistence.Table;

/*
 * Book - Represents a Book object.
 */
// Specify this is a database Entity
@Entity
// Specify on which database table it will be stored (create it if not existing)
@Table( name="books" )
public class Book {

  /*---------------- Properties ----------------*/ 

  // Specify which field is the ID in the database
  @Id
  private String id;
  private String title;
  private String authorFirstName;
  private String authorLastName;
  private String publisher;
  private String publicationDate;
  private String isbn;
  private String language;
  private String series;
  private String seriesNumber;
  private String synopsis;

  /*---------------- Constructor Methods ----------------*/ 

  /*
   * Book - Empty Constructor
   */
  public Book(){    
  }

  /*
   * Book - Full Constructor
   * 
   * @param id - The book's id
   * @param title - The book's title
   * @param authorFirstName - The author's first name
   * @param authorLastName - The author's last name
   * @param publisher - The name of the publisher
   * @param publicationDate - The date the book was published
   * @param isbn - The book's identification number
   * @param language - The book's language
   * @param series - The series' name
   * @param seriesNumber - The number of the book in the series
   * @param synopsis - A summary of the plot
   */
  public Book( String id, String title, String authorFirstName, String authorLastName, String publisher, String publicationDate, String isbn, String language, String series, String seriesNumber, String synopsis ){
    this.id               = id;
    this.title            = title;
    this.authorFirstName  = authorFirstName;
    this.authorLastName   = authorLastName;
    this.publisher        = publisher;
    this.publicationDate  = publicationDate;
    this.isbn             = isbn;
    this.language         = language;
    this.series           = series;
    this.seriesNumber     = seriesNumber;
    this.synopsis         = synopsis;
  }

  /*---------------- Get & Set Methods ----------------*/

  /*
   * getID - Retrieves the book's ID
   * @return String - The book's ID
   */
  public String getID(){
    return this.id;
  }
  /*
   * setID - Sets the book's ID
   * 
   * @param value
   */
  public void setID( String value ){
    this.id = value;
  }
  
  /*
   * getTitle - Retrieves the book's title
   * @return String - The book's title
   */
  public String getTitle(){
    return this.title;
  }
  /*
   * setTitle - Sets the book's title
   * 
   * @param value
   */
  public void setTitle( String value ){
    this.title = value;
  }

  /*
   * getAuthorFirstName - Retrieves the author's first name
   * @return String - The author's first name
   */
  public String getAuthorFirstName(){
    return this.authorFirstName;
  }
  /*
   * setAuthorFirstName - Sets the author's first name
   * 
   * @param value
   */
  public void setAuthorFirstName(String value ){
    this.authorFirstName = value;
  }
  /*
   * getAuthorLastName - Retrieves the author's last name
   * @return String - The author's last name
   */
  public String getAuthorLastName(){
    return this.authorLastName;
  }
  /*
   * setAuthorLastName - Sets the author's last name
   * 
   * @param value
   */
  public void setAuthorLastName(String value ){
    this.authorLastName = value;
  }
  /*
   * getPublisher - Retrieves the book's publisher
   * @return String - The book's publisher
   */
  public String getPublisher(){
    return this.publisher;
  }
  /*
   * setPublisher - Sets the book's publisher
   * 
   * @param value
   */
  public void setPublisher(String value ){
    this.publisher = value;
  }
  /*
   * getPublicationDate - Retrieves the book's publication date
   * @return String - The book's publication date
   */
  public String getPublicationDate(){
    return this.publicationDate;
  }
  /*
   * setPublicationDate - Sets the book's publication date
   * 
   * @param value
   */
  public void setPublicationDate(String value ){
    this.publicationDate = value;
  }
  /*
   * getISBN - Retrieves the book's ISBN
   * @return String - The book's ISBN
   */
  public String getISBN(){
    return this.isbn;
  }
  /*
   * setISBN - Sets the book's ISBN
   * 
   * @param value
   */
  public void setISBN(String value ){
    this.isbn = value;
  }
  /*
   * getLanguage - Retrieves the book's language
   * @return String - The book's language
   */
  public String getLanguage(){
    return this.language;
  }
  /*
   * setLanguage - Sets the book's language
   * 
   * @param value
   */
  public void setLanguage(String value ){
    this.language = value;
  }
  /*
   * getSeries - Retrieves the book's series
   * @return String - The book's series
   */
  public String getSeries(){
    return this.series;
  }
  /*
   * setSeries - Sets the book's series
   * 
   * @param value
   */
  public void setSeries(String value ){
    this.series = value;
  }
  /*
   * getSeriesNumber - Retrieve the number of the book in the series
   * @return String - The book's number in the series
   */
  public String get(){
    return this.seriesNumber;
  }
  /*
   * setSeriesNumber - Sets the book's number in the series
   * 
   * @param value
   */
  public void setSeriesNumber(String value ){
    this.seriesNumber = value;
  }
  /*
   * getSynopsis - Retrieves the book's synopsis
   * @return String - The book's synopsis
   */
  public String getSynopsis(){
    return this.synopsis;
  }
  /*
   * setSynopsis - Sets the book's synopsis
   * 
   * @param value
   */
  public void setSynopsis(String value ){
    this.synopsis = value;
  }

  /*---------------- Other Methods ----------------*/

  

}