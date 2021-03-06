import os
from common.auth import Auth
from locust import HttpUser, task, between


class PersonalDemographicsUser(HttpUser):
    wait_time = between(5, 9)

    def auth(self):
        return Auth(
            os.environ["LOCUST_HOST"],
            os.environ["CALLBACK_URL"],
            os.environ["CLIENT_ID"],
            os.environ["CLIENT_SECRET"]
        )

    def on_start(self):
        self.base_path = os.environ["BASE_PATH"]
        self.patient_search = os.environ["PATIENT_SEARCH"]
        authenticator = self.auth()
        self.credentials = authenticator.login()
        self.headers = {
            "Authorization": self.credentials["token_type"] + " " + self.credentials["access_token"],
            "NHSD-Identity-UUID": "1234567890",
            "NHSD-Session-URID": "1234567890",
        }

    @task(1)
    def pds_api(self):
        self.client.get(f"{self.base_path}/Patient/{self.patient_search}", headers=self.headers)
