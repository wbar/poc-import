from pocimport.celery import app
from celery.utils.log import get_task_logger
from crm.models import Shipment
from .models import ImportProcessLog
from .settings import MAX_IMPORT_CLIENT_RETIRES_DELAY, MAX_IMPORT_CLIENT_RETIRES, EXTERNAL_SHIPMENT_LIST_URL, \
    MAX_NOTIFY_CLIENT_RETIRES, MAX_NOTIFY_CLIENT_RETIRES_DELAY, EXTERNAL_SHIPMENT_NOTIFY_URL
from django.db import transaction
import urllib.request
import json
import time


class Logger(object):
    _logger = get_task_logger(__name__)

    def info(self, process_id, msg):
        self._logger.info(msg)
        with transaction.atomic():
            ImportProcessLog.objects.create(process_id=process_id, message=msg)

    def error(self, process_id, msg):
        self._logger.error(msg)
        with transaction.atomic():
            ImportProcessLog.objects.create(process_id=process_id, message=msg, level=ImportProcessLog.Level.ERROR)

logger = Logger()


@app.task(bind=True, default_retry_delay=MAX_IMPORT_CLIENT_RETIRES_DELAY, max_retries=MAX_IMPORT_CLIENT_RETIRES)
def start_import_process(self, process_id):

    logger.info(process_id, 'Starting process for Process ID: %d' % process_id)
    try:
        data = json.loads(urllib.request.urlopen(EXTERNAL_SHIPMENT_LIST_URL).readall().decode('utf-8'))
    except Exception as e:
        logger.error(process_id, 'An error occurred when fetching data from external system: %s' % e)
        self.retry(exc=e)
        return
    if 'shipments' not in data:
        logger.info(process_id, 'No shipments in response.')
        return
    for item in data['shipments']:
        create_shipment.delay(process_id, item)


@app.task()
def create_shipment(process_id, data):
    logger.info(process_id, 'Processing data for shipment: %d' % int(data['id']))
    # simulating
    time.sleep(3)
    obj, created = Shipment.objects.get_or_create(
        external_id=int(data['id']),
        defaults={
            'from_name': data['from'],
            'to_name': data['to']
        }
    )
    if created:
        notify_external_system.delay(process_id, obj.external_id)


@app.task(bind=True, default_retry_delay=MAX_NOTIFY_CLIENT_RETIRES_DELAY, max_retries=MAX_NOTIFY_CLIENT_RETIRES)
def notify_external_system(self, process_id, ext_shipment_id):
    try:
        logger.info(process_id, 'Notifying external system about shipment: %d' % ext_shipment_id)
        time.sleep(3)
        params = json.dumps({'status': 'imported'}).encode('utf8')
        url = EXTERNAL_SHIPMENT_NOTIFY_URL % ext_shipment_id
        req = urllib.request.Request(
            url, data=params, headers={'content-type': 'application/json'}, method='POST'
        )
        response = urllib.request.urlopen(req)
        logger.info(process_id, 'Received code: %d' % response.getcode())
        if int(response.getcode()/100) != 2:
            logger.error(process_id, 'Wrong response code: %d' % response.getcode())
            self.retry()
            return
    except Exception as e:
        logger.error(process_id, 'while import I received an error: %s' % e)
        self.retry(exc=e)











