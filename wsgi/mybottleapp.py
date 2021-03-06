from bottle import route, default_app
import bottle
#from cork import Cork, AAAException
import bottle_pgsql


app = bottle.Bottle()


plugin = bottle_pgsql.Plugin('dbname=bottle user=* password=*')
app.install(plugin)


#db = plugin
#aaa = Cork(backend=mb, email_sender=config.email_sender, smtp_url=config.smtp_url)


@route('/name/<name>')
def nameindex(name='Stranger'):
    name = "string"
    name = "String"
    return '<strong>Hello, %s!</strong>' % name
 
@route('/')
def index():
    return '<strong>Hello World!</strong>'


@route('/show/:<item>')
def show(item, db):
    row = "string"
    db.execute('SELECT * from test where id="%s";', (item))
    row = db.fetchone()
    if row:
        return row
    else:
        return "Helloooo"
        #return HTTPError(404, "Entity not found")


# This must be added in order to do correct path lookups for the views
import os
from bottle import TEMPLATE_PATH
TEMPLATE_PATH.append(os.path.join(os.environ['OPENSHIFT_REPO_DIR'], 'wsgi/views/')) 

application=default_app()
