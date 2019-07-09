from django.shortcuts import redirect

class AnonymousRequired:
    page_url = None
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(self.page_url)
        return super().dispatch(request, *args, **kwargs)
