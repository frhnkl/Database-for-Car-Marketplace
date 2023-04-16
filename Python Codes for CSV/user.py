#
#import liblary
import csv

#create headers for users table
#since we already know what the header, the headers wont make it to the file. it's just for a reference
headers = ['user_id', 'first_name', 'last_name', 'city_id', 'phone_num', 'email']

#create data lists for users table
users = [
    ['rangers123', 'alif', 'hakim', 3173, '+62821115632', 'a.hakim44@gmail.com', ],
    ['bonvoyage55', 'budi', 'bondowoso', 3172, '+6283125963', 'a.bonvoyage55@gmail.com'],
    ['merkurius22', 'bani', 'iskandar', 3172, '+62831252263', 'a.merkurius]@gmail.com'],
    ['sotong144', 'herman', 'william', 3173, '+628312544342', 'a.sotong@gmail.com'],
    ['bentengtakeshi', 'nugi', 'daniarton', 3573, '+62831252297', 'nugitakeshi@gmail.com'],
    ['rembrembo', 'juilianto', 'kusuma', 1371, '+62812414131', 'rembrembo@gmail.com'],
    ['bocilkematian', 'windah', 'batubara', 3171, '+62891341421', 'bocil.kematian@gmail.com'],
    ['setiabudi.mobil', 'anto', 'basudara', 3273, '+62228424123', 'setiabudi.mobil@gmail.com'],
    ['rajamobil88', 'engkos', 'koswara', 3273, '+622156328592', 'engkosmobil@yahoo.com'],
    ['mobilbekasjakarta', 'rizki', 'cornelius', 3174, '+62212512311', 'jakartamobil@gmail.com'],
    ['balipreloved', 'i made', 'in bali', 5171, '+628123123125', 'balipreloved@gmail.com'],
    ['desuexmakima', 'i gede', 'milik', 5171, '+62916359563249', 'makimadesu@gmail.com'],
    ['samarindamobil','rudi', 'samariska', 6472, '+6281325151242' , 'samarindamobil@gmail.com'],
    ['mugiwaramobil', 'mankidi', 'lutfi', 3578, "+629123823111", 'mugiwaramobil@gmail.com'],
    ['konohautomobile', 'naruto', 'uzumaki', 3173, '+62912652318', 'konohautomobile@gmail.com'],
    ['ishinomiyasecondhand', 'kaguya', 'sama', 1371, '+62151231251', 'ishinomiyasecondhand@gmail.com'],
    ['nierautomobile', 'tu' , 'bi', 6471, '+621515125121', 'nierautomobile@gmail'],
    ['mobillegend', 'zilong', 'mid', 3175, '+6298316723156', 'mobillegend@gmail.com'],
    ['showroomgroovestreet', 'carl', 'johnson', 3471, '+6287865324913', 'groovstreethome@ymail.com'],
    ['absendulubang', 'ada konto', 'ada lodon', 7371, '+6291315128512', 'bocilabsen@gmail.com'],
    ['kolektormobil', 'jajang', 'piston', 1375, '+62981231238124', 'kolektormobil@gmail.com'],
    ['sukamobilbekas', 'deni', 'panther', 3471, '+625125236246537', 'pilihpanterpinter@gmail.com'],
    ['minumanenergi', 'hemabison', 'jreng', 3573, '+62128381241241', 'emsatulimapuluhbisa@gmail.com'],
    ['empatmata', 'rey rey', 'reynaldi', 1375, '+628532416161612','kembalikelaptop@gmail.com'],
    ['peterpancar', 'ariel', 'noah', 3273, '+62593594258235', 'alexandriabestalbum@gmail.com'],
    ['julianto.98', 'juli', 'anton', 3174, '+62149320587925' , 'julijulijuli@gmail.com'],
    ['junianto.95', 'juni', 'anton', 3174, '+6291525235111' , 'junicukasapira@gmail.com'],
    ['carimobilmurah', 'budi', 'boxing', 6472, '+6216423574686', 'jojobukapintu@gmail.com'],
    ['kimetsunoriba', 'tanjidor', 'komodo', 3578, '+6281243522462', 'bloodemonart@gmail.com'],
    ['saberbestgirl', 'arturia', 'pendragon', 3173, '+629123153252', 'exkalibaaaaa@gmail.com'],
    ['soodoadoonrainu', 'kirigaya', 'kamanaatuhgaya', 6472, '+626243754713', 'linksutato@gmail.com'],
    ['jualmobilsitamurah', 'amanda', 'spooring', 6471, '+62713734751441' , 'amandaspooor@gmail.com'],
    ['kimino', 'kotoga', 'sukidakara', 3471, '+62164375468578', 'akabeempatlapan@gmail.com'],
    ['salisendiri', 'sallykau', 'selalusendiri', 1371, '+6216373547212', 'biarsalimencariku@gmail.com'],
    ['lalubiarkandiamenangis','lalubiarkan', 'diapergi', 1375, '+62176843634124', 'salikau75@gmail.com'],
]


with open('user.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
     
    #write multiple rows
    writer.writerows(users)
    
    #sql file will be created at the destination folder