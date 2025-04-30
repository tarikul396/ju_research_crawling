from django.shortcuts import render, get_object_or_404
import requests
from .models import Teacher

def author_search(request):
  papers = []
  if request.method == 'POST':
    author_name = request.POST.get('author_name')
        
    url = "https://api.semanticscholar.org/graph/v1/paper/search"
    params = {
      "query": author_name,
      "fields": "title,authors,year,url,abstract",
      "limit": 25
    }
        
    response = requests.get(url, params=params)
    if response.status_code == 200:
      papers = response.json().get("data", [])
    
  return render(request, 'jurc/teacher_search.html', {'papers': papers})


def teacher_list(request):
  teachers = Teacher.objects.all()
  return render(request, 'jurc/teacher_list.html', {'teachers': teachers})