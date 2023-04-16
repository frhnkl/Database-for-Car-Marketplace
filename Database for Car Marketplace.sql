-- this queries will be used to create a marketplace to sell car
-- some tables will be filled by datas from csv files and other tables will be filled with datas from queries
-- we start by creating needed tables by using DDL

CREATE TABLE "users" (
    "user_id" varchar(30)   NOT NULL,
    "first_name" varchar(50)   NOT NULL,
    "last_name" varchar(50)   NOT NULL,
    "city_id" int   NOT NULL,
    "phone_num" varchar(50)   NOT NULL,
    "email" varchar(50)   NOT NULL,
    CONSTRAINT "pk_user" PRIMARY KEY (
        "user_id"
     )
);

CREATE TABLE "commerce" (
    "commerce_id" serial   NOT NULL,
    "car_id" int   NOT NULL,
    "user_id" varchar(30)   NOT NULL,
    "city_id" int   NOT NULL,
    "description" text,
    "price" int   NOT NULL,
    "bid" bool   NOT NULL,
    "post_date" date   NOT NULL,
    CONSTRAINT "pk_commerce" PRIMARY KEY (
        "commerce_id"
     )
);

CREATE TABLE "car_details" (
    "car_id" serial   NOT NULL,
    "brand" varchar(50)   NOT NULL,
    "type" text   NOT NULL,
    "model" varchar(50)   NOT NULL,
    "year" int   NOT NULL,
    "transmision" text   NOT NULL,
    "kilometer" int   NOT NULL,
	"fuel_type" text,
	"engine_size" text,
    CONSTRAINT "pk_car_details" PRIMARY KEY (
        "car_id"
     )
);

CREATE TABLE "city" (
    "city_id" int   NOT NULL,
    "city_name" text   NOT NULL,
    "latitude" decimal(8,6)   NOT NULL,
    "longitude" decimal(9,6)   NOT NULL,
    CONSTRAINT "pk_city" PRIMARY KEY (
        "city_id"
     )
);

CREATE TABLE "bid" (
    "bid_id" serial   NOT NULL,
    "car_id" int   NOT NULL,
    "user_id" varchar(30)   NOT NULL,
    "bid_date" date   NOT NULL,
    "bid_price" int   NOT NULL,
    "bid_status" text   NOT NULL,
    CONSTRAINT "pk_bid" PRIMARY KEY (
        "bid_id"
     )
);

-- insert required datas into tables
-- for users, city, bid, and car_details we use import method to upload datasets from csv files
-- there is another way to add dataset into table, which is by using INSERT command
-- for Commerce table, i will use INSERT command to input the datasets

