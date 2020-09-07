from django.shortcuts import render, redirect
from pages.models import Team
from django.contrib import messages
from .models import Contact


# Create your views here.
def contact(request):
    teams = Team.objects.all()
    data = {
        'teams': teams,
    }

    return render(request, 'pages/contact.html', data)

def inquiry(request):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        first_name = request.POST['first_name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        contact = Contact(user_id =user_id, first_name=first_name, email=email, subject=subject, message=message)

        contact.save()
        messages.success(request, "Thank you For Reaching Out, We will get Back To You Shortly.")
        return redirect('contact')
