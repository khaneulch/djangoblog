from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.utils import timezone
from django.views import generic
from django.views.generic import View
from .models import Post
from  .forms import UserForm

class post_list(generic.ListView):
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.all()


class post_detail(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

class post_new(CreateView):
    model = Post
    fields = ['author','title','text','published_date','upload_img']

class post_edit(UpdateView):
    model = Post
    fields = ['author','title','text','published_date','upload_img']

class post_delete(DeleteView):
    model = Post
    success_url = reverse_lazy('blog:post_list')

class UserFormView(View):
    form_class = UserForm
    template_name = 'blog/registration_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:
                    login(request, user)
                    return redirect('blog:post_list')

        return render(request, self.template_name, {'form':form})

# def post_list(request):
#     posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
#     return render(request, 'blog/post_list.html', {'posts' : posts})
#
# def post_detail(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     return render(request, 'blog/post_detail.html', {'post' : post})
#
# class post_new(CreateView):
#     model = Post
#     fields = ['author','title','text','created_date','published_date','upload_img']












