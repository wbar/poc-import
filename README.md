
# Coding Exercise for Backend Developer - "Import"
## poc-import
Prof of Concept - Import data from system using tasks


Your job is to imports shipments from an external system. This method will be
"called" periodically by a cron job and could also be "called" by the user
from the UI on demand. The project is using the Django framework, so please
create the following entry points for the functionality:

- A management command to import shipments
- A view with a button on it, to start importing the shipments

The project is using PostgreSQL database.

The external service's interface looks like this:

    GET /shipments/?status=ready

Returns the following json data:

    {
        "shipments": [
            {
                "id": 12,
                "from": "Joe",
                "to": "Pete",
                "status": "ready",
            },
            {
                "id": 13,
                "from": "Stephen",
                "to": "Charlie",
                "status": "ready",
            }
        ]
    }

You want to create local shipment objects for the remote ones, and store
them in your database, basically "import" them.

Once a remote shipment is imported to your local database, you can set the
status on the remote side by making a request:

    POST /shipments/12/status

With the following json data:

    {
        "status": "imported"
    }

Please make sure that the remote and local shipment statuses are
consistent. Also think about the scenario where people click on the import
button too frequently: generating load on your infrastructure. How would you
prevent this from happening? Assume that you have multiple servers and
workers, they only share the database.

If the external service returns anything other than a 200 status, that is
considered an error meaning that the operation failed and the remote state has
not been altered.
