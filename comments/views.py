from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from .models import Comment

# Create your views here.
def comment_list(request):
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

def source(request, id):
    id = int(id)
    comment = Comment.objects.get(id=id)
    context = {'id': id, 'comment': comment}
    return render(request, "comments/comment_source.html", context=context)

import json
import logging
from django.views.decorators.csrf import csrf_protect
from django.template.loader import get_template
from django.http import HttpResponseBadRequest
from .forms import CommentForm

logger = logging.getLogger(__name__)

@csrf_protect
def ajax_comment_form(request):
    form = CommentForm(request.POST)
    if not form.is_valid():
        return HttpResponseBadRequest(json.dumps({'errors': form.errors}), content_type="application/json")

    template = get_template("comments/fragments/comment_form.html")
    comment = Comment(
        text=form.cleaned_data['comment_text'],
        created_by=request.user,
        parent=form.cleaned_data['parent_comment_id'],
    )
    html = template.render({'comment': comment}, request)
    logger.debug("Rendered comment form HTML: %s", html)
    result = {"html": html}
    return HttpResponse(json.dumps(result), content_type="application/json")
    

@csrf_protect
def ajax_add(request, save=True):
    form = CommentForm(request.POST)
    if not form.is_valid():
        return HttpResponseBadRequest(json.dumps({'errors': form.errors}), content_type="application/json")

    comment = Comment(
        text=form.cleaned_data['comment_text'],
        created_by=request.user,
        parent=form.cleaned_data['parent_comment_id'],
    )
    if save:
        comment.save()

    template = get_template("comments/fragments/comment_detail.html")
    html = template.render({'comment': comment}, request)
    result = {"html": html}
    return HttpResponse(json.dumps(result), content_type="application/json")
    # return HttpResponse(json.dumps({"html": "hello"}), content_type = "application/json")
    # return HttpResponse(json.dumps({"markdown": markdown}), content_type = "application/json")

@csrf_protect
def ajax_preview(request):
    return ajax_add(request, save=False)
