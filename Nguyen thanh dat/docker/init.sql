CREATE DATABASE book_store;

USE book_store;

CREATE TABLE book (
    book_id INT PRIMARY KEY AUTO_INCREMENT,
    book_type VARCHAR(255) NOT NULL,
    book_author VARCHAR(255) NOT NULL,
    book_name VARCHAR(255) NOT NULL
);

INSERT INTO book (book_type, book_author, book_name)
VALUES ('Fiction', 'Author 1', 'Book 1'),
       ('Non-Fiction', 'Author 2', 'Book 2'),
       ('Mystery', 'Author 3', 'Book 3');
