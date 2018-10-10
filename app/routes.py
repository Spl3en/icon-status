from flask import render_template
from app import app
from app import constants

from app.models import server_status as model
from app.views import server_status as view

@app.route('/')
@app.route('/index')
def index():

    servers = []
    servers.append (view.status (model.status ("https://ctz.solidwallet.io"), "Mainnet 1"))
    servers.append (view.status (model.status ("https://wallet.icon.foundation"), "Mainnet 2"))
    servers.append (view.status (model.status ("https://bicon.net.solidwallet.io"), "Testnet for DApps"))
    servers.append (view.status (model.status ("https://test-ctz.solidwallet.io"), "Testnet for Exchanges"))
    servers.append (view.status (model.status ("http://13.209.103.183:9000"), "ICON devteam net"))

    return render_template ('index.html', constants=constants, servers=servers)
