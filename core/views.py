from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import TemplateView, ListView , DetailView, CreateView
from django.views.generic.edit import FormView
from django.http import JsonResponse
from business import translation
from business.models import Contact, Quote, Hiring, Slide, About
from config import settings 
from core.models import Service
from business.forms import ContactForm, QuoteForm, HiringForm
from django.shortcuts import redirect
# from django.utils.translation import LANGUAGE_SESSION_KEY
from django.shortcuts import redirect
from django.utils.translation import activate
from django.conf import settings
from django.shortcuts import redirect
from django.utils.translation import activate
from django.conf import settings
from django.views.decorators.cache import never_cache




############### INDEX ###############
class IndexView(TemplateView):
    def get_template_names(self):
        if self.request.LANGUAGE_CODE == 'ar':
            return ['rtl/index.html']
        else:
            return ['index.html']
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context["services"] =Service.objects.all()
        context["slide"] =Slide.objects.last()
        return context

############### ABOUT ###############
class AboutView(TemplateView):
    def get_template_names(self):
        if self.request.LANGUAGE_CODE == 'ar':
            return ['rtl/about.html']
        else:
            return ['about.html']
    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        context["abouts"] =About.objects.all()
        return context

############### SERVICES ###############
##### LIST
class ServiceView(ListView):
    def get_template_names(self):
        if self.request.LANGUAGE_CODE == 'ar':
            return ['rtl/services.html']
        else:
            return ['services.html']
    model = Service
    context_object_name ="services"
##### DETAIL
class ServiceDetail(DetailView):
    model = Service
    def get_template_names(self):
        if self.request.LANGUAGE_CODE == 'ar':
            return ['rtl/services_detail.html']
        else:
            return ['services_detail.html']
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["services"] =Service.objects.all()
        return context

############### CONTACT ###############
class ContactView(SuccessMessageMixin, FormView):
    def get_template_names(self):
        if self.request.LANGUAGE_CODE == 'ar':
            return ['rtl/contact.html']
        else:
            return ['contact.html']
    form_class= ContactForm
    model = Contact 
    success_message = "Votre message a été envoyé avec succès, Un agent vous contactera prochainement avec un appel téléphonique ou un e-mail."
    success_url = reverse_lazy('core:contact')
    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)
        context["services"] =Service.objects.all()
        return context
############### QUOTE ###############
class QuoteoView(SuccessMessageMixin, CreateView):
    def get_template_names(self):
        if self.request.LANGUAGE_CODE == 'ar':
            return ['rtl/quote.html']
        else:
            return ['quote.html']
    form_class= QuoteForm
    model = Quote 
    success_message = "Un agent vous contactera prochainement avec un appel téléphonique ou un e-mail contenant les informations demandées."
    success_url = reverse_lazy('business:quote')
    def get_context_data(self, **kwargs):
        context = super(QuoteoView, self).get_context_data(**kwargs)
        context["services"] =Service.objects.all()
        return context
   
############### HIRING ###############
class RecruitingView(SuccessMessageMixin, CreateView):
    def get_template_names(self):
        if self.request.LANGUAGE_CODE == 'ar':
            return ['rtl/hiring.html']
        else:
            return ['hiring.html']
    form_class= HiringForm
    model = Hiring 
    success_message = "Votre demande a été soumise, Un agent vous contactera prochainement avec un appel téléphonique ou un e-mail." 
    success_url = reverse_lazy('core:hiring')




from django.shortcuts import render

# def contact(request, language):
#     template_name = f'contact_{language}.html'
#     return render(request, template_name)

# def hiring(request, language):
#     template_name = f'hiring_{language}.html'
#     return render(request, template_name)
# def index(request, language):
#     template_name = f'index_{language}.html'
#     return render(request, template_name)
# def about(request, language):
#     template_name = f'about_{language}.html'
#     return render(request, template_name)
# def services(request, language):
#     template_name = f'services_{language}.html'
#     return render(request, template_name)
# @never_cache
# def switch_language(request):
#     if request.method == 'POST':
#         selected_language = request.POST.get('language')
#         print(f"Selected Language: {selected_language}")
#         request.session['language'] = selected_language
#     return redirect(request.META.get('HTTP_REFERER'))






