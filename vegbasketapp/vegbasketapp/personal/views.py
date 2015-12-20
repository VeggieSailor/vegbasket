from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required, user_passes_test

from vegbasketapp.personal.forms import UsernameSetupForm


def check_user_first_time(user):
    """First time predicate.
    """
    return user.userprofile.first_time

@login_required
@user_passes_test(check_user_first_time, '/p/', None)
def accounts_setup(request):
    """Configure the first time account.
    """
    if request.method == 'POST':
        form = UsernameSetupForm(request.POST, instance=request.user)
        if form.is_valid():
            username = form.clean_username()
            request.user.username = username
            request.user.save()
            request.user.userprofile.first_time = False
            request.user.userprofile.save()
            return HttpResponseRedirect('/p/')     
    else:
        form = UsernameSetupForm()
    return render(request, "accounts_setup.html", {"form":form})


@login_required
def personal(request):
    """Personal page after login view.
    """
    return render(request, "personal.html")
    