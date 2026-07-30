const express = require('express');
const app = express();
app.use(express.json());

const tasks = [
    { id: 1, title: "Implement OAuth Login", status: "todo" },
    { id: 2, title: "Build Kanban Drag API", status: "in-progress" },
    { id: 3, title: "Deploy Main Repo to GitHub", status: "done" }
];

app.get('/api/tasks', (req, res) => res.json(tasks));

if (require.main === module) {
    app.listen(6000, () => console.log("🚀 Kanban Service running on port 6000"));
}
module.exports = app;
