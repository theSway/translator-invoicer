'''
Part of Invoicer: Invoice Generator for Translators

Author: Esa Turkulainen
Date: 16th March 2017

Takes client name and invoice number to be generated. Creates an xlsx file with formatting. Reads data from job list
created by joblister.
'''

import xlsxwriter as xcel
from datetime import datetime, timedelta
import pasreadertest as pas


def generate(customer, invoiceno):
    month = input('Month?\n')
    year = input('Year?\n')
    if customer != 'Customer 1':
        f = open('.\Jobs_{0}_{1}_{2}.txt'.format(month, year, customer), 'r')
        jobs_string = f.read()
        jobs_list = jobs_string.rsplit('\n')
        del jobs_list[-1]
        f.close()

    '''Date from PC clock'''

    now = datetime.now()
    invoice_due = now + timedelta(days=30)

    '''Create File'''

    invoice = xcel.Workbook('Invoice for {0} {2} - {1}.xlsx'.format(month, customer, year))
    sheet = invoice.add_worksheet()


    '''Set needed formatting'''

    font = invoice.add_format({'font_size': 8})
    Treb_bold = invoice.add_format({'bold': True, 'font_size': 8, 'font_name': 'Trebuchet MS'})
    center = invoice.add_format({'align': 'center', 'font_size': 8, 'font_name': 'Trebuchet MS'})
    centeredbold = invoice.add_format({'bold': True, 'align': 'center', 'valign': 'center', 'font_size': 8, 'font_name': 'Trebuchet MS'})
    titlecells = invoice.add_format({'bold': True, 'align': 'center', 'valign': 'bottom', 'bg_color': '#B1D4F3', 'font_size': 8, 'font_name': 'Trebuchet MS'})
    jobcells = invoice.add_format({'bold': False, 'align': 'center', 'valign': 'center', 'font_size': 8, 'font_name': 'Trebuchet MS', 'bg_color': '#D1E5F6'})
    totalcell = invoice.add_format({'bold': True, 'align': 'center', 'valign': 'center', 'font_size': 8, 'font_name': 'Trebuchet MS', 'bg_color': '#B1D4F3'})

    if customer == 'AIT':
        sheet.set_column('A:A', 15)
        sheet.set_column('B:B', 30)
        sheet.set_column('D:D', 10)
        sheet.set_column('E:E', 10)
        sheet.set_column('C:C', 10)
        sheet.set_column('E:E', 20)
    else:
        sheet.set_column('A:A', 30)
        sheet.set_column('B:B', 15)
        sheet.set_column('D:D', 20)
        sheet.set_column('E:E', 10)
        sheet.set_column('C:C', 14)
        sheet.set_column('E:E', 20)

    '''Upper left corner: Provider info'''

    sheet.write('A1', 'SERVICE PROVIDER', Treb_bold)
    sheet.write('A2', 'ADDRESS', Treb_bold)
    sheet.write('A3', 'PHONE', Treb_bold)
    sheet.write('A4', 'EMAIL', Treb_bold)
    sheet.write('A5', 'VAT', Treb_bold)
    sheet.write('B1', 'Forename Surname', font)
    sheet.write('B2', 'Provider Address', font)
    sheet.write('B3', 'Provider Number', font)
    sheet.write('B4', 'Provider Email', font)
    sheet.write('B5', 'Tax status', font)
    sheet.write('B6', 'Explanation of tax status', font)

    '''Upper right corner: Payment details'''

    sheet.write('E1', 'INVOICE NO.', Treb_bold)
    sheet.write('E2', 'DATE', Treb_bold)
    sheet.write('E3', 'PAYMENT VIA', Treb_bold)
    sheet.write('F1', '{0}'.format(invoiceno), font)
    sheet.write('F2', '{0}/{1}/{2}'.format(now.day, now.month, now.year), font)
    
    # Modify these as per your needs, for example
    if customer == 'Customer 1':
        sheet.write('F3', 'Wire Transfer or SEPA', font)
        sheet.write('E4', 'IBAN', Treb_bold)
        sheet.write('F4', 'Provider IBAN', font)
        sheet.write('E5', 'BANK NAME', Treb_bold)
        sheet.write('F5', 'Provider Bank', font)
        sheet.write('E6', 'BIC/SWIFT', Treb_bold)
        sheet.write('F6', 'Provider Bank BIC/SWIFT', font)

    if customer == 'Customer 2':
        sheet.write('F3', 'Paypal', font)
        sheet.write('E4', 'PAYPAL ADDR.', Treb_bold)
        sheet.write('F4', 'Provider Paypal', font)

    if customer == 'Customer 3':
        sheet.write('F3', 'Paypal', font)
        sheet.write('E4', 'PAYPAL ADDR.', Treb_bold)
        sheet.write('F4', 'Provider Paypal', font)

    '''Jobs and projects'''
    if customer == 'Customer 1':
        sheet.write('B10', 'PROJECT ID', titlecells)
        sheet.write('C10', 'LINE TOTAL', titlecells)
        i = 11
        projects, prices = pas.convert_pdf_to_txt('./PAS/{0} {1}.pdf'.format(month, year))
        summa = sum(prices)

        for proj, price in zip(projects, prices):
            sheet.write('B{0}'.format(i), '{0}'.format(proj), jobcells)
            sheet.write('C{0}'.format(i), '{0} €'.format(price), jobcells)

            i += 1

    else:
        sheet.write('A10', 'PROJECT ID', titlecells)
        sheet.write('B10', 'DESCRIPTION', titlecells)
        sheet.write('C10', 'LANGUAGE', titlecells)
        sheet.write('D10', 'UNIT RATE', titlecells)
        sheet.write('E10', 'UNITS', titlecells)
        sheet.write('F10', 'LINE TOTAL', titlecells)

        i = 11
        summa = 0

        for job in jobs_list:
            if job in ['\n', '\r\n']:
                pass
            else:
                job = job.rstrip('\n')
                id = job.rsplit(',')[0]
                descr = job.rsplit(',')[1]
                langpair = job.rsplit(',')[2]
                pricing = job.rsplit(',')[3]
                units = job.rsplit(',')[4]
                total = job.rsplit(',')[5]

                summa += float(total)

                if pricing == 'HOURLY':
                    unitrate = 'xx EUR per hour'
                    sheet.write('F{0}'.format(i), '{0} €'.format(total), jobcells)
                else:
                    sheet.write('F{0}'.format(i), '{0} €'.format(total), jobcells)
                    if descr == 'TRANSLATION':
                        unitrate = '0.xx EUR per word'
                    else:
                        unitrate = '0.xx EUR per word'

                sheet.write('A{0}'.format(i), '{0}'.format(id), jobcells)
                sheet.write('B{0}'.format(i), '{0}'.format(descr), jobcells)
                sheet.write('C{0}'.format(i), '{0}'.format(langpair), jobcells)
                sheet.write('D{0}'.format(i), '{0}'.format(unitrate), jobcells)
                sheet.write('E{0}'.format(i), '{0}'.format(units), jobcells)

            i += 1

    '''Payment due and total'''
    if customer == 'Customer 1':
        sheet.write('A{0}'.format(i + 2), 'PAYMENT TERMS', centeredbold)
        sheet.write('A{0}'.format(i + 3), 'PAYMENT DUE', centeredbold)
        sheet.write('B{0}'.format(i + 2), 'Full payment 30 days after final invoice date', font)
        sheet.write('B{0}'.format(i + 3), '{0}/{1}/{2}'.format(invoice_due.day, invoice_due.month, invoice_due.year),
                    font)
        sheet.write('C{0}'.format(i + 2), '{0:.2f} €'.format(summa), totalcell)
        sheet.write('C{0}'.format(i), '{0:.2f} €'.format(summa), font)
        sheet.write('C{0}'.format(i + 1), 'n/a', font)
        sheet.write('D{0}'.format(i), 'SUBTOTAL', Treb_bold)
        sheet.write('D{0}'.format(i + 1), 'TAX', Treb_bold)
        sheet.write('D{0}'.format(i + 2), 'TOTAL', Treb_bold)
    else:
        sheet.write('A{0}'.format(i + 2), 'PAYMENT TERMS', centeredbold)
        sheet.write('A{0}'.format(i + 3), 'PAYMENT DUE', centeredbold)
        sheet.write('B{0}'.format(i + 2), 'Full payment 30 days after final invoice date', font)
        sheet.write('B{0}'.format(i + 3), '{0}/{1}/{2}'.format(invoice_due.day, invoice_due.month, invoice_due.year),
                    font)
        sheet.write('F{0}'.format(i), '{0:.2f} €'.format(summa), font)
        sheet.write('F{0}'.format(i + 1), 'n/a', font)
        sheet.write('F{0}'.format(i + 2), '{0:.2f} €'.format(summa), totalcell)
        sheet.write('G{0}'.format(i), 'SUBTOTAL', Treb_bold)
        sheet.write('G{0}'.format(i + 1), 'TAX', Treb_bold)
        sheet.write('G{0}'.format(i + 2), 'TOTAL', Treb_bold)

    '''Customer details in the footer'''

    sheet.write('A{0}'.format(i+5), 'CUSTOMER DETAILS', centeredbold)
    if customer == 'Customer 1':
        sheet.write('B{0}'.format(i+5), 'Address Line 1', font)
        sheet.write('B{0}'.format(i+6), 'Address Line 2', font)
        sheet.write('B{0}'.format(i+7), 'Address Line 3', font)
        sheet.write('B{0}'.format(i+8), 'Address Line 4', font)
        sheet.write('B{0}'.format(i+9), 'Address Line 5', font)

    if customer == 'Customer 2':
        sheet.write('B{0}'.format(i + 5), 'Address Line 1', font)

    invoice.close()
