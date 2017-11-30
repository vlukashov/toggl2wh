#!/usr/bin/env python3

import sys
import csv

if __name__ == '__main__':
  if (len(sys.argv) == 1):
    print('Usage: toggl2wh.py [toggle-detailed-report.csv] > wh.txt')
  else:
    with open(sys.argv[1]) as csvfile:
      projects = {}
      entries = []

      reader = csv.reader(csvfile, delimiter=',', quotechar='"')
      next(reader) # skip the headers row

      open_date = ''
      for row in reader:
        projects[row[3]] = True
        this_date = row[7]
        if this_date != open_date:
          open_date = this_date
          entries += [
            '',
            '{}.{}.'.format(this_date[8:], this_date[5:7]),
            '----'
          ]
        
        start_time = '{}{}'.format(row[8][0:2], row[8][3:5])
        end_time = '{}{}'.format(row[10][0:2], row[10][3:5])
        entries.append('{}-{}: {}: {}'.format(start_time, end_time, row[3], row[5]))

      print('# format=sami')
      print('# PROJECT MAP START')
      print('')

      for project in projects.keys():
        print('{}=,5,3'.format(project))

      print('')
      for entry in entries:
        print(entry)
