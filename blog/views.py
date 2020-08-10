from django.views import generic
from .models import Post


# Create your views here.
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    context_object_name = 'post_list'


class PostDetail(generic.DetailView):
    template_name = 'post_detail.html'
    model = Post
    context_object_name = 'post'
