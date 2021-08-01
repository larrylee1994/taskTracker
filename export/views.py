from django.http import FileResponse
from main.models import Worksheet
import xlsxwriter
import io
from storefront.settings import DELIMITER as D

# Create your views here.


def excelreport(request):

    buffer = io.BytesIO()
    workbook = xlsxwriter.Workbook(buffer)
    worksheet = workbook.add_worksheet()

    # Get current ws id from session

    ws_id = request.session.get('ws', None)
    ws = Worksheet.objects.get(id=ws_id)
    ws_name = ws.user.first_name
    ws_date = ws.date

    entries = []

    # Format Worksheet toString into list of lists

    for element in ws.entry_set.all():
        string = str(element)
        result = list(string.split(D))
        entries.append(result)

    titles = [
        'Name',
        'Day',
        'Store',
        'Operation',
        'Start Time',
        'End Time',
    ]

    # Start from the first column, Write titles
    col = 0
    row = 0

    for element in titles:
        worksheet.write(row, col, element)
        col += 1

    # Start from the second row.
    row = 1
    col = 0

    # Iterate over the data and write it out row by row.
    for day, store, task, start, end in (entries):
        worksheet.write(row, col,     ws_name)
        worksheet.write(row, col + 1, day)
        worksheet.write(row, col + 2, store)
        worksheet.write(row, col + 3, task)
        worksheet.write(row, col + 4, start)
        worksheet.write(row, col + 5, end)
        row += 1

    workbook.close()
    buffer.seek(0)

    return FileResponse(buffer, as_attachment=True, filename=f'{ws_date}-{ws_name}-{ws_id}.xlsx')
