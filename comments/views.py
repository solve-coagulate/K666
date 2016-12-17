from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from .models import Comment

# Create your views here.
def list(request):
    return render(request, "comments/comment_list.html", context = {
        'comments': Comment.objects.order_by('-id').all().select_related().filter(parent=None),
        })

def detail(request, id):
    id = int(id)
    comment = Comment.objects.get(id=id)
    context = {'id': id, 'comment': comment}
    return render(request, "comments/comment_detail.html", context=context)

def preview(request):
    text = request.POST['comment_text']
    user = request.user
    
    parent = None
    if "parent_comment_id" in request.POST.keys():
        parent_comment_id = int(request.POST["parent_comment_id"])
        parent = Comments.objects.get(id=parent_comment_id)

    comment = Comment(text=text, created_by=user, parent=parent)

    return render(request, "comments/comment_preview.html", context = {
        'comment': comment,
        })

def add(request):    
    data = request.POST
    if not request.method == "POST":
        return HttpResponseRedirect(reverse("comment-list"))
        
    if "preview" in data.keys():
        return preview(request)

    text = request.POST['comment_text']
        
    # attached_type = request.POST['attached_type']
    # attached_id = request.POST['attached_id']
    
    # attach_to = None
    # if attached_type and attached_id:
    #     ct = ContentType.objects.get(model=attached_type)
    #     attach_to = ct.get_object_for_this_type(id=attached_id)

    user = request.user
    
    # if not user.is_authenticated():
    #     user, created = User.objects.get_or_create(username='anonymous')

    # ip_address=get_client_ip(request)
    
    # if is_anonymous(user) and not check_captcha(request):
    #     return HttpResponse("Oh dear! You failed the captcha! Try going back, copy and pasting and reloading the page and then replying to the comment you wanted to, but get your captcha right!")

    parent = None
    if "parent_comment_id" in request.POST.keys():
        parent_comment_id = int(request.POST["parent_comment_id"])
        parent = Comments.objects.get(id=parent_comment_id)

    comment = Comment(text=text, created_by=user, parent=parent)
    comment.save()

    return HttpResponseRedirect(reverse("comment-detail", kwargs={"id": comment.id}))
    # return HttpResponseRedirect(request.META["HTTP_REFERER"] + "#comment-%s" % comment.id)

def reply(request, id):
    id = int(id)
    parent = Comment.objects.get(id=id)
    user = request.user
    text = ""
    comment = Comment(text=text, created_by=user, parent=parent)
    return render(request, "comments/comment_preview.html", context = {
        'comment': comment,
        })


import json
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import get_template

@csrf_exempt
def ajax_add(request, save=True):

    text = request.POST['comment_text']
    user = request.user
    parent = None
    if "parent_comment_id" in request.POST.keys() and request.POST["parent_comment_id"]:
        parent_comment_id = int(request.POST["parent_comment_id"])
        parent = Comment.objects.get(id=parent_comment_id)

    comment = Comment(text=text, created_by=user, parent=parent)
    if save:
        comment.save()

    template = get_template("comments/fragments/comment_detail.html")
    context = {'comment': comment}
    html = template.render(context, request)

    result = {"html": html, }
    return HttpResponse(json.dumps(result), content_type = "application/json")
    # return HttpResponse(json.dumps({"html": "hello"}), content_type = "application/json")
    # return HttpResponse(json.dumps({"markdown": markdown}), content_type = "application/json")

@csrf_exempt
def ajax_preview(request):
    return ajax_add(request, save=False)