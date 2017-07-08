from pyrebrandly.exceptions import RebrandlyError


class RebrandlyResponse:
    @staticmethod
    def raise_exception(code, rebrandly_response):

        if code == 200:
            return {'status': 'ok', 'response': rebrandly_response}
            # Everything went well, continue.
        elif code == 400:
            raise RebrandlyError.BadRequestError(rebrandly_response.message)
        elif code == 401:
            raise RebrandlyError.NotAuthorizedError(rebrandly_response.message)
        elif code == 403:
            if rebrandly_response.code == 'AlreadyExists':
                raise RebrandlyError.AlreadyExistsError(rebrandly_response.message)
            else:
                raise RebrandlyError.InvalidFormatError(rebrandly_response.message)
        if code == 404:
            raise RebrandlyError.NotFoundError(rebrandly_response.message)
        if code == 500:
            raise RebrandlyError.InternalServerError(rebrandly_response.message)
        if code == 502:
            raise RebrandlyError.BadGatewayError(rebrandly_response.message)
        if code == 503:
            raise RebrandlyError.APIUnavailableError(rebrandly_response.message)
        if code == 504:
            raise RebrandlyError.APITimeoutError(rebrandly_response.message)