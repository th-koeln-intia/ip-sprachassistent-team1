from api.app import app

@app.route('/alarm')
def alarmtest():
    return 'alarm API works!'