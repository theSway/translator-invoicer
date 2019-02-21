'''Part of Invoicer'''


def show_jobs():
    month = input('It is the month of:      ')
    print('Your progress and earnings this month:\n')

    try:
        f = open('.\Jobs_{0}_2017_Customer 1.txt'.format(month), 'r')
        f_jobs = f.read().rstrip('\n')
        f_jobs = f_jobs.rsplit('\n')
        totaling = 0
        print('==========| Customer 1 |==========\n\n')
        for item in f_jobs:
            if item in ['\n', '\r\n']:
                pass
            else:
                name = item.rsplit(',')[0]
                typew = item.rsplit(',')[1]
                price = item.rsplit(',')[-1]
                totaling += float(price)
                print('{0}:             {1}             {2} EUR'.format(typew, name, price))
        print('\n\n===========================')
        print('IN TOTAL SO FAR:     {0:.2f} EUR'.format(totaling))
        print('===========================\n\n')
    except FileNotFoundError:
        print('No log of Customer 1 jobs found!')

    try:
        f = open('.\Jobs_{0}_2017_Customer 2.txt'.format(month), 'r')
        f_jobs = f.read().rstrip('\n')
        f_jobs = f_jobs.rsplit('\n')
        totaling = 0
        print('==========| Customer 2 |==========\n\n')
        for item in f_jobs:
            if item in ['\n', '\r\n']:
                pass
            else:
                name = item.rsplit(',')[0]
                type = item.rsplit(',')[1]
                price = item.rsplit(',')[-1]
                totaling += float(price)
                print('{0}:             {1}             {2} EUR'.format(type, name, price))
        print('\n\n===========================')
        print('IN TOTAL SO FAR:     {0:.2f} EUR'.format(totaling))
        print('===========================\n\n')
    except FileNotFoundError:
        print('No log of Customer 2 jobs found!')

    try:
        f = open('.\Jobs_{0}_2017_Customer 3.txt'.format(month), 'r')
        f_jobs = f.read().rstrip('\n')
        f_jobs = f_jobs.rsplit('\n')
        totaling = 0
        print('==========| Customer 3 |==========\n\n')
        for item in f_jobs:
            if item in ['\n', '\r\n']:
                pass
            else:
                name = item.rsplit(',')[0]
                type = item.rsplit(',')[1]
                price = item.rsplit(',')[-1]
                totaling += float(price)
                print('{0}:             {1}             {2} EUR'.format(type, name, price))
        print('\n\n===========================')
        print('IN TOTAL SO FAR:     {0:.2f} EUR'.format(totaling))
        print('===========================\n\n')
    except FileNotFoundError:
        print('No log of Customer 3 jobs found!')
