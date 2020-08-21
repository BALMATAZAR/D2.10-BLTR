import sentry_sdk
import os
import bottle
from sentry_sdk.integrations.bottle import BottleIntegration


sentry_dns = "https://e65b6282cf5e4607adfdaf4b8e282219@o406952.ingest.sentry.io/5399946"
app = bottle.Bottle()

sentry_sdk.init(
	dsn = sentry_dns,
    integrations = [BottleIntegration()]
)

@app.route('/')
def index():
	html = """
<!doctype html>
<html lang="ru">
  <head>
    <title>Sentry_proj</title>
  </head>
  <body>
    <div style="margin:0 30px;text-align:center;">
      <h1 style="font-size:50px;color:gray;">
      TEST
      </h1>
      <p style="font-size:35px;color:gray;">Успех или неудача? </p>
      <a href="/success">SUCCESS</a> | <a href="/fail">FAIL</a>
      </p>
    </div>
  </body>
</html>
"""
	return html

@app.route('/success')
def success():
	html = """
<!doctype html>
<html lang="ru">
  <head>
    <title>SUCCESS</title>
  </head>
  <body>
    <div style="margin:0 30px;text-align:center;">
      <h1 style="font-size:35px;color:gray;">
      Страница SUCCESS работы сервера с SENTRY!
      </h1>
    </div>
  </body>
</html>
"""
	return html

@app.route('/fail')
def fail():
    raise RuntimeError("Сообщение об ошибке: RuntimeError")

if os.environ.get('APP_LOCATION') == 'heroku':
    bottle.run(app,
               host="0.0.0.0",
               port=int(os.environ.get("PORT", 8080)))
else:
    bottle.run(app,
               host='localhost',
               port=8080)