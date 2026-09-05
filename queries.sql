-- Total revenue and orders by country
SELECT 
    "Country", 
    COUNT(DISTINCT "Invoice") AS total_orders,
    SUM("TotalPrice") AS total_revenue
FROM retail
GROUP BY "Country"
ORDER BY total_revenue DESC
LIMIT 10;

-- Monthly revenue trend
SELECT 
    DATE_TRUNC('month', "InvoiceDate"::timestamp) AS month,
    COUNT(DISTINCT "Invoice") AS total_orders,
    SUM("TotalPrice") AS total_revenue
FROM retail
GROUP BY month
ORDER BY month;

-- RFM: recency, frequency, monetary per customer
SELECT 
    "Customer ID",
    (SELECT MAX("InvoiceDate"::timestamp) FROM retail) - MAX("InvoiceDate"::timestamp) AS recency,
    COUNT(DISTINCT "Invoice") AS frequency,
    SUM("TotalPrice") AS monetary
FROM retail
GROUP BY "Customer ID"
ORDER BY monetary DESC;
