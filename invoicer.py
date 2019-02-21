'''This is main of Invoice Generator for Translators by E. Turkulainen'''

import job_lister
import invoice_generator
import view_jobs


customers = ['Customer 1', 'Customer 2']


print('\nHello there! Welcome to Invoice Generator.\nIs there something specific you\'re looking'
      ' to accomplish today?\n')

k = True
while k is True:
    choice = int(input('\n1. Add a completed job\n'
                       '2. View a month\'s completed jobs and their total\n'
                       '3. Generate an invoice\n'
                       '4. Quit\n'))
    if choice == 1:
        client = input('\nAight, for whom did you work for?\n'
                       '1. Customer 1\n'
                       '2. Customer 2\n')
        job_lister.add_job(customers[int(client)-1])

    elif choice == 2:
        view_jobs.view_jobs()

    elif choice == 3:
        another = 'y'
        while another == 'y':
            number = input('\nWho owes ya?\n'
                           '1. Customer 1\n'
                           '2. Customer 2\n')
            customer = customers[int(number)-1]
            invoiceno = input('And your invoice number?\n')
            print('Gotcha!\n')
            invoice_generator.generate(customer, invoiceno)
            print('Ka-ching! Generation ready. Enjoy :)')
            another = input('Create another?\ny/n\n')
            if another == 'n':
                print('Awesome!\n')
            else:
                print('Coming right up!\n')
    elif choice == 4:
        break
    print('\nAnything else?\n')

print('\nKay, see ya next time!\n')
exit()
