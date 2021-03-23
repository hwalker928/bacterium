import configparser
import socket

print("Starting server!")

config = configparser.ConfigParser()
config.read('db.ini')

host = config['network']['host']
port = config['network']['port']

print("Server running on "+str(host)+":"+str(port))
