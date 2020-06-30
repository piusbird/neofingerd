# neofingerd
Not Nearly as naughty as it sounds

This implements a working subset of the finger protocol RFCs 742, and 1288.
For now it relies on tcpserver from ucspi-tcp, but I plan on adding an 
internal socket-server later.

Requires the dotenv module after you've copied the sample config file
to .env and adjusted it Run initdb.py, and have fun!

# Why?

I was Bored, and making old internet gizmos work again is fun

# Features

* Users are mapped not by the system but by an sqlite3 database
* Multiple randomized banners
* Dynamic Content entities
