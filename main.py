from src.app import app

HOST = 'localhost'
PORT = 4500
DEBUG = True

if(__name__ == '__main__'):
    app.run(HOST, PORT, DEBUG)
