#! /usr/bin/awk -f
#
# Usage:
# $ ./toggl2wh.awk toggl-export.csv > wh.txt

BEGIN {
  FS = ","
  open_date = ""
}
NR > 1 {
  this_date = $8
  if (this_date != open_date) {
    open_date = this_date
    printf("\n%s.%s.\n----\n", substr(this_date, 9, 2), substr(this_date, 6, 2))
  }
  start_time = substr($9, 1, 2) substr($9, 4, 2)
  end_time = substr($11, 1, 2) substr($11, 4, 2)
  print start_time "-" end_time ": " $4 ": " $6
}
