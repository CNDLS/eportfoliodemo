from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django import forms

from forms import AddDocumentForm

def add(request):
	"""
	Upload a document
	"""
	
	if request.method == "POST":

		form = AddDocumentForm(request.POST, request.FILES)
		if form.is_valid():
			document = form.save(commit=False)
			document.user = request.user
			
			try:
				from pyPdf import PdfFileReader
				pdf = PdfFileReader(document.file)
				
				document.title = pdf.getDocumentInfo().title
				document.author = pdf.getDocumentInfo().author
				
			except:
				document.title = "( Insert title )"
				document.author = "( Insert author )"
				
			document.save()
			return HttpResponseRedirect('/documents/edit/' + str(document.id))
	else:
		form = AddDocumentForm()
	
	context = {
		'form': form,
	}
	return render_to_response('add.html', context,
							  context_instance=RequestContext(request))
