# built-ins
from os.path import join as _join
import os

# local
from .exceptions import *

# 3rd party
import requests


class Client:
    """
    Base class for Rebrandly API actions
    """
    __slots__ = ['api_key', 'domain_name', 'domain_id', 'team_id', 'domain', 'hdrs']
    API_ENDPOINT = 'api.rebrandly.com/v1'

    @staticmethod
    def make_path(cls=None, path=None, *extra):
        """Make a request path

        :param path: Method path
        :type path: str
        :param params: Path Parameters (ID, etc.)
        :type params: str
        :param uri: API endpoint
        :type uri: str
        :returns: Joined path
        :rtype: str
        """
        return _join(Client.API_ENDPOINT, cls, path, extra)

    def __init__(self, api_key='', domain_name='rebrand.ly', domain_id='', team_id=None):
        """
        Initialize the class

        :param api_key: An API key from your account
        :type api_key: str
        :param domain_name: A domain name to use against the API
        :type domain_name: str
        :param domain_id: Your optional hexadecimal Domain ID
        :type domain_id: str
        :param team_id: Optional Team ID
        :type team_id: str
        """

        hdrs = {}

        self.api_key = api_key or os.environ.get('REBRANDLY_API_KEY')
        self.domain_name = domain_name or os.environ.get('REBRANDLY_DEF_DOMAIN_NAME')
        self.domain_id = domain_id or os.environ.get('REBRANDLY_DEF_DOMAIN_ID')
        self.team_id = team_id or os.environ.get('REBRANDLY_DEF_TEAM_ID')

        if domain_id and domain_name:
            self.domain = {
                'fullName': domain_name,
                'id':       domain_id
            }

        hdrs['Content-Type'] = 'application/json'
        hdrs['apikey'] = api_key
        if team_id:
            hdrs['team'] = team_id
        self.hdrs = hdrs

    class Links:
        """

        Rebrandly.Links class

        For managing links, including adding, removing, updating, returning
        """
        __slots__ = ['path']

        def __init__(self):
            self.path = "links"

        def list(self=None, options=None):
            """
            Lists links that follow certain criteria

            orderBy => {createdAt, updatedAt, title, slashtag} -- Sort by

            orderDir=> {desc, asc} -- Order Direction

            offset => N -- Skip N links

            limit => N -- Limit to N links

            favourite => true/false -- optional, shows or hides favourites if given

            status => active -- Sort by status, {active, trashed}

            :param options: A Dict of options
            :type options: dict

            :returns: RebrandlyResponse

            """
            if not options:
                r = requests.get(Client.make_path(self.path, '/'), options)
                status_code = r.status_code
                response = Response.raise_exception(status_code, r.json())
                if response == 'ok':
                    return response['response']

        def get(self=None, link: object = None, options: object =None):
            """
            :param link: Link ID to lookup
            :type link: str
            :param options: A Dict of options
            :type options: dict

            :returns: RebrandlyResponse
            """
            if id is None:
                raise APIError
            if options is None:
                return requests.get(Client.make_path(self.path, '', extra=link))
            else:
                return requests.get(Client.make_path(self.path, '', extra=link), options)

        def count(self=None, options=None):
            """
            :param options: A Dict of options
            :type options: dict

            :returns: RebrandlyResponse
            """
            if options is None:
                return requests.get(Client.make_path(self.path, 'count'))
            else:
                return requests.get(Client.make_path(self.path, 'count'), json=options)

        def new(self=None, method=None, options=None):
            """Add a new Link

            :param method: GET or POST
            :type method:
            :param options: Dict of Options
            :type options: dict

            :returns: RebrandlyResponse

            """
            if method == 'get':
                if options:
                    return requests.get(Client.make_path(self.path, 'new'))
                else:
                    return requests.get(Client.make_path(self.path, 'new'), json=options)
            if method == 'post':
                if options is None:
                    return requests.post(Client.make_path(self.path))
                else:
                    return requests.post(Client.make_path(self.path), json=options)

        def update(self=None, link=None, options=None):
            """
            :param link: Link ID to update
            :type link: str
            :param options: A Dict of options
            :type options: dict
            """
            if options is None:
                raise APIError("Rebrandly#update must be used with options.")
            else:
                return requests.post("/{}", json=options)

        def delete(id=None, options=None):
            """
            :param id: Link ID
            :type id: str
            :param options: Options Dict
            :type options: dict
            """
            if id == None:
                raise APIError("No ID to delete")

            else:
                if options:
                    return requests.delete("/{}".format(id))
                else:
                    if options.keys == ['trash']:
                        if options['trash'] == True or options['trash'] == False:
                            return requests.delete("/{}".format(id), options)
                        else:
                            raise APIError("Rebrandly#delete supports one key only, 'trash', which is a boolean")
                    else:
                        raise APIError("Rebrandly#delete supports one key only, 'trash', which is a boolean")


    class Domain:
        """
        Rebrandly Domains API Actions
        """
        def __init__(self):
            self.path = 'domains'

        def list(self=None, options=None):
            """
            List the domains in the account.

            :param self:
                active
                    optional boolean -- true/false
                type:
                    optional string -- user/service
                orderBy:
                    optional string -- criteria to filter by/ createdAt, updatedAt, fullName
                orderDir:
                    optional string -- Order Direction, asc/desc
                offset:
                    optional integer -- skip N domains
                limit:
                    optional integer -- limit to N domains
            :type self: dict

            :returns: RebrandlyResponse
            """
            if options is None:
                return requests.get(Client.make_path(path))
            else:
                return requests.get('/', options)

        def get(self, id=None):
            """
            Return information about a certain domain.

            :param id: domain ID to pull information about
            :type id: str

            :returns: RebrandlyResponse
            """
            return requests.get("/{}".format(id))

        def count(self, options=None):
            """
            Count the number of Domains the account has

            :param options: Options
            :type options: dict

            :returns: RebrandlyResponse

            """
            if options is None:
                return requests.get("/count")
            else:
                return requests.get("/count", options)

    class Account:
        """
        Rebrandly Account API Actions
        """
        def __init__(self):
            self.path = 'account'

        def get(self=None, options: object=None):
            """
            Get account information

            :param dict options: A dict of options

            """

        def teams(self=None, options: object=None):
            """
            :param options: Options to filter teams by
            :type options: dict

            :returns: RebrandlyResponse
            """
            if options is None:
                return requests.get("/teams")
            else:
                return requests.get("/teams", options)


