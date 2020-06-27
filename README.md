# Pulse
This is a demonstration of an architectural idea for web applications.

The idea represented here is based upon representing the ui as a pure function
mapping JSON to DOM with a complimentary mapping of Events to Websocket messages.

The server in this architecure must play the role of every client's logic,
including the 'dynamic stuff that makes SPAs great'.

The assumption is that the latency it takes for the server to assume those 
responsibilities does not destroy the responsiveness which that extra logic
accomplished in the first place.


## Running the app
* make sure dependencies are installed (pkg mgmt for py coming soon)
* python3 serve_pulse.py
* python3 serve.py
* go to localhost:5000
