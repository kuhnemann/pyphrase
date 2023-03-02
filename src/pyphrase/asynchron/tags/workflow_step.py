from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, Any, List, Optional, Union

if TYPE_CHECKING:
    from ..client import AsyncPhraseTMSClient

from ...models.phrase_models import (
    CreateWorkflowStepDto,
    EditWorkflowStepDto,
    PageDtoWorkflowStepDto,
    WorkflowStepDto,
)


class WorkflowStepOperations:
    def __init__(self, client: AsyncPhraseTMSClient):
        self.client = client

    async def listWFSteps(
        self,
        phrase_token: str,
        abbr: str = None,
        name: str = None,
        pageNumber: int = "0",
        pageSize: int = "50",
    ) -> PageDtoWorkflowStepDto:
        """
        List workflow steps

        :param phrase_token: string (required) - token to authenticate
        :param abbr: string (optional), query. Abbreviation of workflow step.
        :param name: string (optional), query. Name of the workflow step.
        :param pageNumber: integer (optional), query. Page number, starting with 0, default 0.
        :param pageSize: integer (optional), query. Page size, accepts values between 1 and 50, default 50.

        :return: PageDtoWorkflowStepDto
        """
        endpoint = f"/api2/v1/workflowSteps"
        params = {
            "pageNumber": pageNumber,
            "pageSize": pageSize,
            "name": name,
            "abbr": abbr,
        }

        files = None
        payload = None

        r = await self.client.get(
            phrase_token, endpoint, params=params, payload=payload, files=files
        )

        return PageDtoWorkflowStepDto(**r)

    async def createWFStep(
        self, phrase_token: str, body: CreateWorkflowStepDto
    ) -> WorkflowStepDto:
        """
        Create workflow step

        :param phrase_token: string (required) - token to authenticate
        :param body: CreateWorkflowStepDto (required), body.

        :return: WorkflowStepDto
        """
        endpoint = f"/api2/v1/workflowSteps"
        params = {}

        files = None
        payload = body

        r = await self.client.post(
            phrase_token, endpoint, params=params, payload=payload, files=files
        )

        return WorkflowStepDto(**r)

    async def editWFStep(
        self, phrase_token: str, workflowStepUid: str, body: EditWorkflowStepDto
    ) -> WorkflowStepDto:
        """
        Edit workflow step

        :param phrase_token: string (required) - token to authenticate
        :param workflowStepUid: string (required), path.
        :param body: EditWorkflowStepDto (required), body.

        :return: WorkflowStepDto
        """
        endpoint = f"/api2/v1/workflowSteps/{workflowStepUid}"
        params = {}

        files = None
        payload = body

        r = await self.client.put(
            phrase_token, endpoint, params=params, payload=payload, files=files
        )

        return WorkflowStepDto(**r)