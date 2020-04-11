from pyblog.views import app
import os

if __name__ == '__main__':

    app.run(
       # ssl_context='adhoc',
         host = '0.0.0.0',
         debug = True,
         port = 8080
    )
