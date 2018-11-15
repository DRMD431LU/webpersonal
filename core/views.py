from django.shortcuts import render,HttpResponse

# Create your views here.
html_base = """
<h1> Mi web personal </h1>
<ul>
	<li><a href="/">Portada</a></li>
	<li><a href="/about-me/">Acerca de</a></li>
	<li><a href="/portfolio/">Portfolio</a></li>
	<li><a href="/contact/">Contacto</a></li>
</ul>
"""
def home(request):
	return HttpResponse(html_base + """
		<h2 Portada </h2>
		<p>Esto es la portada</p>
		""")

def about(request):
	return HttpResponse(html_base+"""
		<h2>Acerca de: </h2>
		<p>perro >:v</p>
		""")

def portfolio(request):
	return HttpResponse(html_base +"""
		<h2 Portafolio</h2>
		<p>Trabajos :D</p>
		""")

def contact(request):
	return HttpResponse(html_base+"""
		<h2>Contact </h2>
		<p>prueba de contacto</p>
		""")

