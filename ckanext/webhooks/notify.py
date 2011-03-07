import urllib2, json, logging

from ckanext.queue.worker import Worker 

log = logging.getLogger(__name__)

OP_MAP = {
    'created': 'create',
    'updated': 'update',
    'deleted': 'delete'
    }

CONFIG_KEY = 'webhooks.target'

class WebhooksWorker(Worker):

    def consume(self, routing_key, operation, payload):
        assert CONFIG_KEY in self.config, "No webhooks.target defined!"
        target = self.config.get(CONFIG_KEY)
        req_data = json.dumps({
            'payload': payload, 
            'entity-type': routing_key,
            'operation-type': OP_MAP.get(operation)
            })
        req = urllib2.Request(target, req_data, 
                {'Content-type': 'application/json'})
        urlfh = urllib2.urlopen(req)
        urlfh.close()


