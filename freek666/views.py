from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django import forms

from user_messages import api as user_messages_api


class ComposeForm(forms.Form):
    to = forms.ModelChoiceField(queryset=User.objects.all(), label="To")
    message = forms.CharField(widget=forms.Textarea, label="Message")


@login_required
def message_inbox(request):
    messages_list = user_messages_api.get_messages(request=request)
    return render(request, "user_messages/inbox.html", {"messages_list": messages_list})


@login_required
def message_compose(request):
    if request.method == "POST":
        form = ComposeForm(request.POST)
        if form.is_valid():
            user_messages_api.info(
                form.cleaned_data["to"],
                form.cleaned_data["message"],
            )
            messages.success(request, "Message sent")
            return redirect("messages_inbox")
    else:
        form = ComposeForm()
    return render(request, "user_messages/compose.html", {"form": form})

# Create your views here.
