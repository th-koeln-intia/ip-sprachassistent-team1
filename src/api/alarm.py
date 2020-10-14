from app import app
import time

@app.route('/alarm')
def alarmtest():
    return 'alarm API works!'

@app.cli.command()
def check_alarm():
    """Check alarms."""
    print('Importing feeds...')
    time.sleep(5)
    print('Done!')