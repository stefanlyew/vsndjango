from django.db import models
import csv
import re

class Vehicle(models.Model):
    serial_number_pattern = models.CharField(max_length=12)
    vehicle_trim_id = models.IntegerField()
    year = models.IntegerField()
    make = models.CharField(max_length=140)
    model = models.CharField(max_length=140)
    trim_name = models.CharField(max_length=300)
    regexp = models.CharField(max_length=100)
    wildcard_count = models.IntegerField()

    @classmethod
    def find_records_where_pattern_matches(self, serial_number):
      # Be paranoid and guard to validate well-formed serial
      pattern = re.compile("^[A-Z]{6}[0-9]{6}$")
      if not pattern.match(serial_number):
        return self.objects.none()

      # Format serial_number with single quotes for SQL
      snum = "'%s'" % serial_number
      # use params to guard against SQL injection
      raw_query_set = self.objects.raw("SELECT * FROM searcher_vehicle WHERE %s RLIKE searcher_vehicle.regexp", [snum])

      # Get ids to filter raw_query_set into standard query_set
      ids = []
      for record in raw_query_set:
        ids.append(record.id)

      # Order by pattern with fewer asterisks
      query_set = self.objects.filter(id__in=ids).order_by('wildcard_count')
      return query_set


class VSNDataParser:
    # Parses a CSV into Vehicle Records

    def __init__(self, file_path):
        self.file_path = file_path

    def parse(self):
        with open( self.file_path, "rb" ) as theFile:
            reader = csv.DictReader( theFile )
            for row in reader:
                row = self.__snake_case_dict(row)
                row['wildcard_count'] = self.__wildcard_count_in(row['serial_number_pattern'])
                row['regexp'] = self.__produce_regexp_from(row['serial_number_pattern'])
                v = Vehicle(**row)
                v.save()

    def __snake_case_dict(self, row):
      new_dict = {}
      for key, value in row.items():
        formatted_key = key.lower().replace(' ', '_', 6)
        new_dict[formatted_key] = value
      return new_dict

    def __wildcard_count_in(self, pattern):
      return pattern.count('*')

    def __produce_regexp_from(self, pattern):
      # Valid VSNs are in the format of six letters (A-Z)
      # followed by six numbers (0-9)
      # we will substitute wildcard characters for their possible values

      first_half, second_half = pattern[:6], pattern[7:]
      six_letters = first_half.replace('*', '[A-Z]', 6)
      six_numbers = second_half.replace('*', '[0-9]', 6)
      return six_letters + six_numbers
