# built-ins
from os.path import join as _join
import os

# local
from .exceptions import *

# 3rd party
import requests

# TODO:
#       1. Make Links, Domain, Account inherit from requests.Session()


class Client:
    """
    Base class for Rebrandly API actions
    """
    __slots__ = ['api_key', 'domain_name', 'domain_id', 'team_id', 'domain', 'hdrs']
    API_ENDPOINT = 'https://api.rebrandly.com/v1'

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
        path = "links"
        
        @staticmethod
        def list(options=None):
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
                r = requests.get(make_path(Client.Links.path), json=options)
                return dir(r)
            
        @staticmethod
        def get(link=None, options=None):
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
                return requests.get(make_path(Client.Links.path, link))
            else:
                return requests.get(make_path(Client.Links.path, link), json=options)

        @staticmethod
        def count(options=None):
            """
            :param options: A Dict of options
            :type options: dict

            :returns: RebrandlyResponse
            """
            if options is None:
                return requests.get(make_path(Client.Links.path, 'count'))
            else:
                return requests.get(make_path(Client.Links.path, 'count'), json=options)

        @staticmethod
        def new(method: str = 'post', options: dict = None) -> object:
            """Add a new Link

            :param method: GET or POST
            :type method:
            :param options: Dict of Options
            :type options: dict

            :rtype: object

            """
            if method == 'get':
                if options:
                    return requests.get(make_path(Client.Links.path, 'new'))
                else:
                    return requests.get(make_path(Client.Links.path, 'new'), json=options)
            if method == 'post':
                if options is None:
                    return requests.post(make_path(Client.Links.path))
                else:
                    return requests.post(make_path(Client.Links.path), json=options)

        @staticmethod
        def update(link: str = None, options: dict = None) -> object:
            """
            :param link: Link ID to update
            :type link: str
            :param options: A Dict of options
            :type options: dict

            :rtype: object

            """
            if options is None and link is None:
                raise NotEnoughArgumentsError(func='Client.Links#update', args=['link', 'options'])
            else:
                return requests.post(make_path(Client.Links.path, link), json=options)

        @staticmethod
        def delete(link=None, options=None):
            """
            :param link: Link ID
            :type link: str
            :param options: Options Dict
            :type options: dict
            """
            if link is None:
                raise NotEnoughArgumentsError(func='Client.Links#delete', args=['link'])

            else:
                if options:
                    if options.keys == ['trash']:
                        return requests.delete(make_path(Client.Links.path, link), json=options)
                    else:
                        raise InvalidOptionsError(possible=['trash'], invalid=options.keys())

    class Domain:
        """
        Rebrandly Domains API Actions
        """
        path = 'domains'
            
        @staticmethod
        def list(options=None):
            """
            List the domains in the account.

            :param options:
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
            :type options: dict

            :returns: RebrandlyResponse
            """
            if options is None:
                return requests.get(make_path(Client.Domain.path, ''))
            else:
                return requests.get(make_path(Client.Domain.path, ''), json=options)

        @staticmethod
        def get(domain=None):
            """
            Return information about a certain domain.

            :param domain: domain ID to pull information about
            :type domain: str

            :returns: RebrandlyResponse
            """
            return requests.get(make_path(Client.Domain.path, domain))

        @staticmethod
        def count(options=None):
            """
            Count the number of Domains the account has

            :param options: Options
            :type options: dict

            :returns: RebrandlyResponse

            """
            if options is None:
                return requests.get(make_path(Client.Domain.path, 'count'))
            else:
                return requests.get(make_path(Client.Domain.path, 'count'), json=options)

    class Account:
        """
        Rebrandly Account API Actions
        """
        path = 'account'

        @staticmethod
        def get(options=None):
            """
            Get account information

            :param options: Options
            :type options: dict
            """
            if options:
                return requests.get(make_path(Client.Account.path), json=options)
            else:
                return requests.get(make_path(Client.Account.path))
            
        @staticmethod
        def teams(options=None):
            """
            :param options: Options to filter teams by
            :type options: dict


            """
            if options is None:
                return requests.get(make_path(Client.Account.path, 'teams'))
            else:
                return requests.get(make_path(Client.Account.path, 'teams'), json=options)


def make_path(cls=None, path=None):
    """Make a request path

    :param cls: Class Path (usually Client.CLASS.path)
    :type cls: str
    :param path: Method path
    :type path: str
    :returns: Joined path
    :rtype: str
    """
    return _join(Client.API_ENDPOINT, cls, path)


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