insert into commerce (user_id, car_id, city_id, description, price, bid, post_date)
values('samarindamobil', 1, 6472, 'WTS Yaris 2016 bekas dokter. kondisi interior eksterior rapih. hubungi kontak yang tersedia!!', 125000000, True, '2020-03-01'),
    ('samarindamobil', 2, 6472, 'WTS Yaris 2016 tangan pertama. cek sendiri datang ke lokasi bawa mekanik terpercayamu !', 115000000, True, '2020-03-01'),
    ('rangers123', 3, 3173, 'JUAL YARIS 2015 PEMAKAIAN PRIBADI. COD JAKARTA ONLY', 123000000, True, '2021-04-09'),
    ('bonvoyage55', 4, 3172, 'jual yaris 2020 kilometer rendah pemakaian kota. hubungi budi bondowoso +6283125963', 200000000, True, '2022-03-04' ),
    ('merkurius22', 5, 3172, 'JUAL YARIS 2019 MANUAL PEMAKAIAN KOTA. HARGA NETT !!', 150000000, False, '2022-09-08' ),
    ('sotong144', 6, 3173, 'JUAL TOYOTA RUSH PEMAKAIAN PRIBADI BUKAN BEKAS TAKSOL HARGA KARET!!', 123000000, True, '2021-04-09'),
    ('bentengtakeshi', 7, 3573, 'JUAL CEPAT TOYOTA RUSH BU HUBUNGI NUGI BY WHATSAPP +62831252297', 163000000, True, '2023-04-09'),
    ('rembrembo', 8, 1371, 'jual santai toyota rush langsung nego gan', 165000000, True, '2022-04-09'),
    ('bocilkematian', 9, 3171, 'jual camry bekas pejabat. kondisi mint perawatan apik uang negara. bisa nego cantik', 200000000, True, '2022-05-09'),
    ('setiabudi.mobil', 10, 3273, 'setiabudi mobil. mobil bekas tapi tetap berkelas demi hati pelanggan puas. info lebih lanjut hubungi anto +62228424123', 70000000, True, '2022-04-09'),
    ('setiabudi.mobil', 11, 3273, 'setiabudi mobil. mobil bekas tapi tetap berkelas demi hati pelanggan puas. info lebih lanjut hubungi anto +62228424123', 65000000, True, '2022-04-09'),
    ('setiabudi.mobil', 12, 3273, 'setiabudi mobil. mobil bekas tapi tetap berkelas demi hati pelanggan puas. info lebih lanjut hubungi anto +62228424123', 80000000, True, '2022-04-09'),
    ('setiabudi.mobil', 13, 3273, 'setiabudi mobil. mobil bekas tapi tetap berkelas demi hati pelanggan puas. info lebih lanjut hubungi anto +62228424123', 323000000, True, '2023-04-09'),
    ('setiabudi.mobil', 14, 3273, 'setiabudi mobil. mobil bekas tapi tetap berkelas demi hati pelanggan puas. info lebih lanjut hubungi anto +62228424123', 383000000, True, '2023-04-09'),
    ('rajamobil88', 15, 3273, 'raja mobil rajanya fortuner. hubungi whatsapp engkos +622156328592', 223000000, True, '2022-04-09'),
    ('rajamobil88', 16, 3273, 'raja mobil rajanya fortuner. hubungi whatsapp engkos +622156328592', 351000000, True, '2023-02-09'),
    ('mobilbekasjakarta', 17, 3174, 'anda mencari avanza untuk keluarga dengan harga miring? hubungi mobilbekasjakarta +62212512311. JAMIN BUKAN BEKAS TAKSI/TAKSOL', 180000000, True, '2023-01-09'),
    ('mobilbekasjakarta', 18, 3174, 'anda mencari avanza untuk keluarga dengan harga miring? hubungi mobilbekasjakarta +62212512311. JAMIN BUKAN BEKAS TAKSI/TAKSOL', 110000000, True, '2023-02-09'),
    ('mobilbekasjakarta', 19, 3174, 'anda mencari avanza untuk keluarga dengan harga miring? hubungi mobilbekasjakarta +62212512311. JAMIN BUKAN BEKAS TAKSI/TAKSOL', 200000000, True, '2023-03-09'),
    ('mobilbekasjakarta', 20, 3174, 'anda mencari avanza untuk keluarga dengan harga miring? hubungi mobilbekasjakarta +62212512311. JAMIN BUKAN BEKAS TAKSI/TAKSOL', 123000000, True, '2022-10-09'),
    ('mobilbekasjakarta', 21, 3174, 'anda mencari avanza untuk keluarga dengan harga miring? hubungi mobilbekasjakarta +62212512311. JAMIN BUKAN BEKAS TAKSI/TAKSOL', 153000000, True, '2022-11-09'),
    ('mobilbekasjakarta', 22, 3174, 'anda mencari avanza untuk keluarga dengan harga miring? hubungi mobilbekasjakarta +62212512311. JAMIN BUKAN BEKAS TAKSI/TAKSOL', 150000000, True, '2022-09-09'),
    ('balipreloved', 23, 5171, 'Ayla bekas pemakaian pribadi. nego cantik !', 110000000, True, '2021-04-09'),
    ('balipreloved', 24, 5171, 'ayla bekas pemakaian pribadi. open nego !', 135000000, True, '2022-04-09'),
    ('desuexmakima', 25, 5171, 'ayla plat dk bekas dokter tangan pertama pajak akur !!', 110000000, True, '2023-01-09'),
    ('samarindamobil', 26, 6472, 'SELLER TRUSTED MOKAS AREA SAMARINDA DAN SEKITARNYA HUBUNGI SAMARINDA MOBIL', 105000000, True, '2021-04-09'),
    ('samarindamobil', 27, 6472, 'SELLER TRUSTED MOKAS AREA SAMARINDA DAN SEKITARNYA HUBUNGI SAMARINDA MOBIL', 130000000, True, '2021-08-30'),
    ('samarindamobil', 28, 6472, 'SELLER TRUSTED MOKAS AREA SAMARINDA DAN SEKITARNYA HUBUNGI SAMARINDA MOBIL', 90000000, True, '2023-01-28'),
    ('mugiwaramobil', 29, 3578, 'MUGIWARA MOBIL. MOKAS BERKUALITAS DIJAMIN BISA MUTERIN GRANDLINE AND BACK', 92000000, True, '2022-09-10'),
    ('mugiwaramobil', 30, 3578, 'MUGIWARA MOBIL. MOKAS BERKUALITAS DIJAMIN BISA MUTERIN GRANDLINE AND BACK', 190000000, True, '2020-05-21'),
    ('mugiwaramobil', 31, 3578, 'MUGIWARA MOBIL. MOKAS BERKUALITAS DIJAMIN BISA MUTERIN GRANDLINE AND BACK', 170000000, True, '2020-10-08'),
    ('mugiwaramobil', 32, 3578, 'MUGIWARA MOBIL. MOKAS BERKUALITAS DIJAMIN BISA MUTERIN GRANDLINE AND BACK', 152000000, True, '2021-05-26'),
    ('konohautombile', 33, 3173, 'Penyedia mobil bekas murah untuk keluarga konoha bahagia. Daihatsu sigra bisa nego !', 190000000, True, '2021-01-28'),
    ('konohautomobile', 34, 3173, 'Penyedia mobil bekas murah untuk keluarga konoha bahagia. Daihatsu sigra bisa nego !', 195000000, True, '2022-06-10'),
    ('ishinomiyasecondhand', 35, 1371, 'CHILD COMPANY DARI ISHINOMIYA.INC. MENJUAL MOBIL BEKAS BERKUALITAS TANPA ADA DOMPET YANG TERKURAS. RAJANYA XENIA AREA PADANG !!', 95000000, True, '2021-10-07'),
    ('ishinomiyasecondhand', 36, 1371, 'CHILD COMPANY DARI ISHINOMIYA.INC. MENJUAL MOBIL BEKAS BERKUALITAS TANPA ADA DOMPET YANG TERKURAS. RAJANYA XENIA AREA PADANG !!', 98000000, True, '2021-05-20'),
    ('ishinomiyasecondhand', 37, 1371, 'CHILD COMPANY DARI ISHINOMIYA.INC. MENJUAL MOBIL BEKAS BERKUALITAS TANPA ADA DOMPET YANG TERKURAS. RAJANYA XENIA AREA PADANG !!', 102000000, True, '2021-09-30'),
    ('nierautomobile', 38, 6471, 'nierautomobile hanya menjual mobil bekas pemakaian pribadi. dijamin terawat !! XENIA murah bekas saudara !!', 133000000, True, '2022-01-21'),
    ('nierautomobile', 39, 6471, 'nierautomobile hanya menjual mobil bekas pemakaian pribadi. dijamin terawat !! XENIA murah bekas mantan istri !!', 143000000, True, '2021-05-31'),
    ('mobillegend', 40, 3175, 'jual brio bekas pemakaian pribadi. kondisi apik. harga nett no nego !!', 122000000, False, '2022-11-01'),
    ('mobillegend', 41, 3175, 'jual brio bekas pemakaian pribadi. kondisi apik. harga nett no nego !!', 130000000, False, '2021-11-28'),
    ('showroomgroovestreet', 42, 3471, 'Groove street. home ! MENJUAL MOBIL IMPIAN UNTUK WARGA LOS SANTOS DAN SEKITARNYA!! HUBUNGI C.J +6287865324913', 121000000, True, '2021-08-20'),
    ('showroomgroovestreet', 43, 3471, 'Groove street. home ! MENJUAL MOBIL IMPIAN UNTUK WARGA LOS SANTOS DAN SEKITARNYA!! HUBUNGI C.J +6287865324913', 137000000, True, '2022-12-04'),
    ('showroomgroovestreet', 44, 3471, 'Groove street. home ! MENJUAL MOBIL IMPIAN UNTUK WARGA LOS SANTOS DAN SEKITARNYA!! HUBUNGI C.J +6287865324913', 158000000, True, '2020-03-03'),
    ('showroomgroovestreet', 45, 3471, 'Groove street. home ! MENJUAL MOBIL IMPIAN UNTUK WARGA LOS SANTOS DAN SEKITARNYA!! HUBUNGI C.J +6287865324913', 275000000, True, '2021-10-04'),
    ('showroomgroovestreet', 46, 3471, 'Groove street. home ! MENJUAL MOBIL IMPIAN UNTUK WARGA LOS SANTOS DAN SEKITARNYA!! HUBUNGI C.J +6287865324913', 95000000, True, '2022-12-02'),
    ('showroomgroovestreet', 47, 3471, 'Groove street. home ! MENJUAL MOBIL IMPIAN UNTUK WARGA LOS SANTOS DAN SEKITARNYA!! HUBUNGI C.J +6287865324913', 300000000, True, '2021-08-04    '),
    ('kolektormobil', 48, 1375, 'CRV Facelift dengan perawatan ciamik kilometer rendah dan terawat', 300000000, True, '2020-12-29'),
    ('kolektormobil', 49, 1375, 'honda jazz pemakaian pribadi. owner pecinta mobil, service record dan pajak aman.', 275000000, True, '2022-11-22'),
    ('kolektormobil', 50, 1375, 'honda jazz rendah, ex-owner terkenal sebagai pecinta mobil dan youtuber otomotif. dijamin zero problem', 258000000, True, '2020-05-09'),
    ('kolektormobil', 51, 1375, 'civic hatchback 2016 bekas pemakaian dokter. service record aman dan kondisi interior mint !', 300000000, True, '2020-02-03'),
    ('kolektormobil', 52, 1375, 'civic sedan langka! kilometer rendah pemakaian dalam kota !!', 320000000, True, '2021-12-18'),
    ('kolektormobil', 53, 1375, 'MOBIL SI BOY !! E 30 FULL TERAWAT TOTAL SERVICE TERAKHIR HABIS 90 JUTA BON TERLAMPIR. NO NEGO !', 145000000, False, '2021-04-24'),
    ('sukamobilbekas', 54, 3471, 'SUKA MOBIL BEKAS RAJANYA BMW ! SEMUA BARANG DIJAMIN TERAWAT, PAJAK ON, DAN SERVICE RECORD LENGKAP !! HUBUNGI DENI +625125236246537', 70000000, True, '2020-05-23'),
    ('sukamobilbekas', 55, 3471, 'SUKA MOBIL BEKAS RAJANYA BMW ! SEMUA BARANG DIJAMIN TERAWAT, PAJAK ON, DAN SERVICE RECORD LENGKAP !! HUBUNGI DENI +625125236246537', 65000000, True, '2021-11-19'),
    ('sukamobilbekas', 56, 3471, 'SUKA MOBIL BEKAS RAJANYA BMW ! SEMUA BARANG DIJAMIN TERAWAT, PAJAK ON, DAN SERVICE RECORD LENGKAP !! HUBUNGI DENI +625125236246537', 80000000, True, '2022-07-03'),
    ('sukamobilbekas', 57, 3471, 'SUKA MOBIL BEKAS RAJANYA BMW ! SEMUA BARANG DIJAMIN TERAWAT, PAJAK ON, DAN SERVICE RECORD LENGKAP !! HUBUNGI DENI +625125236246537', 75000000, True, '2021-06-26'),
    ('sukamobilbekas', 58, 3471, 'SUKA MOBIL BEKAS RAJANYA BMW ! SEMUA BARANG DIJAMIN TERAWAT, PAJAK ON, DAN SERVICE RECORD LENGKAP !! HUBUNGI DENI +625125236246537', 85000000, True, '2021-09-09'),
    ('peterpancar', 59, 3273, 'PETERPAN CAR LORD BMW BANDUNG ! CARI BMW RETRO HANYA DI PETERPAN CAR !!', 90000000, True, '2021-02-18'),
    ('peterpancar', 60, 3273, 'PETERPAN CAR LORD BMW BANDUNG ! CARI BMW RETRO HANYA DI PETERPAN CAR !!', 95000000, True, '2023-01-21'),
    ('peterpancar', 61, 3273, 'PETERPAN CAR LORD BMW BANDUNG ! CARI BMW RETRO HANYA DI PETERPAN CAR !!', 110000000, True, '2020-05-14'),
    ('peterpancar', 62, 3273, 'PETERPAN CAR LORD BMW BANDUNG ! CARI BMW RETRO HANYA DI PETERPAN CAR !!', 70000000, True, '2020-10-09'),
    ('peterpancar', 63, 3273, 'PETERPAN CAR LORD BMW BANDUNG ! CARI BMW RETRO HANYA DI PETERPAN CAR !!', 71000000, True, '2020-12-05'),
    ('jualmobilsitamurah', 64, 6471, '', 70000000, True, '2021-12-10'),
    ('jualmobilsitamurah', 65, 6471, '', 300000000, True, '2022-12-28'),
    ('jualmobilsitamurah', 66, 6471, '', 350000000, True, '2021-03-17'),
    ('kimetsunoriba', 67, 3578, 'KOLEKTOR JIMNY ! pemakaian pribadi jimny baru barang terawat harga nett!', 400000000, False, '2020-06-23'),
    ('kimetsunoriba', 68, 3578, 'suzuki jimny jadul barang apik body interior terawat surat surat akur harga nett', 85000000, False, '2022-06-02'),
    ('salisendiri', 69, 1371, '', 75000000, True, '2022-11-15'),
    ('salisendiri', 70, 1371, '', 80000000, True, '2022-01-07'),
    ('soodoadoonrainu', 71, 6472, '', 60000000, True, '2020-09-18'),
    ('soodoadoonrainu', 72, 6472, '', 180000000, True, '2020-07-02'),
    ('julianto.98', 73, 3174, 'suzuki ertiga pemakaian pribadi. jual nett no nego', 200000000, False, '2021-12-12'),
    ('junianto.95', 74, 3174, 'suzuki ertiga no nego', 231000000, False, '2023-03-24'),
    ('kimino', 75, 3471, 'baleno klasik jual murah!!', 55000000, False, '2021-10-08'),
    ('saberbestgirl', 76, 3173, 'baleno murah !!', 52000000, False, '2021-05-17'),
    ('empatmata', 77, 1375, 'new baleno pemakain pribadi harga nett !!', 240000000, False, '2022-07-14');

-- after the tables has been created we add relations by using another DDL Command which is alter and add desired Foreign Keys

ALTER TABLE users ADD CONSTRAINT fk_city
	FOREIGN KEY(city_id)
	REFERENCES city(city_id);
	
ALTER TABLE commerce ADD CONSTRAINT fk_users
	FOREIGN KEY(user_id)
	REFERENCES users(user_id);
	
ALTER TABLE commerce ADD CONSTRAINT fk_car_details
	FOREIGN KEY(car_id)
	REFERENCES car_details(car_id);
	
ALTER TABLE commerce ADD CONSTRAINT fk_city
	FOREIGN KEY(city_id)
	REFERENCES city(city_id);
	
ALTER TABLE bid ADD CONSTRAINT fk_car_details
	FOREIGN KEY(car_id)
	REFERENCES car_details(car_id);

ALTER TABLE bid ADD CONSTRAINT fk_users
	FOREIGN KEY(user_id)
	REFERENCES users(user_id);
	
-- we've created a database !
