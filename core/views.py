from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from core.models import Coach

# Create your views here.

@login_required
def homepage(request):
    user = Coach.objects.filter(id_auth_user=request.user.pk)
    context = {"user": user}
    return render(request, 'core/homepage.html', context)