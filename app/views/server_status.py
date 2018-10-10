
def status (status, name):

    online = "online" in status['status']
    reason = None

    if not online:
        reason = status['status'].split(':', 1)[1]

    return {
        'online' : online,
        'reason' : reason,
        'consensus' : status['consensus'],
        'block_height' : status['block_height'],
        'total_tx' : status['total_tx'],
        'unconfirmed_tx' : status['unconfirmed_tx'],
        'url' : status['url'],
        'name' : name
    }