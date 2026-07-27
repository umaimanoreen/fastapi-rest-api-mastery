from fastapi import FastAPI
from .models import Movie_item


app = FastAPI()
movies_list = []


@app.get("/")
def movies():
    return {"message": "hello world"}


@app.post("/movies")
def add_movies(movie: Movie_item):
    movies_list.append(movie)
    return {"message": "Movie added successfully"}


@app.get("/movies/{movie_id}")
def get_movie(movie_id: int):
    for movie in movies_list:
        if movie_id >= len(movies_list):
            return {"error": "Movie not found"}

        return movies_list[movie_id]


@app.get("/movies")
def get_movies():
    return movies_list
