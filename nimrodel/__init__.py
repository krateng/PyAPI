name = "nimrodel"
version = 0,4,6
versionstr = ".".join(str(n) for n in version)
author = {
	"name": "Johannes Krattenmacher",
	"email": "python@krateng.dev",
	"github": "krateng"
}
requires = [
	"bottle",
	"waitress",
	"doreah>=0.9.1",
	"parse"
]


from ._apiobject import API as ObjectAPI
from ._apifunction import API as EndpointAPI
from ._misc import Multi

# short names
OAPI = ObjectAPI
EAPI = EndpointAPI

# default
API = OAPI
