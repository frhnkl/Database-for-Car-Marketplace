# Database-for-Car-Marketplace
To learn more about SQL and relational databases, we can create a project to practice. In this project, you are given the task of building a relational database for a website that offers used car sales. The general description of this project is that anyone can offer their products (used cars) in the form of advertisements and potential buyers can search based on several categories. the client determines several parameters that we must comply with in creating a database which includes:

1. a user can sell more than one car but must first fulfil personal data (user's name, contact, domicile).
2. Users can advertise cars for sale provided that the ad must have car information (make, model, type, transmission, year, etc.) and contact the seller.
3. Each user can search for the offered car based on the seller's user location, car brand, and car body type.
4. There is a bid feature for users who allow "bids" on the cars they sell.
5. transactions are made outside the web so that they are not included in the scope of work

i've created this database so we can learn SQL together. This DB can also be used as a simple Car Marketplace database if needed (whith slight changes)

![ERD DB](https://user-images.githubusercontent.com/125452431/232265190-8591fef8-8060-446c-8321-3691700658ec.jpg)

## Sample SQL Queries
Following are sample `SQL` queries you can do on `Database-for-Car-Marketplace' to test`

## Looking for cars from 2015 and up

```sql
select car_details.car_id, car_details.brand, car_details.type, car_details.model, car_details.year, commerce.price
FROM car_details
INNER JOIN commerce ON car_details.car_id=commerce.car_id
WHERE year > 2015;
```
`output`:
![output query 1](https://user-images.githubusercontent.com/125452431/232265484-5416a01d-6fce-495e-b47c-d90b2c5fe053.jpg)

### 2. Added one new product bid record
`before`:
![last bid](https://user-images.githubusercontent.com/125452431/232265545-961ef002-3696-4fb3-98f8-aed3f4a258d7.jpg)

```sql
INSERT INTO bid (bid_id, car_id, user_id, bid_date, bid_price, bid_status)
VALUES (34, 76, 'rangers123', '2021-09-02', 50000000, 'on')
```
`after`: 
![update last bid](https://user-images.githubusercontent.com/125452431/232265553-3806c749-4c2f-4f01-a47a-b6e662f5d1ea.jpg)

### 3. View all cars sold 1 account from the most recent (using 'kolektormobil' user_id as example)
```sql
select car_details.car_id, car_details.brand, car_details.type, car_details.model, car_details.year, commerce.price, commerce.post_date, commerce.user_id
FROM car_details
INNER JOIN commerce ON car_details.car_id=commerce.car_id
WHERE user_id = 'kolektormobil';
```
`output`:
![output q](https://user-images.githubusercontent.com/125452431/232265614-94403a95-4cfa-489e-9aff-6264a47427ac.jpg)

### 4. Search for the cheapest used cars based on keywords (keyword: Yaris)
```sql
select car_details.car_id, car_details.brand, car_details.model, car_details.year, commerce.price, commerce.post_date
FROM car_details
INNER JOIN commerce ON car_details.car_id=commerce.car_id
WHERE model = 'Yaris'
order by price asc;
```
`output`:
![output p](https://user-images.githubusercontent.com/125452431/232265648-3015654a-cf8b-4a08-8031-b685333138c7.jpg)

### 5. Looking for the nearest used car based on a city id, the shortest distance is calculated based on latitude longitude (city_id 3173)
```sql
SELECT commerce.commerce_id AS product_id, car_details.brand, car_details.model, car_details.year, 
       commerce.price, SQRT((city.latitude - given_city.latitude)^2 + (city.longitude - given_city.longitude)^2) AS distance
FROM commerce
JOIN car_details ON commerce.car_id = car_details.car_id
JOIN users ON commerce.user_id = users.user_id
JOIN city ON commerce.city_id = city.city_id
CROSS JOIN (SELECT latitude, longitude FROM city WHERE city_id = 3173) AS given_city -- change given_city_id to 3173
WHERE car_details.year <= extract(year from now()) - 3 -- used car criteria, assuming car age greater than or equal to 3 years is used

ORDER BY distance ASC
LIMIT 10;
```
`output`:
![output ps](https://user-images.githubusercontent.com/125452431/232265708-51e19d65-846e-47b4-bb33-997dff4c68a6.jpg)
