from django.shortcuts import get_object_or_404, render, HttpResponse
from blog.models import Post, another
from django.views.generic.list import ListView

from hitcount.utils import get_hitcount_model
from hitcount.views import HitCountMixin
from hitcount.models import HitCountBase
# Create your views here.

from home.models import Contact

class blogHomeListView(ListView):
    model = Post #like there model = Post
    context_object_name = 'posted'
    template_name = 'blog/blogHome.html'
    paginate_by = 2



def blogPostDetailView(request, slug):
    object = get_object_or_404(Post, slug=slug)
    context = {
        'contact':Contact.objects.all().first()
    }

    # hitcount logic
    hit_count = get_hitcount_model().objects.get_for_object(object)
    hits = hit_count.hits
    hitcontext = context['hitcount'] = {'pk': hit_count.pk}
    hit_count_response = HitCountMixin.hit_count(request, hit_count)
    if hit_count_response.hit_counted:
        hits = hits + 1
        hitcontext['hit_counted'] = hit_count_response.hit_counted
        hitcontext['hit_message'] = hit_count_response.hit_message
        hitcontext['total_hits'] = hits


    post = Post.objects.filter(slug=slug).first()
    content = another.objects.filter(name=slug)

    context.update({
    'popular_posts': Post.objects.order_by('-hit_count_generic__hits')[:2],
    'content': content, 'post': post
    })
    return render(request, 'blog/blogPost.html', context)





# def blogPost(request, slug): 
#     post = Post.objects.filter(slug=slug).first()
#     content = another.objects.filter(name=slug)
#     post.views = post.views+1
#     post.save()
#     context={'post': post, 'content': content}




# def blogHome(request): 
#     allPosts= Post.objects.all()
#     context={'allPosts': allPosts}
#     return render(request, "blog/blogHome.html", context)
#     return render(request, 'blog/blogPost.html', context)