const express = require('express');
const app = express();
app.use(express.json());

const posts = [];

app.get('/api/posts', (req, res) => res.json(posts));
app.post('/api/posts', (req, res) => {
    const newPost = { id: Date.now(), ...req.body };
    posts.unshift(newPost);
    res.status(201).json(newPost);
});

if (require.main === module) {
    app.listen(5000, () => console.log("🚀 CMS API Service running on port 5000"));
}
module.exports = app;
