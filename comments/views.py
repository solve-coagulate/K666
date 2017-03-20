from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from .models import Comment

# Create your views here.
def list(request):
    return render(request, "comments/comment_list.html", context = {
        'comments': Comment.objects.order_by('-id').all().select_related().filter(parent=None),
        })

def story_list(request):
    return render(request, "stories/story_list.html", context= {
        'comments': Comment.objects.order_by('-id').all().select_related().filter(parent=None),
        })        

def story_detail(request, id):
    id = int(id)
    comment = Comment.objects.get(id=id)
    context = {'id': id, 'comment': comment}
    return render(request, "stories/story_detail.html", context=context)

def detail(request, id):
    id = int(id)
    comment = Comment.objects.get(id=id)
    context = {'id': id, 'comment': comment}
    return render(request, "comments/comment_detail.html", context=context)

def add(request):    
    data = request.POST
    if not request.method == "POST":
        data = request.GET
        # return HttpResponseRedirect(reverse("comment-list"))
        
    preview = True
    if request.method == "POST" and "post" in data.keys():
        preview = False
        # return preview(request)

    text = ""
    if "comment_text" in data.keys():
        text = data['comment_text']
    user = request.user
    
    parent = None
    if "comment_parent_id" in data.keys() and data["comment_parent_id"]:
        comment_parent_id = int(data["comment_parent_id"])
        parent = Comment.objects.get(id=comment_parent_id)

    comment = Comment(text=text, created_by=user, parent=parent)
    if not preview:
        comment.save()        
        if not parent:        
            return HttpResponseRedirect(reverse("story-detail", kwargs={"id": comment.id}))
        if not parent.parent:
            return HttpResponseRedirect(reverse("story-detail", kwargs={"id": parent.id}))
        return HttpResponseRedirect(reverse("comment-detail", kwargs={"id": parent.id}))

    return render(request, "comments/comment_preview.html", context = {
        'comment': comment,
        })
    # return HttpResponseRedirect(request.META["HTTP_REFERER"] + "#comment-%s" % comment.id)

def reply(request, id):
    id = int(id)
    parent = Comment.objects.get(id=id)
    user = request.user
    text = ""
    comment = Comment(text=text, created_by=user, parent=parent)
    return render(request, "comments/comment_preview.html", context = {
        'comment': comment,
	    'require_preview': True,
        })

import json
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import get_template

@csrf_exempt
def ajax_comment_form(request):
    template = get_template("comments/fragments/comment_form.html");
    text = request.POST['comment_text']
    user = request.user
    parent = None
    if "parent_comment_id" in request.POST.keys() and request.POST["parent_comment_id"] and request.POST["parent_comment_id"]!="None":
        parent_comment_id = int(request.POST["parent_comment_id"])
        parent = Comment.objects.get(id=parent_comment_id)

    comment = Comment(text=text, created_by=user, parent=parent)
    context = {'comment': comment}
    html = template.render(context, request)

    result = {"html": html, }
    print("HTML: ", html)
    return HttpResponse(json.dumps(result), content_type = "application/json")
    

@csrf_exempt
def ajax_add(request, save=True):

    text = request.POST['comment_text']
    user = request.user
    parent = None
    if "parent_comment_id" in request.POST.keys() and request.POST["parent_comment_id"] and request.POST["parent_comment_id"]!="None":
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
