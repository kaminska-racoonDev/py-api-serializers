from django.urls import path, include
from rest_framework import routers
from cinema.views import (
    MovieViewSet,
    CinemaHallViewSet,
    GenreViewSet,
    ActorViewSet,
    TicketViewSet,
    OrderViewSet,
    MovieSessionViewSet,
)
# write urls here
router = routers.DefaultRouter()
router.register("movies", MovieViewSet, basename="movie")
router.register("cinema_hall", CinemaHallViewSet, basename="cinema_hall")
router.register("genres", GenreViewSet, basename="genres")
router.register("actors", ActorViewSet, basename="actors")
router.register("tickets", TicketViewSet, basename="tickets")
router.register("orders", OrderViewSet, basename="orders")
router.register("movie_sessions", MovieSessionViewSet, basename="movie_sessions")

urlpatterns = [
    path("", include(router.urls)),
]

app_name = "cinema"
