from django.shortcuts import render
from django.views.generic import DetailView, ListView

from cms.utils import get_language_from_request

from .models import Car

# Create your views here.

class CarListView(ListView):
    model = Car
    queryset = Car.objects.all()

    def dispatch(self, request, *args, **kwargs):
        language = get_language_from_request(request)

        if request.toolbar.preview_mode_active or request.toolbar.edit_mode_active:
            # add unpublished pagecontent object to the toolbar
            request.toolbar.set_object(
                request.current_page.get_admin_content(language)
            )
        else:
            # add published pagecontent object to the toolbar
            request.toolbar.set_object(
                request.current_page.get_content_obj(language)
            )
        return super().dispatch(request, *args, **kwargs)


class CarDetailView(DetailView):
    model = Car
    context_object_name = "car"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # show edit button on the apphook detail page
        self.request.toolbar.set_object(self.object)
        return context


# cms edit endpoint requires this signature
def car_detail_view(request, obj):
    return CarDetailView.as_view()(request, pk=obj.pk)
