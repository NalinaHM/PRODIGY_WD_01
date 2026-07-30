const express = require('express');
const app = express();
app.use(express.json());

const PORT = 3000;

app.post('/api/auth/register', (req, res) => {
    const { email, password } = req.body;
    res.status(201).json({ success: true, message: `User ${email} registered successfully.` });
});

app.post('/api/auth/login', (req, res) => {
    const { email } = req.body;
    const token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.sampletoken.signature";
    res.json({ success: true, token, user: { email, role: "developer" } });
});

if (require.main === module) {
    app.listen(PORT, () => console.log(`🚀 Auth Service running on port ${PORT}`));
}

module.exports = app;
