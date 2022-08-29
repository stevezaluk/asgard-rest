# asgard-rest
Simple, easy, file sharing and organization 

# Requirements
* [asgard-sdk](https://github.com/stevezaluk/asgard-sdk)
* flask
* flask-restx
* argparse

# Namespaces

* "file" namespace - This namespace holds all endpoints relating to creating, and retrieving file metadata. This includes the "/section" endpoint, which allows you to retreieve section data.

### GET /section/{section_name}
### GET /section

section_name - The name of the section you want

Query String Args:
  key (str) - Only return the value of a key from the JSON model
  limit (int) - The limit how many results you recieve 
  sort (str) - Sort the data on response time [alpha, desc]

Description: Returns a AsgardSection model

### GET /file/{section_name}/{query}
### GET /file/{query}
### POST /file/{section_name}/{query}

section_name - The name of the AsgardSection you want to limit your search to
query - Either a file_name or SHA-256 hash

Query String Args:
  key (str) - Only return the value of a key from the JSON model
  plex (bool) - Return metadata stored in plex. This generates on response-time and is not stored in mongoDB.
  
Description: Retrieves a single file. Can be any of the asgard models, depending on the section and what your retrieving.

### GET /index/{section_name}
### GET /index

section_name - The name of the section you want

Query String Args:
  key (str) - Only return the value of a key from the JSON model
  limit (int) - The limit how many results you recieve 
  sort (str) - Sort the data on response time [alpha, desc]

Description: Returns a dict with the results and the total count
Ex Resp: {"index":[...], "total_count":0}

### GET /search/{section_name}
### GET /search

section_name - The name of the section you want

Query String Args:
  q (str) [Required] - The file you are searching for. Searches by file name
  key (str) - Only return the value of a key from the JSON model
  limit (int) - The limit how many results you recieve 
  sort (str) - Sort the data on response time [alpha, desc]

Description: Returns a dict with the results and the total count
Ex Resp: {"search":[...], "total_count":0}


* "analytics" namespace - This namespace holds the endpoints relating to your analytic data and your show case items. You can manage your popular, most recent, etc items with the endpoints in this namespace. You can also generate analytic data based on your plex user's viewing habits


* "ux" namespace - This holds all the endpoints for the User Interface that runs on the endpoint "/dashboard/home"

### /dashboard/home - Your home page. Contains general statistics, and overview of downloading and uploading rates. Because... well... content is #1.
### /dashboard/files - View, download, and lightly (file_name only) search your files. You can limit by section here and view file metadata.
### /dashboard/sections - View, manage, and create sections here.
### /dashboard/upload - You can upload your files here.
### /dashboard/analytics - The analytics homepage
### /dashboard/vpkg - The package manager for hosted software on asgard
### /dashboard/docs - Swagger Documentation

# UI/UX

If you choose to you can manage your entire asgard server with the admin page. This page runs on "/dashboard/home". The data is generate by in-line python code right in the html files. Flask than accepts these as Jinja templates and renders the page. 
