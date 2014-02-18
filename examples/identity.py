import os, sys
sys.path.append(os.path.abspath('../'))

import config, trakio

client=trakio.TrakIOClient(config.trakio_api_token)

identify_result=client.identify("some distinct id", {
	'email':'distinct_email@fakeemailprovider.fake'
})

print(identify_result)