import os
import tempfile
import openpyxl


def write(data):
    workbook = openpyxl.Workbook()
    worksheet = workbook.active

    # Move every provided row and append it to worksheet
    for row in data:
        worksheet.append(row)

    # Using temporary file save generated workbook and then return stream
    with tempfile.NamedTemporaryFile(delete=False) as temp:
        workbook.save(temp.name)
        temp_content = temp.read()

        # Close temporary file and remove it
        temp.close()
        os.unlink(temp.name)

        return temp_content
