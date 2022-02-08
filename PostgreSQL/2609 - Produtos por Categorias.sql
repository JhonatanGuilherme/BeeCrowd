SELECT categories.name, SUM(products.amount) sum
FROM products INNER JOIN categories
ON products.id_categories = categories.id
GROUP BY categories.name;