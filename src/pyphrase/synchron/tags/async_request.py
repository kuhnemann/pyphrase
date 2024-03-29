from __future__ import annotations

from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from ..client import SyncPhraseTMSClient

from ...models.phrase_models import (
    AsyncRequestDto,
    AsyncRequestStatusDto,
    PageDtoAsyncRequestDto,
)


class AsyncRequestOperations:
    def __init__(self, client: SyncPhraseTMSClient):
        self.client = client

    def getAsyncRequest(
        self,
        asyncRequestId: int,
        phrase_token: Optional[str] = None,
    ) -> AsyncRequestDto:
        """
                Get asynchronous request
                This API call will return information about the specified
        [asynchronous request](https://support.phrase.com/hc/en-us/articles/5709706916124-API-TMS-#asynchronous-apis-0-2).

        Apart from basic information about the asynchronous operation such as who created it and for what action, the response
        will contain a subset of [Get project](#operation/getProject) information.

        The response contains an `asyncResponse` field which will remain `null` until the async request has finished processing.
        If any errors occurred during processing of the request, this field will contain such errors or warnings.

        _Note_: It is important to keep track of the number of pending asynchronous requests as these are subject to [Phrase
        limits](https://support.phrase.com/hc/en-us/articles/5784117234972-Phrase-TMS-Limits#api-limits-async-requests-0-2).
                :param asyncRequestId: integer (required), path.

                :param phrase_token: string (optional) - if not supplied, client will look token from init

                :return: AsyncRequestDto
        """
        endpoint = f"/api2/v1/async/{asyncRequestId}"
        params = {}

        files = None
        payload = None

        r = self.client.get(
            endpoint, phrase_token, params=params, payload=payload, files=files
        )

        return AsyncRequestDto(**r)

    def listPendingRequests(
        self,
        all: bool = "False",
        pageNumber: int = "0",
        pageSize: int = "50",
        phrase_token: Optional[str] = None,
    ) -> PageDtoAsyncRequestDto:
        """
                List pending requests
                API call to return a list of pending asynchronous requests.

        Some operations within Phrase TMS are performed
        [asynchronously](https://support.phrase.com/hc/en-us/articles/5784117234972-Phrase-TMS-Limits#api-limits-async-requests-0-2)
        and their response only serves as an acknowledgement of receipt, not an actual completion of such request.
        Since Phrase  imposes restrictions on the number of pending asynchronous
        requests within an organization, this API call provides the means to check the number of such
        pending requests.

        When processing a large number of asynchronous operations, Phrase recommends periodically checking this list of
        pending requests in order to not receive an error code during the actual processing of the requests.

        _Note: Only actions triggered via the APIs are counted towards this limit, the same type of operation carried out via the
        UI is not taken into account. This means that even with 200 pending requests, users can still create jobs via the UI._
                :param all: boolean (optional), query. Pending requests for organization instead of current user. Only for ADMIN..
                :param pageNumber: integer (optional), query. Page number, starting with 0, default 0.
                :param pageSize: integer (optional), query. Page size, accepts values between 1 and 50, default 50.

                :param phrase_token: string (optional) - if not supplied, client will look token from init

                :return: PageDtoAsyncRequestDto
        """
        endpoint = "/api2/v1/async"
        params = {"all": all, "pageNumber": pageNumber, "pageSize": pageSize}

        files = None
        payload = None

        r = self.client.get(
            endpoint, phrase_token, params=params, payload=payload, files=files
        )

        return PageDtoAsyncRequestDto(**r)

    def getCurrentLimitStatus(
        self,
        phrase_token: Optional[str] = None,
    ) -> AsyncRequestStatusDto:
        """
        Get current limits


        :param phrase_token: string (optional) - if not supplied, client will look token from init

        :return: AsyncRequestStatusDto
        """
        endpoint = "/api2/v1/async/status"
        params = {}

        files = None
        payload = None

        r = self.client.get(
            endpoint, phrase_token, params=params, payload=payload, files=files
        )

        return AsyncRequestStatusDto(**r)
