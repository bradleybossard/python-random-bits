import random

articles = ['A good day to die',
            'Investing for the future',
            'Time is money',
            'Becoming a Fireman',
            'Magic as a hobby',
            'US Stock Report 2016'
           ]

with open('input.txt', 'w') as f:
    for article in articles:
        f.write("Article: %s \n" % article)
        f.write("Requests: %d \n" % (random.random() * 20000))
        f.write("bytes served: %d \n" % (random.random() * 1000000))
        f.write("\n")

