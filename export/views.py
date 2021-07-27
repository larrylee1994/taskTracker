from django.shortcuts import render
from django.http import FileResponse
import io
import xlsxwriter
from main.models import Worksheet
import json

# Create your views here.


def excelreport(request):

    buffer = io.BytesIO()
    workbook = xlsxwriter.Workbook(buffer)
    worksheet = workbook.add_worksheet()

    categories = [
        'Start Time',
        'Task',
        'Store',
        'End Time',
    ]

    # Get string representation of list of dict
    ws = request.session.get('ws', None)

    # Convert string to list of dict object
    ws1 = json.loads(ws)
    print(ws1)

    # Get object id
    ws_id = ws1[0]['pk']
    ws_name = ws1[0]['fields']['name']
    ws_date = ws1[0]['fields']['date']
    ws = Worksheet.objects.get(id=ws_id)

    entries = []

    # Format Worksheet toString into list of lists
    for element in ws.entry_set.all():
        string = str(element)
        result = list(string.split(" "))
        entries.append(result)

    # Start from the first column, Write titles
    col = 0

    for element in categories:
        worksheet.write(0, col, element)
        col += 1

    # Start from the second row.
    row = 1
    col = 0

    # Iterate over the data and write it out row by row.
    for start, task, store, end in (entries):
        worksheet.write(row, col,     start)
        worksheet.write(row, col + 1, task)
        worksheet.write(row, col + 2, store)
        worksheet.write(row, col + 3, end)
        row += 1


    workbook.close()
    buffer.seek(0)

    return FileResponse(buffer, as_attachment=True, filename=f'{ws_date}-{ws_name}-{ws_id}.xlsx')