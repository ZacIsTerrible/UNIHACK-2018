// Server Setup and Running.
const express = require('express');
const app = express();

server = app.listen(3001, function(){
    console.log('server is running on port 3001')
});

// import Socket IO for Realtime Bi-directional Communication
const io = require('socket.io')(server);

// OPEN CONNECTION for communication.
io.on('connection', function(socket) {
    console.log(socket.id)
	console.log("Connected")

	// Handling EVENT Below!!!!

	// SEND_MESSAGE event.
	// The following function read:
	// ON SEND MESSAGE event, EXECUTE THIS FUNCTION.
	socket.on('ADDED_PATIENT', function(data) {
		console.log("RECEIVE 'SEND' Request")
    	io.emit('INCOMING_PATIENT', data)
    });

    socket.on('ASSIGNED_DOCTOR', function(data) {
		console.log("RECEIVE 'SEND' Request")
    	io.emit('ATTENTION_DOCTOR', data)
    });

    socket.on('ACCEPTED_PATIENT', function(data) {
		console.log("RECEIVE 'SEND' Request")
    	io.emit('DIAGNOSIS_PATIENT', data)
    });

});
