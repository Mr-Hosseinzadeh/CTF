# Use the official PHP image from the Docker Hub
FROM php:7.4-apache

# Copy the PHP source code to the Apache document root
COPY index.php flag.txt uploads /var/www/html/

# Expose port 80 to be able to access the web server
EXPOSE 80
