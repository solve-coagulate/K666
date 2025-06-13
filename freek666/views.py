from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django import forms

from . import message_utils


class ComposeForm(forms.Form):
    to = forms.ModelChoiceField(queryset=User.objects.all(), label="To")
    message = forms.CharField(widget=forms.Textarea, label="Message")


@login_required
def message_inbox(request):
    messages_list = message_utils.inbox_for(request.user)
    return render(request, "user_messages/inbox.html", {"messages_list": messages_list})


@login_required
def message_compose(request):
    if request.method == "POST":
        form = ComposeForm(request.POST)
        if form.is_valid():
            message_utils.send_message(
                sender=request.user,
                recipient=form.cleaned_data["to"],
                body=form.cleaned_data["message"],
            )
            messages.success(request, "Message sent")
            return redirect("messages_inbox")
    else:
        form = ComposeForm()
    return render(request, "user_messages/compose.html", {"form": form})


@login_required
def profile(request):
    return render(request, "profile.html")

# Create your views here.
