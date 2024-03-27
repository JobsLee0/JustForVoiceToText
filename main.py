import client.client_factory as cf
import config.config as conf
import gui.gui as g

g.start(cf.get_client(conf.get_conf().getClientType()))
