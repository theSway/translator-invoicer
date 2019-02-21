import os.path


def add_job(customer):
    acceptable_inputs = ['y', 'Y', 'n', 'N']
    yes = ['y', 'Y']
    pairs = ['ENG-FIN', 'FIN-ENG']
    service = ['TRANSLATION', 'REVIEW']
    rate = ['HOURLY', 'WORDS']
    month = input('Month\n')
    year = input('Year\n')
    if os.path.isfile('.\Jobs_{0}_{1}_{2}.txt'.format(month, year, customer)) is True:
        f = open('.\Jobs_{0}_{1}_{2}.txt'.format(month, year, customer), 'a')
        print('OK, I will append the existing file!\n')
    else:
        f = open('.\Jobs_{0}_{1}_{2}.txt'.format(month, year, customer), 'w+')
        print('Seems like this is the first job of the month for this client!\n')
    c = 'y'
    while c in yes:
        mode = input('Select mode of input: g for guided and m for manual!\n')
        while mode != 'g' and mode != 'm':
            mode = input('Sorry, I didn\'t quite catch that, guided (g) or manual (m)?\n')

        if mode == 'g' and customer == 'Customer 1':
            name = input('PROJECT ID: ')
            wtype = int(input('1. TRANSLATION\n'
                              'or\n'
                              '2. REVIEW\n'))
            langs = int(input('1. ENG-FIN\n'
                              'or\n'
                              '2. FIN-ENG\n'))
            units = int(input('1. HOURLY\n'
                              'or\n'
                              '2. WORD COUNT\n'))
            if units == 1:
                hours = float(input('How many hours?\n'))
                total = hours*28
                f.write('{0},{1},{2},{3},{4},{5}\n'.format(name, service[wtype-1], pairs[langs-1], rate[units-1], hours, total))
            else:
                words = float(input('How many words?\n'))
                total = float(input('How much did you get, in Euros? Format: NN.NN\n'))
                f.write('{0},{1},{2},{3},{4},{5}\n'.format(name, service[wtype-1], pairs[langs-1], rate[units-1], words, total))
        
        # Some customers can be set to have a quick profile
        elif mode == 'g' and customer == 'Customer 2':
            name = input('PROJECT ID: ')
            quick_prompt = input('Apply Quick Profile? y/n?\n')
            while quick_prompt not in acceptable_inputs:
                quick_prompt = input('Sorry, what? y/n?\n')

            if quick_prompt in yes:
                wtype = 1
                langs = 1
                units = 2
                words = float(input('How many words?\n'))
                total = words*0.08
                print('You earned {0} from this project.'.format(total))
                f.write('{0},{1},{2},{3},{4},{5}\n'.format(name, service[wtype - 1], pairs[langs - 1], rate[units - 1],
                                                           words, total))
            else:
                wtype = int(input('1. TRANSLATION\n'
                                  'or\n'
                                  '2. REVIEW\n'))
                langs = int(input('1. ENG-FIN\n'
                                  'or\n'
                                  '2. FIN-ENG\n'))
                units = int(input('1. HOURLY\n'
                                  'or\n'
                                  '2. WORD COUNT\n'))
                if units == 1:
                    hours = float(input('How many hours?\n'))
                    total = hours*28
                    f.write('{0},{1},{2},{3},{4},{5}\n'.format(name, service[wtype-1], pairs[langs-1], rate[units-1], hours, total))
                else:
                    words = float(input('How many words?\n'))
                    total = float(input('How much did you get, in Euros? Format: NN.NN\n'))
                    f.write('{0},{1},{2},{3},{4},{5}\n'.format(name, service[wtype-1], pairs[langs-1], rate[units-1], words, total))

        else:
            data = input('Input as: name,type,pair,rateunit,units,total\n')
            f.write(data+'\n')

        c = input('Thanks! Another? y/n\n')
        while c not in acceptable_inputs:
            c = input('Sorry, what? y/n?\n')

    print('\nTill next time!\n\n###############################')
    f.close()
