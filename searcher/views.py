from django.shortcuts import render
from searcher.models import Vehicle

# Create your views here.
def search(request):
  results = Vehicle.find_records_where_pattern_matches('XXRCAV111111')
  return render(request, "searcher/search.html", {'vehicles': results})
