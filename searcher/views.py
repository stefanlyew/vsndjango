from django.shortcuts import render
from searcher.models import Vehicle
import re

def search(request):
  if request.GET:
    query = request.GET['q']
    if not Vehicle.validate(query):
      return render(request, "searcher/search.html", {'errors': 'Invalid Serial Number Format' })

    results = Vehicle.find_records_where_pattern_matches(query)
    return render(request, "searcher/search.html", {'vehicles': results, 'searched': True})
  return render(request, "searcher/search.html", {})

def handler404(request):
    response = render_to_response('404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response

def handler500(request):
    response = render_to_response('500.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response
