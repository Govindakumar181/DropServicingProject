from django.shortcuts import render


from contact.models import Contact

def index(request):


    if request.method == "POST":
        email = request.POST["email"]
        name = request.POST["name"]
        message = request.POST["message"]
        new_contact = Contact()
        new_contact.name = name
        new_contact.message = message
        new_contact.email = email
        
        new_contact.save()



    return render(request, 'index.html',{})