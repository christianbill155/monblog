-- SQL Implementation of Django Models
-- This file creates the database schema with exact same names as Python models

-- User table (quoted because User is a reserved keyword)
CREATE TABLE "User" (
    id SERIAL PRIMARY KEY,
    username VARCHAR(150) NOT NULL,
    email VARCHAR(254) UNIQUE NOT NULL,
    password VARCHAR(128) NOT NULL
);

-- Profile table
CREATE TABLE "Profile" (
    id SERIAL PRIMARY KEY,
    bio TEXT,
    avatar VARCHAR(100), -- upload_to='avatars/' max_length=100
    user_id INTEGER UNIQUE NOT NULL,
    FOREIGN KEY (user_id) REFERENCES "User"(id) ON DELETE CASCADE
);

-- Category table
CREATE TABLE "Category" (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

-- Tag table
CREATE TABLE "Tag" (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL
);

-- Product table
CREATE TABLE "Product" (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT NOT NULL,
    price DECIMAL(8,2) NOT NULL,
    stock INTEGER NOT NULL,
    available BOOLEAN DEFAULT TRUE,
    date_of_added TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Article table
CREATE TABLE "Article" (
    id SERIAL PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    content TEXT NOT NULL,
    published_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    author_id INTEGER NOT NULL,
    category_id INTEGER,
    FOREIGN KEY (author_id) REFERENCES "User"(id) ON DELETE CASCADE,
    FOREIGN KEY (category_id) REFERENCES "Category"(id) ON DELETE SET NULL
);

-- Comment table
CREATE TABLE "Comment" (
    id SERIAL PRIMARY KEY,
    text TEXT NOT NULL,
    author VARCHAR(100) NOT NULL,
    created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    article_id INTEGER NOT NULL,
    FOREIGN KEY (article_id) REFERENCES "Article"(id) ON DELETE CASCADE
);

-- Article-Tag many-to-many relationship table (implicit through table)
CREATE TABLE "Article_tags" (
    id SERIAL PRIMARY KEY,
    article_id INTEGER NOT NULL,
    tag_id INTEGER NOT NULL,
    FOREIGN KEY (article_id) REFERENCES "Article"(id) ON DELETE CASCADE,
    FOREIGN KEY (tag_id) REFERENCES "Tag"(id) ON DELETE CASCADE
);

-- Create indexes for better performance
CREATE INDEX "User_email_index" ON "User"(email);
CREATE INDEX "Article_author_id_index" ON "Article"(author_id);
CREATE INDEX "Article_category_id_index" ON "Article"(category_id);
CREATE INDEX "Article_published_date_index" ON "Article"(published_date);
CREATE INDEX "Comment_article_id_index" ON "Comment"(article_id);
CREATE INDEX "Product_available_index" ON "Product"(available);
CREATE INDEX "Product_price_index" ON "Product"(price);
CREATE INDEX "Article_tags_article_id_index" ON "Article_tags"(article_id);
CREATE INDEX "Article_tags_tag_id_index" ON "Article_tags"(tag_id);

-- Insert sample data for Categories
INSERT INTO "Category" (name) VALUES 
('Technology'),
('Science'),
('Business'),
('Health'),
('Entertainment');

-- Insert sample data for Tags
INSERT INTO "Tag" (name) VALUES 
('python'),
('django'),
('web development'),
('data science'),
('machine learning'),
('beginner'),
('advanced');