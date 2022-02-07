from unicodedata import name
from django.contrib import admin
from django.urls import include, path
from . import views


urlpatterns = [
    path('member_register',views.registerMember,name="member_register"),
    path ('edit_member/<str:pk>',views.editMember,name="edit_member"),
    path ('delete_member/<str:pk>',views.deleteMember,name="delete_member"),
    path('member_pdf/<str:pk>',views.render_pdf_view,name="member_pdf")
]