from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
# Create your views here.

posts = [
    {
        "id": 1,
        "title": "Let's explore Python",
        "content": "Python is an interpreted, high-level, general-purpose programming language. Widely used in web development, data science, and machine learning."
    },
    {
        "id": 2,
        "title": "Django for Web Development",
        "content": "Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. It follows the 'Don't Repeat Yourself' principle."
    },
    {
        "id": 3,
        "title": "Machine Learning Basics",
        "content": "Machine learning is a subset of artificial intelligence that enables computers to learn from data without explicit programming."
    },
    {
        "id": 4,
        "title": "REST APIs with Django Rest Framework",
        "content": "Django Rest Framework (DRF) is a powerful and flexible toolkit for building Web APIs in Django applications."
    },
    {
        "id": 5,
        "title": "Understanding Databases in Django",
        "content": "Django supports various databases like PostgreSQL, MySQL, and SQLite. The ORM allows easy interaction with the database using Python code."
    }
]

def home(request):
    # return HttpResponse("Hello, World!")

    html = ""
    for post in posts:
        html += f'''
            <div>
            <a href="/post/{post["id"]}">
                <h2>{post["id"]} - {post["title"]}</h2> </a>
                <p>{post["content"]}</p>
            </div>
        '''

    return render(request, "posts/home.html", { "posts": posts })

def post_detail(request, id):

    for post in posts:
        valid_id = False
        if post["id"] == id:
            post_dict = post
            valid_id = True
            break
    if valid_id:
        html = f'''
            <div>
                <h2>{post_dict["id"]} - {post_dict["title"]}</h2>
                <p>{post_dict["content"]}</p>
            </div>
        '''
        return render(request, "posts/post.html", { "post_dict": post_dict })
    else:
        return HttpResponseNotFound("Post not found")
    

def post_redirect(request, id):
    url = reverse("post", args=[id])
    return HttpResponseRedirect(url)
    
def google(request):
    return HttpResponseRedirect("https://www.google.com")
