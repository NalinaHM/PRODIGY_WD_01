const http = require('http');
const server = http.createServer((req, res) => res.end("WebSocket Server Active"));

console.log("🚀 Real-Time Chat WebSocket Server listening on port 4000");

if (require.main === module) {
    server.listen(4000);
}
module.exports = server;
