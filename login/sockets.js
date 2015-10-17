
var sockets = [];

function init(io){
io.sockets.on('connection', function (client) {
console.log("connection initialized!");
sockets.push(client);
 });
}

function pushToSockets(data){
sockets.map(function(client){
client.emit(data.message,data.payload);
})
}

module.exports = {
init: init,
pushToSockets: pushToSockets
}