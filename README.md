## About
This is a project made for the course 'Web Technologies' at FH Campus Wien by:

- Florian Panek
- Navdeep Singh
- Anastasiya Urusova
- Hugo Hernán Vergara Vásquez

## Aim of the project
'Find The Way' is a website that provides users in Vienna a list of nearest public transport stations upon receiving their location. The website is consumable by desktop and mobile devices via the address http://findtheway.geokhugo.com/.

## Used technology
#### Front end:
- HTML5, CSS, JavaScript
- Tailwind CSS, daisyUI
- AJAX, GET, POST, PUT, DELETE
- Google Maps JavaScript API

#### Back end:
- Python
- Flask
- Wiener Linien API
- Data provided as JSON

## Functionality
- To use the service, users need to register an account using the corresponding option on the front page
- When logged in, users are presented with the option to choose a radius which will be used for finding nearest public transport stations
- A list of stations is loaded asynchronously when a button is pressed; stations are sorted by distance to user's location in ascending order
- Location sharing must be enabled in browser for data to be retrieved
- Users can manage their account data from the account dashboard - changing of first and last name, email address, or password is possible
- Users can delete their account, which will be then removed from the database
