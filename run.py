
from app import create_app 

app = create_app()
"""calls the create_app() method"""

if __name__ == "__main__":
   """ checks if current module is the file being run"""

    app.run()
