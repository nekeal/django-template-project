from django.urls import include, path

app_name = "accounts"

urlpatterns = [
    path(r"", include("djoser.urls")),
]
