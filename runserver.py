from pyblog.views import app
import os

if __name__ == '__main__':

    app.run(
       # ssl_context='adhoc',
         host = 'localhost',
         debug = True,
         port = 8080
    )
