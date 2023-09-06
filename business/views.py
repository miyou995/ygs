import json

from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, ListView, TemplateView
from django_htmx.http import HttpResponseClientRedirect

from .forms import MagasinModalForm
# Create your views here.
from .models import Store


def only_store_list(request):
    print('only_store_list')
    stores = Store.objects.all()
    return render(request, 'snippets/stores_list_line.html', {
        'stores': stores,
        'selected_store': stores.last(),
    })


def create_store(request):
    context = {}
    template_name = "snippets/_create_edit_store_form.html"
    form = MagasinModalForm(request.POST or None) 
    context["form"] = form
    print('THE FORM')
    if request.method == "POST" and form.is_valid(): 
        store = form.save()
        message = _("Store created successfully.")
        messages.success(request, str(message), extra_tags="toastr")
        print('YESSS DONE CREATED', store.id)
        return HttpResponse(status=204,
            headers={
                'HX-Trigger': json.dumps({
                    "closeModal": "sg_create_modal",
                    "selected_store": f"{store.id}",
                    "refresh_stores": None
                })
            }) 
    return render(request, template_name=template_name, context=context)



def delete_store(request, pk):
    context = {}
    store = get_object_or_404(Store, id=pk)
    if request.method == "POST":
        store.delete()
        messages.success(request, "Store supprimer avec succés", extra_tags="toastr")
        return redirect('business:stores_list')
    context["object"] = store
    print('TINTINTINTITN')
    response =  render(request, 'popups/delete_modal.html', context) 
    return response




def update_store(request, pk):
    context = {}
    template_name = "snippets/_create_edit_store_form.html"
    store = get_object_or_404(Store, id=pk)

    form = MagasinModalForm(request.POST or None, instance=store) 
    context["form"] = form
    print('THE store', store.id)
    if request.method == "POST" and form.is_valid(): 
        print('FORM INSTRANCEZ', form.instance)
        store = form.save()
        message = _("Store updated successfully.")
        messages.success(request, str(message), extra_tags="toastr")
        print('YESSS DONE updated', store.id)
        return HttpResponseClientRedirect(store.get_absolute_url()) 
    return render(request, template_name=template_name, context=context)

class StoreListView(ListView):
    model = Store
    template_name = "store_list.html" 
    context_object_name = "stores"

    def get_queryset(self):
        queryset = super().get_queryset().order_by('-id')
        return queryset
    def get_context_data(self, **kwargs):
        context = super(StoreListView, self).get_context_data(**kwargs)
        return context
    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        context = self.get_context_data(**kwargs)
        queryset = self.get_queryset(**kwargs)
        print('qeurys====>', queryset)
        if request.htmx:
            print('WE ARE OIN A HTMX REQUEST')
            return render(request, "snippets/_store_block.html", context)
        if queryset.count() > 1:
            return self.render_to_response(context)
        else:
            # queryset.first().get_absolute_url()
            return redirect(queryset.first().get_absolute_url())
        

class StoreDetailView(DetailView):
    model = Store
    template_name = "store_detail.html"
    def get_context_data(self, **kwargs):
        context = super(StoreDetailView, self).get_context_data(**kwargs)
        store = self.get_object()
        context["store"] = self.get_object()

        # context["outputs"] = SalesOrder.objects.filter(sender=self.get_object())
        # context["order_count"] = SalesOrder.objects.filter(sender=self.get_object()).count()
        # context["inputs"] = StockTransfer.objects.filter(receiver_depot=self.get_object())
        # context["sales_data"] = SalesOrder.objects.annotate()

        # data = (
        #     SalesOrder.objects
        #     .filter(sender=self.get_object())
        #     .annotate(month=TruncMonth('date'))  # Use the 'date' field
        #     .values('month')
        #     .annotate(count=Count('id'))  # Count orders
        #     .order_by('month')
        # )
        # context['months']= [item['month'].strftime('%b') for item in data]
        # context['counts']= [item['count'] for item in data]
        return context

