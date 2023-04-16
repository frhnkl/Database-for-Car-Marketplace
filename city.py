#
#import liblary
import csv

#create headers for city table
headers = ['city_id', 'city_name', 'latitude', 'longitude']

#create data lists for city table
#insert required data including latitude and longitude coordinates
city = [
    [3171, 'Kota Jakarta Pusat', -6.186486, 106.834091],
    [3172, 'Kota Jakarta Utara', -6.121435, 106.774124],
    [3173, 'Kota Jakarta Barat', -6.1352, 106.813301],
    [3174, 'Kota Jakarta Selatan', -6.300641, 106.814095],
    [3175, 'Kota Jakarta Timur', -6.264451, 106.895859],
    [3573, 'Kota Malang', -7.981894, 112.626503],
    [3578, 'Kota Surabaya', -7.289166, 112.734398],
    [3471, 'Kota Yogyakarta', -7.797224, 110.368797],
    [3273, 'Kota Bandung', -6.9147444, 107.6098111],
    [1371, 'Kota Padang', -0.95, 100.3530556],
    [1375, 'Kota Bukittinggi', -0.3055556, 100.3691667],
    [6471, 'Kota Balikpapan', -1.2635389, 116.8278833],
    [6472, 'Kota Samarinda', -0.502183, 117.153801],
    [7371, 'Kota Makassar', -5.1333333, 119.4166667],
    [5171, 'Kota Denpasar', -8.65629, 115.222099],
]
with open('city.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    
    
    #write the header
    writer.writerow(headers)
    
    
    #write multiple rows
    writer.writerows(city)
    
    #sql file will be created at the destination folder