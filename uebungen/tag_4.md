# Übungen Tag 4

- Login required
- Userpassestest
- OPtional: noch einen Test schreiben

### Login Required als Klasse

    from django.contrib.auth.mixins import LoginRequiredMixin

    class EventCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):


### Login Required als Funktions-Decorator

    from django.contrib.auth.decorators import login_required

    @login_required
    def event_create(request):


### User Passes Test als Klasse

    from django.contrib.auth.mixins import UserPassesTestMixin
    class UserIsOwner(UserPassesTestMixin):
        def test_func(self):
            return self.get_object().author == self.request.user

    class EventUpdateView(UserIsOwner, UpdateView):

### in funktionsbasierten Views ist das eine Möglichkeit, zu prüfen, ob Author == User

    @login_required
    def event_update(request, pk):
        event = get_object_or_404(Event, pk=pk)
    
        if event.author != request.user:
            return HttpResponseForbidden("Du bist nicht der Besitzer dieses Events.")
    
    

