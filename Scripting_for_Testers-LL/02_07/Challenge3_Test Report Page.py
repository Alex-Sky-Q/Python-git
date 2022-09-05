import csv
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

sheet = client.open('TestRunData').sheet1

#read in the data from the spreadsheet
spreadsheet_data = sheet.get_all_values()

#   We don't need the Test Name or Average Run Time data, so we can remove those from each row using
#   del row_data[x] where x is the index of the element we want to remove
run_times = []
for row in spreadsheet_data:
    #Remove the first 2 items from the row since we are not interested in the Test Name or Avg Run time
    run_times.append(row[2:])

#read in csv data
csv_data = []
with open('LatestTestRunData.csv') as f:
    test_data = csv.reader(f)
    for row in test_data:
        csv_data.append(row[1:3])

#for the sake of simplicity we are going to assume a few things:
# 1. All of the tests in the csv data were run on the same date
# 2. The test are in the same order in the csv file as they are in the spreadsheet data

#find the run date 
#remember that we can assume that all the tests in the csv file were run on the same date
#which means we can get the run date from the 3rd column of the 2nd row in the csv data

run_date = csv_data[1][1]
#now get the first row of the run_times list and modify it to remove the oldest value
#and add in the new run date
new_data = [run_times[0][1:]]
new_data[0].append(run_date)

#similar to above, do this for each remaining row loop over the run_times and csv_data lists and for each time through the loop,
#get the new value from the csv_data and add it to the end of the run_times row
#and then remove the oldest value from that row note that you can use zip to iterate over multiple lists at the same time
for spreadsheet_row,csv_row in zip(run_times[1:],csv_data[1:]):
    row = spreadsheet_row[1:]
    row.append(csv_row[0])
    new_data.append(row)


#write the new spreadsheet data back into the spreadsheet
#don't forget that lists are indexed starting from 0 and the spreadsheet index starts at 1.  Also remember that we want to
#start writing the data in the 3rd column in the spreadsheet since the first two columns have the test name and the average run time.
#As a reminder, if you want both the value and the index of a list you can use the enumerate function
sheet_new = client.open('TestRunData-New').sheet1
for row_index, row in enumerate(new_data):
    for col_index, col in enumerate(row):
        sheet_new.update_cell(row_index+1,col_index+3,col)

#read in the average data from the spreadsheet
#Hint: use sheet.col_values
avg_data = sheet_new.col_values(2)

#intializing the chart_data list with the headers
chart_data = [["Test Name","Diff From Avg"]]

#add test names and the difference from the average for each of the test to the chart_data list
#hint: use zip again to loop over both the avg_data and the csv_data lists at the same time
test_names = sheet_new.col_values(1)
for test_name, avg, run in zip(test_names[1:], avg_data[1:], csv_data[1:]):
    chart_data.append([test_name, float(avg)-int(run[0])])

from string import Template
#first substitution is the header, the rest is the data
htmlString = Template("""<html><head><script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
<script type="text/javascript">
  google.charts.load('current', {packages: ['corechart']});
  google.charts.setOnLoadCallback(drawChart);
  
  function drawChart(){
      var data = google.visualization.arrayToDataTable([
      $labels,
      $data
      ],
      false);

      var chart = new google.visualization.ColumnChart(document.getElementById('chart_div'));
      chart.draw(data);
  }
</script>
</head>
<body>
<div id = 'chart_div' style='width:800; height:600'><div>
</body>

</html>""")

#format the data correctly
chart_data_str = ''
for row in chart_data[1:]:
    chart_data_str += '%s, \n'%row

#Substitute the data into the template
html_final = htmlString.substitute(labels=chart_data[0], data=chart_data_str)

#Write the html to a file
with open ('Chart.html', 'w') as f:
    f.write(html_final)
