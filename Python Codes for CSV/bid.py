#import liblary
import csv

#create headers for users table
#since we already know what the header, the headers wont make it to the file. it's just for a reference
headers = ['bid_id', 'car_id', 'user_id', 'bid_date', 'bid_price', 'bid_status']

#create data lists for users table
bids = [
    [1, 66, 'rangers123', '2021-03-11', 345000000, 'on'],
    [2, 66, 'kimino', '2021-04-12', 342000000, 'on'],
    [3, 66, 'bonvoyage55', '2021-05-14', 340000000, 'on'],
    [4, 66, 'salisendiri', '2021-06-16', 335000000, 'on'],
    [5, 66, 'mobilegend', '2021-07-19', 335000000, 'on'],
    [6, 66, 'empatmata', '2021-08-14', 330000000, 'on'],
    [7, 66, 'mobillegend', '2021-09-15', 327000000, 'on'],
    [8, 66, 'ishinomiyasecondhand', '2021-10-17', 326000000, 'on'],
    [9, 66, 'nierautomobile', '2021-12-01', 325000000, 'on'],
    [10, 76, 'kimino', '2021-06-01', 50000000, 'on'],
    [11, 76, 'julianto.98', '2021-07-04', 47000000, 'on'],
    [12, 76, 'junianto.95', '2021-09-01', 48000000, 'on'],
    [13, 9, 'kimino', '2022-07-01', 195000000, 'on'],
    [14, 9, 'absendulubang', '2022-08-08', 192000000, 'on'],
    [15, 9, 'carimobilmurah', '2022-09-07', 190000000, 'on'],
    [16, 9, 'bocilkematian', '2022-10-21', 185000000, 'on'],
    [17, 9, 'kimino', '2022-12-18', 197000000, 'on'],
    [18, 53, 'bocilkematian', '2021-05-18', 142000000, 'on'],
    [19, 53, 'saberbestgirl', '2021-07-12', 140000000, 'on'],
    [20, 53, 'ishinomiyasecondhand', '2021-08-11', 146000000, 'on'],
    [21, 53, 'rangers123', '2021-09-16', 150000000, 'on'],
    [22, 53, 'bonvoyage55', '2021-10-17', 152000000, 'on'],
    [23, 53, 'saberbestgirl', '2022-01-18', 160000000, 'on'],
    [24, 52, 'mugiwaramobil', '2021-12-30', 315000000, 'on'],
    [25, 52, 'balipreloved', '2022-01-18', 310000000, 'on'],
    [26, 52, 'desuexmakima', '2023-02-15', 306000000, 'on'],
    [27, 52, 'balipreloved', '2023-03-18', 304000000, 'on'],
    [28, 52, 'sotong144', '2023-04-08', 300000000, 'on'],
    [29, 1, 'kimino', '2020-04-09', 110000000, 'off'],
    [30, 1, 'sotong144', '2020-04-15', 113000000, 'off'],
    [31, 16, 'sotong144', '2023-03-15', 330000000, 'off'],
    [32, 16, 'ishinomiyasecondhand', '2023-03-19', 320000000, 'off'],
    [33, 16, 'saberbestgirl', '2023-04-01', 335000000, 'off'],
]


with open('bids.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    
    #write multiple rows
    writer.writerows(bids)
    
    #sql file will be created at the destination folder