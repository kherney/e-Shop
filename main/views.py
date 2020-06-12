# from django.shortcuts import render
# from django.http import HttpResponseRedirect
from main import forms
from django.views.generic.edit import FormView


class ContactUsView(FormView):
    template_name = "contact_us.html"
    form_class = forms.ContactForm
    success_url = '/'

    def form_valid(self, form):
        """If the form is valid, redirect to the supplied URL."""
        form.send_mail()
        return super(ContactUsView, self).form_valid(form)

# def contact_us(request):
#     if request.method == "POST":
#         form = forms.ContactForm(request.POST)
#         if form.is_valid():
#             form.send_mail()
#             return HttpResponseRedirect('/')
#     else:
#         form = forms.ContactForm()
#     return render(request, 'contact_us.html', {'form': form})
