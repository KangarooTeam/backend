from django.shortcuts import render, render_to_response

def error404():
    request = 404
    """return (
        "<title>Страница не найдена </title>"
        "<h1>Упс что то пошло не так</h1>"
        "<h2>404</h2>"
        "<p>Страница не найдена</p>"
    )"""
    return render(request, "errors/404.html")