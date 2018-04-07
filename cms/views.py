from django.shortcuts import render
from django.http import HttpResponse
from .models import Pages

# Create your views here.

def look_pages(request,identificador):
	try:
		pag = Pages.objects.get(name = identificador)
		ans = pag.page
	except Pages.DoesNotExist:
		ans = "No hay datos en la base de datos"
	return HttpResponse(ans)

def list_pages(request):
	ans = "Lista de páginas: <br/>"
	pages_list = Pages.objects.all()
	for pg in pages_list:
		ans += pg.name + ' es ' + str(pg.page)+"<br/>"
	return HttpResponse(ans)