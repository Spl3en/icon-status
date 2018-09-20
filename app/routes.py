from flask import render_template
from app import app
from app import constants

from app.models import server_status as server_status_model
from app.views import server_status as server_status_view

@app.route('/')
@app.route('/index')
def index():

    # Get the latest blocks
    ctz = server_status_model.get_status ("https://ctz.solidwallet.io")
    wallet = server_status_model.get_status ("https://wallet.icon.foundation")
    bicon = server_status_model.get_status ("https://bicon.net.solidwallet.io")
    test_ctz = server_status_model.get_status ("https://test-ctz.solidwallet.io")
    iconNet = server_status_model.get_status ("http://13.209.103.183:9000")

    ctz = server_status_view.get_status (ctz,"https://ctz.solidwallet.io", "Mainnet 1")
    wallet = server_status_view.get_status (wallet,"https://wallet.icon.foundation",  "Mainnet 2")
    bicon = server_status_view.get_status (bicon, "https://bicon.net.solidwallet.io", "Testnet for DApps")
    test_ctz = server_status_view.get_status (test_ctz, "https://test-ctz.solidwallet.io", "Testnet for Exchanges")
    iconNet = server_status_view.get_status (iconNet, "http://13.209.103.183:9000", "ICON devteam net")

    servers = [ctz, wallet, bicon, test_ctz, iconNet]

    return render_template ('index.html', constants=constants, servers=servers)
