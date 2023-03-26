from blog.models import Post
from django.contrib import messages
from django.shortcuts import HttpResponse, render
from home.models import Contact


# Create your views here.
def home(request):
    post = Post.objects.all()

    return render(request, 'home/home.html')


def contact(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        selected=request.POST['contact_type']
        content =request.POST['content']

        SendContent = '''write'''
        if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<4:
            messages.error(request, "Please fill the form correctly")


        else:
            # Contact.objects.all().delete()
            contact=Contact(name=name, email=email, phone=phone, content=content, contact_type=selected)
            contact.save()
            messages.success(request, "Your message has been successfully sent")


    return render(request, "home/contact.html")


def about(request): 
    return render(request, 'home/about.html')


def search(request):
    query=request.GET['query']
    lower_Q = query.lower()
    her = ''
    search_tip = Post.objects.all()
    for SearchedTip in search_tip:
        for tag in SearchedTip.tags.all():
            print(f"{SearchedTip.title}: {tag.name.lower()}")
            if tag.name.lower() in lower_Q:
                print(True)
                SearchedTip.Is_search = True
                SearchedTip.save()  
                her = True
                print(SearchedTip.Is_search)
                break
            
            elif her == False:
                SearchedTip.Is_search = False
                SearchedTip.save()
                print(SearchedTip.Is_search)
            else:
                SearchedTip.Is_search = False
                SearchedTip.save()
                print(f"Nothing to be: {SearchedTip.Is_search}")



    searchPost = Post.objects.filter(Is_search=True)
    print(f"hello: {searchPost}")
    if len(query)>78:
        allPosts=Post.objects.none()

    elif searchPost.count()>0:
        allPosts = searchPost
        print(f"search: {allPosts}")


    else:
        allPostsTitle= Post.objects.filter(title__icontains=query)
        allPostsContent =Post.objects.filter(content__icontains=query)
        allPosts =  allPostsTitle.union(allPostsContent)
        print(f"post: {allPosts}")

    
    if allPosts.count()==0:
        messages.warning(request, "No search results found. Please refine your query.")

    params={
        'allPosts': allPosts,
        'query': query,
        }
    return render(request, 'home/search.html', params)
