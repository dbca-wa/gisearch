from django.shortcuts import render
import xml.etree.ElementTree as ET

def Search(request):
	#request info
	if request.method == 'GET':
		query = request.GET.get('q')

		#loading and parsing xml
		root = ET.parse('menu_3.0.xml').getroot()
		xmlstring = ET.tostring(root, encoding='utf8').decode('utf8')
		lines = xmlstring.split('\n')
		
		# variables to be passed to the template
		results = True
		data = []

		#if the search bar contains a string
		if query is not None:
			for element in lines:
				#lowering the strings prevents case sensitivity issues
				if query.lower() in element.lower():
					#add matching items
					data.append(element)
					results = True
		else:
			#populates the page with unfiltered entries
			data=lines

		#check the number of results
		if len(data) < 1:
			results = False

		#render template
		context = {'content' :data, 'results' : results}
		return render(request, 'app/search.html', context)