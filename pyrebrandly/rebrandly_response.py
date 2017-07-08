from pyrebrandly.exceptions import *


class RebrandlyResponse:
    @staticmethod
    def raise_exception(code, rebrandly_response):

        if code == 200:
            return {'status': 'ok', 'response': rebrandly_response}
            # Everything went well, continue.
        elif code == 400:
            raise BadRequestError(rebrandly_response.message)
        elif code == 401:
            raise NotAuthorizedError(rebrandly_response.message)
        elif code == 403:
            if rebrandly_response.code == 'AlreadyExists':
                raise AlreadyExistsError(rebrandly_response.message)
            else:
                raise InvalidFormatError(rebrandly_response.message)
        if code == 404:
            raise NotFoundError(rebrandly_response.message)
        if code == 500:
            raise InternalServerError(rebrandly_response.message)
        if code == 502:
            raise BadGatewayError(rebrandly_response.message)
        if code == 503:
            raise APIUnavailableError(rebrandly_response.message)
        if code == 504:
            raise APITimeoutError(rebrandly_response.message)
