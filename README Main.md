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
![update last bid](https://user-images.githubusercontent.com/125452431/232265751-cb4e39bb-43bc-4141-b91f-2795887d3b8a.jpg)


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

##analytical query: Car model popularity ranking based on bid amount
```sql
SELECT c.model, COUNT(DISTINCT c.car_id) AS car_count, COUNT(b.bid_id) AS bid_count
FROM car_details c
LEFT JOIN bid b ON c.car_id = b.car_id
GROUP BY c.model
ORDER BY SUM(b.bid_price) asc;
```
`output`:
![analitikal 1](https://user-images.githubusercontent.com/125452431/232272089-26167b30-ad10-4e8f-a049-d8986c805249.jpg)

### analytical query: Compareing car prices based on the average price per city
```sql
SELECT 
    city.city_name,
    car_details.brand,
    car_details.model,
    car_details.year,
    commerce.price,
    ROUND(AVG(commerce.price) OVER (PARTITION BY city.city_name, car_details.brand, car_details.model, car_details.year), 2) as avg_car_city
FROM 
    commerce
JOIN 
    city ON commerce.city_id = city.city_id
JOIN 
    car_details ON commerce.car_id = car_details.car_id
ORDER BY 
    city_name ASC,
    brand ASC,
    model ASC,
    year ASC
```
`output`
![analitikal 2](https://user-images.githubusercontent.com/125452431/232272121-7a284f93-0b9c-44e8-94c8-7dee0f9dfb4a.jpg)

### analytical query: looking for a comparison of the date the user made a bid with the next bid along with the bid price given from the offer for a car model ('Camry' model as example)
```sql
       SELECT c.model, b1.user_id, b1.bid_date AS first_bid_date, b2.bid_date AS next_bid_date, b1.bid_price AS first_bid_price, b2.bid_price AS next_bid_price
FROM bid b1
JOIN car_details c ON b1.car_id = c.car_id
LEFT JOIN bid b2 ON b1.car_id = b2.car_id AND b2.bid_date > b1.bid_date
WHERE c.model = 'Camry' AND b2.bid_id = (
    SELECT MIN(bid_id) 
    FROM bid 
    WHERE car_id = b1.car_id AND bid_date > b1.bid_date
)
ORDER BY b1.bid_date ASC;
```
`output`:
![analitikal 3](https://user-images.githubusercontent.com/125452431/232272177-e60c7f1f-e0ed-4c51-8389-82b78f34c9ab.jpg)

### analytical query: Comparing the percentage difference in the average car price by model and the average bid price offered by customers in the last 6 months
```sql
SELECT cd.model,
       ROUND(AVG(c.price)::numeric, 2) AS avg_price,
       ROUND(AVG(b.bid_price)::numeric, 2) AS avg_bid_6month,
       ROUND((AVG(c.price) - AVG(b.bid_price))::numeric, 2) AS difference,
       ROUND(((AVG(c.price) - AVG(b.bid_price)) / AVG(c.price) * 100)::numeric, 2) AS difference_percent
FROM car_details cd
INNER JOIN commerce c ON cd.car_id = c.car_id
INNER JOIN bid b ON c.car_id = b.car_id
WHERE b.bid_date >= (NOW() - INTERVAL '6 months')
GROUP BY cd.model
ORDER BY difference_percent DESC;
```
`output`:
![analitikal 4](https://user-images.githubusercontent.com/125452431/232272205-6c6805e4-fcaf-42fc-8af3-7f4674dc3846.jpg)

### analytical query: Make a window function of the average bid price of a car brand and model for the last 6 months

```sql
SELECT 
    brand, 
    model, 
    AVG(bid_price) FILTER (WHERE bid_date >= NOW() - INTERVAL '6 months') OVER (PARTITION BY brand, model ORDER BY bid_date ASC ROWS BETWEEN 6 PRECEDING AND 1 PRECEDING) AS m_min_6,
    AVG(bid_price) FILTER (WHERE bid_date >= NOW() - INTERVAL '5 months') OVER (PARTITION BY brand, model ORDER BY bid_date ASC ROWS BETWEEN 5 PRECEDING AND 0 PRECEDING) AS m_min_5,
    AVG(bid_price) FILTER (WHERE bid_date >= NOW() - INTERVAL '4 months') OVER (PARTITION BY brand, model ORDER BY bid_date ASC ROWS BETWEEN 4 PRECEDING AND 1 PRECEDING) AS m_min_4,
    AVG(bid_price) FILTER (WHERE bid_date >= NOW() - INTERVAL '3 months') OVER (PARTITION BY brand, model ORDER BY bid_date ASC ROWS BETWEEN 3 PRECEDING AND 0 PRECEDING) AS m_min_3,
    AVG(bid_price) FILTER (WHERE bid_date >= NOW() - INTERVAL '2 months') OVER (PARTITION BY brand, model ORDER BY bid_date ASC ROWS BETWEEN 2 PRECEDING AND 1 PRECEDING) AS m_min_2,
    AVG(bid_price) FILTER (WHERE bid_date >= NOW() - INTERVAL '1 month') OVER (PARTITION BY brand, model ORDER BY bid_date ASC ROWS BETWEEN 1 PRECEDING AND 0 PRECEDING) AS m_min_1
FROM 
    car_details 
JOIN 
    bid ON car_details.car_id = bid.car_id 
WHERE 
    brand = 'honda' AND model = 'Civic';
```
`output`:
![analitikal 5](https://user-images.githubusercontent.com/125452431/232272311-732d90c9-db10-48a8-bf92-fb55266a99c5.jpg)


#DBMS USED
Pgadmin4
