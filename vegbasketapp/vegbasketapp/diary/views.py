from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from vegbasketapp.content.models import VeggieSailorEntry
from .models import Visit
from captcha.fields import ReCaptchaField

#from 

from django import forms
class VisitForm(forms.Form):
    visit_date = forms.DateTimeField()
    captcha = ReCaptchaField()
    
@login_required
def visit(request, entry_id):
    entry = VeggieSailorEntry.objects.get(id=entry_id)
    
    if request.POST:
        form = VisitForm(request.POST)
        if form.is_valid():
            visit = Visit()
            visit.user = request.user
            visit.visit_timestamp = form.cleaned_data['visit_date']
            visit.entry = entry
            visit.save()
            return HttpResponseRedirect(reverse("entry_slug",args=[entry.slug,]))
    else:
        form = VisitForm()
    return render(request, "diary/visit.html", {'entry':entry, 'form':form})