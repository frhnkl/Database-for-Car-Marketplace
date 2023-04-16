#
#import liblary
import csv

#create headers for car_details table
headers = ['car_id', 'brand', 'type', 'model', 'year', 'transmission', 'kilometers', 'fuel', 'engine']

#create data lists for cars table
cars_details = [
        [1, 'toyota', 'Hatchback', 'Yaris', 2016, 'AT', 98000, 'Gasoline', '1200 cc'],
        [2, 'toyota', 'Hatchback', 'Yaris', 2016, 'MT', 95000, 'Gasoline', '1200 cc'],
        [3, 'toyota', 'Hatchback', 'Yaris', 2015, 'AT', 90000, 'Gasoline', '1200 cc'],
        [4, 'toyota', 'Hatchback', 'Yaris', 2020, 'AT', 42400, 'Gasoline', '1200 cc'],
        [5, 'toyota', 'Hatchback', 'Yaris', 2019, 'MT', 60000, 'Gasoline', '1200 cc'],
        [6, 'toyota', 'SUV', 'Rush', 2009, 'MT', 140000, 'Gasoline', '1400 cc'],
        [7, 'toyota', 'SUV', 'Rush', 2016, 'AT', 100000, 'Gasoline', '1400 cc'],
        [8, 'toyota', 'SUV', 'Rush', 2016, 'MT', 135000, 'Diesel', '1400 cc'],
        [9, 'toyota', 'Sedan', 'Camry', 2008, 'AT', 120000, 'Gasoline', '2400 cc'],
        [10, 'toyota', 'Sedan', 'Camry', 1998, 'MT', 220000, 'Gasoline', '2400 cc'],
        [11, 'toyota', 'Sedan', 'Corolla', 2000, 'MT', 190000, 'Gasoline', '1800 cc'],
        [12, 'toyota', 'Sedan', 'Crown', 1994, 'AT', 145000, 'Gasoline', '1800 cc'],
        [13, 'toyota', 'SUV', 'Fortuner', 2017, 'AT', 79000, 'Gasoline', '2400 cc'],
        [14, 'toyota', 'SUV', 'Fortuner', 2020, 'AT', 45000, 'Gasoline', '2400 cc'],
        [15, 'toyota', 'SUV', 'Fortuner', 2014, 'MT', 120000, 'Diesel', '2400 cc'],
        [16, 'toyota', 'SUV', 'Fortuner', 2018, 'MT', 30000, 'Diesel', '2400 cc'],
        [17, 'toyota', 'MPV', 'Avanza', 2014, 'MT', 135000, 'Gasoline', '1200 cc'],
        [18, 'toyota', 'MPV', 'Avanza', 2006, 'MT', 220000, 'Gasoline', '1200 cc'],
        [19, 'toyota', 'MPV', 'Avanza', 2017, 'MT', 87000, 'Gasoline', '1200 cc'],
        [20, 'toyota', 'MPV', 'Avanza', 2009, 'MT', 180000, 'Gasoline', '1200 cc'],
        [21, 'toyota', 'MPV', 'Avanza', 2015, 'AT', 125000, 'Gasoline', '1200 cc'],
        [22, 'toyota', 'MPV', 'Avanza', 2015, 'MT', 115000, 'Gasoline', '1200 cc'],
        [23, 'daihatsu', 'LCGC', 'Ayla', 2017, 'MT', 76000, 'Gasoline', '1200 cc'],
        [24, 'daihatsu', 'LCGC', 'Ayla', 2017, 'AT', 30000, 'Gasoline', '1200 cc'],
        [25, 'daihatsu', 'LCGC', 'Ayla', 2016, 'AT', 98000, 'Gasoline', '1200 cc'],
        [26, 'daihatsu', 'LCGC', 'Ayla', 2018, 'MT', 54000, 'Gasoline', '1200 cc'],
        [27, 'daihatsu', 'LCGC', 'Ayla', 2019, 'AT', 22000, 'Gasoline', '1200 cc'],
        [28, 'daihatsu', 'LCGC', 'Ayla', 2015, 'MT', 87000, 'Gasoline', '1200 cc'],
        [29, 'daihatsu', 'LCGC', 'Ayla', 2015, 'MT', 110000, 'Gasoline', '1200 cc'],
        [30, 'daihatsu', 'MPV', 'Sigra', 2021, 'AT', 23000, 'Gasoline', '1200 cc'],
        [31, 'daihatsu', 'MPV', 'Sigra', 2020, 'MT', 80000, 'Gasoline', '1200 cc'],
        [32, 'daihatsu', 'MPV', 'Sigra', 2018, 'MT', 45000, 'Gasoline', '1200 cc'],
        [33, 'daihatsu', 'MPV', 'Sigra', 2019, 'AT', 35000, 'Gasoline', '1200 cc'],
        [34, 'daihatsu', 'MPV', 'Sigra', 2020, 'AT', 33000, 'Gasoline', '1200 cc'],
        [35, 'daihatsu', 'MPV', 'Xenia', 2007, 'MT', 230000, 'Gasoline', '1200 cc'],
        [36, 'daihatsu', 'MPV', 'Xenia', 2005, 'MT', 250000, 'Gasoline', '1200 cc'],
        [37, 'daihatsu', 'MPV', 'Xenia', 2012, 'MT', 140000, 'Gasoline', '1200 cc'],
        [38, 'daihatsu', 'MPV', 'Xenia', 2017, 'MT', 81000, 'Gasoline', '1200 cc'],
        [39, 'daihatsu', 'MPV', 'Xenia', 2019, 'MT', 45000, 'Gasoline', '1200 cc'],
        [40, 'honda', 'LCGC', 'Brio', 2015, 'MT', 132000, 'Gasoline', '1200 cc'],
        [41, 'honda', 'LCGC', 'Brio', 2016, 'MT', 102000, 'Gasoline', '1400 cc'],
        [42, 'honda', 'LCGC', 'Brio', 2017, 'AT', 82000, 'Gasoline', '1200 cc'],
        [43, 'honda', 'LCGC', 'Brio', 2017, 'AT', 72000, 'Gasoline', '1200 cc'],
        [44, 'honda', 'LCGC', 'Brio', 2020, 'AT', 32000, 'Gasoline', '1200 cc'],
        [45, 'honda', 'SUV', 'CR-V', 2020, 'AT', 56000, 'Gasoline', '1800 cc'],
        [46, 'honda', 'SUV', 'CR-V', 2002, 'AT', 140000, 'Gasoline', '2000 cc'],
        [47, 'honda', 'SUV', 'CR-V', 2016, 'AT', 66000, 'Gasoline', '2400 cc'],
        [48, 'honda', 'SUV', 'CR-V', 2021, 'AT', 30000, 'Gasoline', '1800 cc'],
        [49, 'honda', 'Hatchback', 'Jazz', 2016, 'AT', 77000, 'Gasoline', '1400cc'],
        [50, 'honda', 'Hatchback', 'Jazz', 2020, 'AT', 25000, 'Gasoline', '1400cc'],
        [51, 'honda', 'Hatchback', 'Civic', 2016, 'AT', 77000, 'Gasoline', '1400cc'],
        [52, 'honda', 'Sedan', 'Civic', 2020, 'AT', 47000, 'Gasoline', '1400 cc'],
        [53, 'bmw', 'Sedan', 'E30', 1992, 'MT', 142000, 'Gasoline', '1800 cc'],
        [54, 'bmw', 'Sedan', 'E30', 1990, 'MT', 132000, 'Gasoline', '1800 cc'],
        [55, 'bmw', 'Sedan', 'E30', 1991, 'MT', 152000, 'Gasoline', '1800 cc'],
        [56, 'bmw', 'Sedan', 'E36', 1996, 'MT', 102000, 'Gasoline', '1800 cc'],
        [57, 'bmw', 'Sedan', 'E36', 1997, 'MT', 112000, 'Gasoline', '2000 cc'],
        [58, 'bmw', 'Sedan', 'E36', 1998, 'MT', 142000, 'Gasoline', '2400 cc'],
        [59, 'bmw', 'Sedan', 'E46', 2001, 'AT', 114000, 'Gasoline', '2000 cc'],
        [60, 'bmw', 'Sedan', 'E46', 2001, 'AT', 102000, 'Gasoline', '1800 cc'],
        [61, 'bmw', 'Sedan', 'E46', 2002, 'AT', 98000, 'Gasoline', '1800 cc'],
        [62, 'bmw', 'Sedan', 'E30', 1991, 'MT', 120000, 'Gasoline', '1800 cc'],
        [63, 'bmw', 'Sedan', 'E36', 1990, 'MT', 114000, 'Gasoline', '1800 cc'],
        [64, 'bmw', 'Sedan', 'E30', 1990, 'MT', 60000, 'Gasoline', '1800 cc'],
        [65, 'suzuki', 'SUV', 'Jimny', 2019, 'MT', 24000, 'Gasoline', '1500 cc'],
        [66, 'suzuki', 'SUV', 'Jimny', 2019, 'AT', 14000, 'Gasoline', '1500 cc'],
        [67, 'suzuki', 'SUV', 'Jimny', 2020, 'AT', 15000, 'Gasoline', '1500 cc'],
        [68, 'suzuki', 'SUV', 'Jimny', 1996, 'MT', 144000, 'Gasoline', '1200 cc'],
        [69, 'suzuki', 'SUV', 'Jimny', 1995, 'MT', 132000, 'Gasoline', '1200 cc'],
        [70, 'suzuki', 'SUV', 'Jimny', 1995, 'MT', 120000, 'Gasoline', '1200 cc'],
        [71, 'suzuki', 'SUV', 'Jimny', 1993, 'MT', 150000, 'Gasoline', '1200 cc'],
        [72, 'suzuki', 'MPV', 'Ertiga', 2014, 'AT', 140000, 'Gasoline', '1500 cc'],
        [73, 'suzuki', 'MPV', 'Ertiga', 2018, 'AT', 80000, 'Gasoline', '1500 cc'],
        [74, 'suzuki', 'MPV', 'Ertiga', 2020, 'MT', 40000, 'Gasoline', '1500 cc'],
        [75, 'suzuki', 'Sedan', 'Baleno', 1999, 'MT', 140000, 'Gasoline', '1600 cc'],
        [76, 'suzuki', 'Sedan', 'Baleno', 2001, 'MT', 156000, 'Gasoline', '1600 cc'],
        [77, 'suzuki', 'Hatchback', 'Baleno', 2014, 'AT', 32000, 'Gasoline', '1500 cc'],
    ]

with open('cars_details.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    
    
    #write the header
    writer.writerow(headers)
    
    
    #write multiple rows
    writer.writerows(cars_details)
    
    #sql file will be created at the destination folder