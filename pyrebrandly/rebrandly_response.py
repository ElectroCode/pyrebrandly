import pyrebrandly.exceptions as exc


class RebrandlyResponse:
    @staticmethod
    def raise_exception(code, rebrandly_response):

        if code == 200:
            return {
                'status': 'ok',
                'code': 200,
                'response': rebrandly_response
            }
            # Everything went well, continue.
        elif code == 400:
            raise exc.BadRequestError(rebrandly_response.code, rebrandly_response.message)
        elif code == 401:
            raise exc.NotAuthorizedError(rebrandly_response.code, rebrandly_response.message)
        elif code == 403:
            if rebrandly_response.code == 'AlreadyExists':
                raise exc.AlreadyExistsError(rebrandly_response.code, rebrandly_response.message)
            else:
                raise exc.InvalidFormatError(rebrandly_response.code, rebrandly_response.message)
        if code == 404:
            raise exc.NotFoundError(rebrandly_response.code, rebrandly_response.message)
        if code == 500:
            raise exc.InternalServerError(rebrandly_response.code, rebrandly_response.message)
        if code == 502:
            raise exc.BadGatewayError(rebrandly_response.code, rebrandly_response.message)
        if code == 503:
            raise exc.APIUnavailableError(rebrandly_response.code, rebrandly_response.message)
        if code == 504:
            raise exc.APITimeoutError(rebrandly_response.code, rebrandly_response.message)
