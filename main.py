#This IS THE MAIN FILE TO RUN TO START OUR WEBSITE 
from website import create_app #IMPORTING FROM CREATE_APP FROM INITI.PY FILE


app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
