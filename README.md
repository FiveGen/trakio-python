# Trak.io API client for Python

Use this library to integrate your Python app with [trak.io](http://www.trak.io).
Built and used by [UserApp](https://www.userapp.io) in their [trak.io](http://www.trak.io) addon.

### Install with [pip](https://pypi.python.org/pypi/trakio/)

    pip install trakio --pre

### Usage

    import trakio

    client=trakio.TrakIOClient("API KEY")

    result=client.identify("your_unique_id", {
        'email':'you@email.com'
    })

### Constructor

    TrakIOClient(token, base_address='api.trak.io', version=1, secure=True)

### Methods

* identify(distinct_id, properties)
* alias(distinct_id, alias)
* annotate(event, properties=None, channel=None)
* track(distinct_id, event, channel=None, properties=None, time=None)

### Error handling

	try:
	    client.track("bob")
	except trakio.TrakIOServiceException as e:
		print(e.type, e.message, e.details)
	except trakio.TrakIOException as e:
		print(e)

### License

MIT