class Response(requests.Response):

    def __init__(self, *args, **kwargs):
        self.tuple = {
            'msg': args,
            'extra': kwargs
        }

    def __str__(self):
        return self.tuple

    @staticmethod
    def raise_exception(code, rebrandly_response) -> dict or RebrandlyError:
        """
        Raise an exception based on whether we got an error, and which one.

        :param code:
        :type code:
        :param rebrandly_response:
        :type rebrandly_response:
        :return: object
        :rtype: dict or RebrandlyError
        """
        if code == 200:
            return {
                'status': 'ok',
                'code': 200,
                'response': rebrandly_response
            }
            # Everything went well, continue.
        elif code == 400:
            raise BadRequestError(rebrandly_response.code, rebrandly_response.message)
        elif code == 401:
            raise NotAuthorizedError(rebrandly_response.code, rebrandly_response.message)
        elif code == 403:
            if rebrandly_response.code == 'AlreadyExists':
                raise AlreadyExistsError(rebrandly_response.code, rebrandly_response.message)
            else:
                raise InvalidFormatError(rebrandly_response.code, rebrandly_response.message)
        if code == 404:
            raise NotFoundError(rebrandly_response.code, rebrandly_response.message)
        if code == 500:
            raise InternalServerError(rebrandly_response.code, rebrandly_response.message)
        if code == 502:
            raise BadGatewayError(rebrandly_response.code, rebrandly_response.message)
        if code == 503:
            raise APIUnavailableError(rebrandly_response.code, rebrandly_response.message)
        if code == 504:
            raise APITimeoutError(rebrandly_response.code, rebrandly_response.message)
