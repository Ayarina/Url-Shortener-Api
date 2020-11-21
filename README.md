# URL Beheader
Hito 1 de Ingeniería Web. (No voy a poner milestone porque me suena a piedra del Minecraft)

## Requierements
  * An interpreter/shell/terminal of any distribution that supports python (Pycharm can be also used)
  * Install all the requierements.txt in the terminal

## How it works
This API shortens URLs introduced by the user thanks to FastAPI's functions.

To run the app, we will use `uvicorn main:app --reload` (main refers to the file's .py name). Then, navigate to `http://localhost:8000` or `http://127.0.0.1:8000` (if this does not work, in the terminal it is specified where the API is being hosted).

By adding `/docs` at the end of the URL, the Swagger interface will show up. The Swagger interface (wich is very easy and intuitive to use) let us try all the functions http methods available in the API.

This API consists in a pattern of `POST` and `GET` of URLs that gets stored in a temporary database, and dies when the app stops. The function of the temporary database is to not have more than one URL assignated to the same custom name, or more than one custom name asiggnated to the same URL. 

If a non-temporary database is added, it will be more efficient. However, this will not be added to this API, only to mantain his didactic function.

### Small Warning
>>>   This API IS NOT SUITED for a large quantities of URLs, we do not want, wherever the API is being hosted, to do 800 for iterations. It is bad for your health.

😎
