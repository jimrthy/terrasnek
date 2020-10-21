"""
Module for Terraform Cloud API Endpoint: OAuth Clients.
"""

from .endpoint import TFCEndpoint
from._constants import Entitlements

class TFCOAuthClients(TFCEndpoint):
    """
    `API Docs \
        <https://www.terraform.io/docs/cloud/api/oauth-clients.html>`_
    """

    def __init__(self, instance_url, org_name, headers, well_known_paths, verify, log_level):
        super().__init__(instance_url, org_name, headers, well_known_paths, verify, log_level)
        self._org_api_v2_base_url = \
            f"{self._api_v2_base_url}/organizations/{org_name}/oauth-clients"
        self._oauth_clients_api_v2_base_url = f"{self._api_v2_base_url}/oauth-clients"

    def _required_entitlements(self):
        return [Entitlements.VCS_INTEGRATIONS]

    def list(self):
        """
        ``GET /organizations/:organization_name/oauth-clients``

        `API Doc Reference \
            <https://www.terraform.io/docs/cloud/api/oauth-clients.html#list-oauth-clients>`_
        """
        return self._list(self._org_api_v2_base_url)

    def show(self, client_id):
        """
        ``GET /oauth-clients/:id``

        `API Doc Reference \
            <https://www.terraform.io/docs/cloud/api/oauth-clients.html#show-an-oauth-client>`_
       """
        url = f"{self._oauth_clients_api_v2_base_url}/{client_id}"
        return self._show(url)

    def create(self, payload):
        """
        ``POST /organizations/:organization_name/oauth-clients``

        `API Doc Reference \
            <https://www.terraform.io/docs/cloud/api/oauth-clients.html#create-an-oauth-client>`_

        `Sample Payload \
            <https://www.terraform.io/docs/cloud/api/oauth-clients.html#sample-payload>`_
        """
        return self._create(self._org_api_v2_base_url, payload)

    def update(self, client_id, payload):
        """
        ``PATCH /oauth-clients/:id``

        `API Doc Reference \
            <https://www.terraform.io/docs/cloud/api/oauth-clients.html#update-an-oauth-client>`_

        `Sample Payload \
            <https://www.terraform.io/docs/cloud/api/oauth-clients.html#sample-payload-1>`_
        """
        url = f"{self._oauth_clients_api_v2_base_url}/{client_id}"
        return self._update(url, payload)

    def destroy(self, client_id):
        """
        ``DELETE /oauth-clients/:id``

        `API Doc Reference \
            <https://www.terraform.io/docs/cloud/api/oauth-clients.html#destroy-an-oauth-client>`_
        """
        url = f"{self._oauth_clients_api_v2_base_url}/{client_id}"
        return self._destroy(url)
