const express = require('express');
const app = express();
app.use(express.json());

const products = [
    { id: 1, name: "Wireless Headphones", price: 99.00 },
    { id: 2, name: "Smart Watch Pro", price: 199.00 }
];

app.get('/api/products', (req, res) => res.json(products));

if (require.main === module) {
    app.listen(3000, () => console.log("🚀 E-Commerce Catalog Service running on port 3000"));
}

module.exports = app;
