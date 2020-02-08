from django.shortcuts import render

# Create your views here.
def post_list(request):
    return render(request, 'blog/post_list.html', {})
    
def contact(request):
    return render(request, 'blog/contact.html', {})

def aboutme(request):
    return render(request, 'blog/aboutme.html', {})    