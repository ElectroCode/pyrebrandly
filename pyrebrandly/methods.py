import requests
import json
from pyrebrandly.exceptions import RebrandlyError
from pyrebrandly.rebrandly_response import RebrandlyResponse
from pyrebrandly import version

"""
.. automodule:: Rebrandly
    :members:
    :undoc-members:
    :inherited-members:
    :show-inheritance:
"""
class Rebrandly:
    """
    Base class for Rebrandly API actions
    """

    @property
    def __version__(self):
        """
        Returns:
            version
        """
        return repr(version.pyrebrandly)

    base_uri = 'api.rebrandly.com/v1'
#        if team_id:
#            team = {
#                'team': team_id
#            }

    headers = {'Content-Type': 'application/json'}
#            if team:
#                headers << team
    def __init__(self, api_key='', domain_name='rebrand.ly', domain_id='', team_id='', domain={}):
        self.api_key = api_key, self.domain_name = domain_name, self.domain_id = domain_id, self.team_id = team_id, self.domain = domain
        domain = {
            'fullName': domain_name,
            'id': domain_id
        }
#            if team_id:
#                headers['team'] =  team_id

class Links(Rebrandly):
    """

    Main Rebrandly.Links class

    For managing links, including adding, removing, updating, returning
    """


    def list(options=None):
        """
        Lists links that follow certain criteria

        orderBy => {createdAt, updatedAt, title, slashtag} -- Sort by

        orderDir=> {desc, asc} -- Order Direction

        offset => N -- Skip N links

        limit => N -- Limit to N links

        favourite => true/false -- optional, shows or hides favourites if given

        status => active -- Sort by status, {active, trashed}

        Parameters:
            options: A Dict of options

        """
        if not options:
            rebrandly_return requests.get('/', options)

            RebrandlyResponse.raise_exception(http_response, rebrandly_response)

    def get(id=None, options=None):
        """
        Args:
            id: Link ID to lookup
            options: A Dict of options
        """
        if id is None:
            raise RebrandlyError.APIError
        if options is None:
            return requests.get("/#{id}")
        else:
            return requests.get("/#{id}", options)

    def count(options=None):
        """
        Args:
            options (Dict): A Dict of options

        Returns:
            RebrandlyResponse
        """
        if options is None:
            return requests.get("/count")
        else:
            return requests.get('/count', options)

    def new(method=None, options=None):
        """
        Args:
            method (String): POST or GET HTTP method
            options (Dict): a Dict() of options

        Returns:
            HTTP Response
        """
        if method == 'get':
            if options:
                return requests.get('/new')
            else:
                return requests.get('/new', options)
        if method == 'post':
            if options is None:
                return requests.get('/')
            else:
                return requests.get('/', options)

    def update(id=None, options=None):
        """

        Parameters
        ----------
            id: Link ID to update
            options: A Dict
        """
        if options is None:
            raise RebrandlyError.APIError("Rebrandly#update must be used with options.")
        else:
            return requests.post("/#{id}", options)

    def delete(id=None, options=None):
        """

            Parameters
            ----------
            id: Link ID
            options: Options Dict
        """
        if id == None:
            raise RebrandlyError.APIError("No ID to delete")

        else:
            if options:
                return requests.delete("/#{id}")
            else:
                if options.keys == ['trash']:
                    if options['trash'] == True or options['trash'] == False:
                        return requests.delete("/#{id}", options)
                    else:
                        raise RebrandlyError.APIError("Rebrandly#delete supports one key only, 'trash', which is a boolean")
                else:
                    raise RebrandlyError.APIError("Rebrandly#delete supports one key only, 'trash', which is a boolean")

class Domain(Rebrandly):
    """
    """
    base_uri = 'api.rebrandly.com/v1/domains'

    # @option options [Hash] None An optional Hash to filter by
    # @overload list(options = None)
    #   @note There are certain options allowed for sorting filtering
    #
    #   active: optional boolean -- true/false
    #
    #   type: optional string -- user/service
    #
    #   orderBy: optional string -- criteria to filter by/ createdAt, updatedAt, fullName
    #
    #   orderDir: optional string -- Order Direction, asc/desc
    #
    #   offset: optional integer -- skip N domains
    #
    #   limit: optional integer -- limit to N domains
    def list(options=None):
        """

        Args:
            options:
        """
        if options is None:
            return requests.get('/')
        else:
            return requests.get('/', options)
# @param [String] id domain id
# @option options [Hash] None An optional Hash containing filter
    def get(id=None):
        """

        Args:
            id:
        """
        return requests.get("/#{id}")
# @option options [Hash] None
# @overload count(options = None)
#  Options:
#
#    active: true/false
#
#    type: user/service
    def count(options=None):
        """

        Args:
            options:
        """
        if options is None:
            return requests.get("/count")
        else:
            return requests.get("/count", options)

class Account(Rebrandly):
    """
    """
    base_uri = 'api.rebrandly.com/v1/account'

    # @option options [Hash]
    def get(options=None):
        """

        Args:
            options:
        """
        try:
            return requests.get('/')
        except Requests as e:
            "Requests encountered an error. Details: #{e}"

    def teams(options=None):
        """

        Args:
            options:
        """
        if options is None:
            return requests.get("/teams/")
        else:
            return requests.get("/teams/", options)
