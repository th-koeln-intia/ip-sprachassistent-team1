from app import app

@app.route('/light')
def lighttest():
    return 'light API works!'