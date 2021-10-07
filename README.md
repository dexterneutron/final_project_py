# Final Project
For the final project of the Bootcamp the challenge was to build a content aggregator to fetch news from:
-   [https://techcrunch.com/](https://techcrunch.com/)
-   [https://mashable.com/](https://mashable.com/)
-   [https://www.theverge.com/](https://www.theverge.com/)
## Application Architecture
![Application Architecture](https://github.com/dexterneutron/final_project_py/blob/main/docs/architecture.png)
The app is made up of two services:
### [REST API](https://github.com/dexterneutron/final_project_py/tree/main/api) :
The API has a scheduled script that runs in the background, fetching data from the sources, parsing it, and finally storing it in a MongoDB database. This database is exposed through an endpoint created with Flask.
 ### [Web App](https://github.com/dexterneutron/final_project_py/tree/main/app) :
The Web App has a scheduled script that runs in the background, fetching data from the API and storing it in a Django model, connected to a local SQLite Database. Once in the DB, the data is sent and displayed in a view.

## How to run the app:

 1. Run MongoDB database container
`docker-compose up`

 2. Create Virtual Environment
 `py -m venv env`

 3. Activate Virtual Env
`venv\Scripts\activate`

 4. Install requirements.txt
 ````pip install -r requirements.txt````

 5. Run API service
  `cd api`
  `flask run`
  
The background service will start fetching the news after 1 minute. The data is available through the API endpoint:
http://127.0.0.1:5000/api/feed

 6. Run Web App service
  `cd app`
  `python manage.py runserver --noreload`
  
The background service will start fetching and storing the data from the API after 2 minutes. The web app is available through  http://127.0.0.1:8000/reader/ 

![App Home](https://github.com/dexterneutron/final_project_py/blob/main/docs/screenshot.PNG)
