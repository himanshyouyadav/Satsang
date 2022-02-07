from django.shortcuts import render,redirect

from dashboard.models import Member
from .forms import memberForm
from django.contrib.auth.models import User
from django.core.paginator import Paginator
import os
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders


# Create your views here.


def registerMember(request):
    form = memberForm()
    if request.method == "POST":
        form = memberForm(request.POST,request.FILES)
        if form.is_valid():
            member_instance = form.save(commit=False)
            member_instance.ritwik = User.objects.get(id = request.user.id)
            member_instance.save()
            form.save_m2m()
            print("Form Saved !")
            return redirect('/dashboard')
    context = {'form':form}
    return render(request,'dashboard/member_form.html',context)


def editMember(request, pk):
    member = Member.objects.get(id=pk)
    if(request.user.id != member.ritwik.id):
        return HttpResponse("<h2>Unauthorised Access !</h2>")
    form = memberForm(instance=member ) 
    if request.method == "POST":
            print("Printing POST",request.POST)
            form = memberForm(request.POST, request.FILES, instance=member)
            if form.is_valid():
                form.save()
                print("Form Updated")
                return redirect('/dashboard')
    context = {'form' :form}
    return render (request,'dashboard/member_form.html',context)

def deleteMember(request, pk):
       member = Member.objects.get(id=pk)
       if(request.user.id != member.ritwik.id):
           return HttpResponse("<h2>Unauthorised Access !</h2>")
       member.delete()
       return redirect('/dashboard')


def render_pdf_view(request,pk):
    
    member = Member.objects.filter(id=pk).first()
    if(request.user.id != member.ritwik.id):
        return HttpResponse("<h2>Unauthorised Access !</h2>")
   
    if member is not None:
        template_path = 'dashboard/new-m-pdf.html'
        context = {'member': member}
        # Create a Django response object, and specify content_type as pdf
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="registration-details.pdf"'
        # find the template and render it.
        template = get_template(template_path)
        html = template.render(context)

        # create a pdf
        pisa_status = pisa.CreatePDF(
        html, dest=response)
        # if error then show some funy view
        if pisa_status.err:
            return HttpResponse('We had some errors <pre>' + html + '</pre>')
        
        return response
    else:
        return redirect("/dashboard")        