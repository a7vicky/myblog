from pyblog.views import app
import os

if __name__ == '__main__':

    app.run(os.uname()[1], 5555 ,debug=True)
