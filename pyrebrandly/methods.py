import requests
from pyrebrandly.exceptions import RebrandlyError
from pyrebrandly.rebrandly_response import RebrandlyResponse
from pyrebrandly import version

class Rebrandly
    def __version__:
        repr(version.Rebrandlyrb)
    class Links
        base_uri = 'api.rebrandly.com/v1/links'
        api_key = None
        domain_id = None
        domain_name = None
        team_id = None
        if team_id
            team = {
                'team': team_id
            }

            headers('Content-Type' = > 'application/json')
            unless
            team.nil?
            headers << team
        def __init__(self):
            domain = {
                'fullName': domain_name,
                'id': domain_id
            }
            if team_id:
                team_header = {
                    'team': team_id
                }
            else:
        # @option option [Hash] nil A hash of options to list links
        # @overload list(options = nil)
        #   @note There are certain options allowed for sorting filtering
        #
        #     orderBy => {createdAt, updatedAt, title, slashtag} -- Sort by
        #
        #     orderDir=> {desc, asc} -- Order Direction
        #
        #     offset => N -- Skip N links
        #
        #     limit => N -- Limit to N links
        #
        #     favourite => true/false -- optional, shows or hides favourites if given
        #
        #     status => active -- Sort by status, {active, trashed}
        #
        #     @note Due to markup restrictions, I have to explain this next one
        #       @overload
        #         To use the sort by domain ID, use domain^id^, replacing ^
        #         with left and right square brackets respectively.
        def list(self, options=None):
            """
            :param options:
            :return:
            """
            if not options:
            rebrandly_response = self.

            class self.get('/', options)

            http_response = rebrandly_response
            RebrandlyResponse.raise_exception(http_response, rebrandly_response)

    # @param [String] id Link ID
    # @option options [Hash] nil A hash of options to filter by
    def get(id=nil, options=nil):
        """
        :param id
        :param options
        """
        if id == None:
            if options == None:
                response = self.get("/#{id}")

        else:
            response = self.get("/#{id}", options)

    def count(options=nil):
        if options == None:
            response = self.get("/count")
        else:
            response = self.get('/count', options)
    # @param [Symbol] method POST or GET method
    # @option options [Hash] nil A Hash of options to filter by
    def new(method=nil, options=nil)
        case
        method
        when: get
        if options.nil?
        response = self.
    
        class .get('/new')
    
    else
    response = self.
    
    
    class .get('/new', options)
    
    
    
    when: post
    if options.nil?
    response = self.
    
    
    class .get('/')
    
    else
    response = self.
    
    
    class .get('/', options)
    
    
    
    
    
    
    
    # @param [String] id link id to update
    # @option options [Hash] nil A Hash of the fields to update, all required
    # but not necessarily different than their values
    def update(id=nil, options=nil)
        if options.nil?
        raise RebrandlyAPIError
        "Rebrandly#update must be used with options."
    
    else
    response = self.
    
    
    class .post("/#{id}", options)
    
    
    
    
    
    
    # @param [String] id link id to delete
    # @option options [Hash] nil An optional Hash containing the key 'trash'
    # that declares whether to trash the link or to delete it permanently.
        def delete(id=nil, options=nil)
            if id.nil?
                raise RebrandlyAPIError
                "No ID to delete"
    
            else:
                if options.nil?
                    response = self.delete("/#{id}")
                else:
                    if options.keys == ['trash']:
                        if options['trash'] == True or options['trash'] == False:
                            response = self.delete("/#{id}", options)
                    else:
                        raise RebrandlyAPIError "Rebrandly#delete supports one key only, 'trash', which is a boolean"
    
    else
    raise RebrandlyAPIError
    "Rebrandly#delete supports one key only, 'trash', which is a boolean"
    
    
    
    
    
    
    
    class Domain:
        base_uri = 'api.rebrandly.com/v1/domains'
    
        # @option options [Hash] nil An optional Hash to filter by
        # @overload list(options = nil)
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
        def list(options=nil)
            if options == None:
                response = self.get('/')
            else:
                response = self.get('/', options)
    # @param [String] id domain id
    # @option options [Hash] nil An optional Hash containing filter
        def get(id=nil)
            response = self.get("/#{id}")
    # @option options [Hash] nil
    # @overload count(options = nil)
    #  Options:
    #
    #    active: true/false
    #
    #    type: user/service
        def count(options=None):
            if options == None:
                response = self.get("/count")
            else:
                response = self.get("/count", options)

    class Account:
        base_uri = 'api.rebrandly.com/v1/account'
    
        # @option options [Hash]
        def get(options=None):
            try:
                response = self.get('/')
            except Requests as e:
                "Requests encountered an error. Details: #{e}"

        def teams(options=None)
            if options == None:
                response = self.get("/teams/")
            else:
                response = self.get("/teams/", options)