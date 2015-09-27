from django.conf import settings

# Frame width in seconds where only one import can be set up
THUNDERING_FRAME_WIDTH = getattr(
    settings, 'IMPORTING_THUNDERING_FRAME_WIDTH', 10
)

EXTERNAL_SHIPMENT_LIST_URL = getattr(
    settings, 'IMPORTING_EXTERNAL_SHIPMENT_LIST_URL', 'http://127.0.0.1:5000/shipments?status=ready'
)

EXTERNAL_SHIPMENT_NOTIFY_URL = getattr(
    settings, 'IMPORTING_EXTERNAL_SHIPMENT_NOTIFY_URL', 'http://127.0.0.1:5000/shipments/%d/status'
)

MAX_IMPORT_CLIENT_RETIRES = getattr(
    settings, 'IMPORTING_MAX_IMPORT_CLIENT_RETIRES', 10
)

MAX_IMPORT_CLIENT_RETIRES_DELAY = getattr(
    settings, 'IMPORTING_MAX_IMPORT_CLIENT_RETIRES_DELAY', 5
)

MAX_NOTIFY_CLIENT_RETIRES = getattr(
    settings, 'IMPORTING_MAX_NOTIFY_CLIENT_RETIRES', None   # unlimited
)

MAX_NOTIFY_CLIENT_RETIRES_DELAY = getattr(
    settings, 'IMPORTING_MAX_NOTIFY_CLIENT_RETIRES_DELAY', 5
)




