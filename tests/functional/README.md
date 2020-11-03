# Functional Testing
​
Testing the API depending on mode of authentication.
​
This test suite uses [pytest](https://docs.pytest.org/en/stable/)
​
​
​
## Install dependancies
​
* To install the project dependancies:  
    * ```$ poetry install```
​
​
​
## Configuration through Environment Varibles
​
* To run the pytest script some environment variables must be set:
  - ```UNATTENDED_ACCESS_SIGNING_KEY_PATH``` path to private key for signing the JWT.
  - ```UNATTENDED_ACCESS_API_KEY``` the API key for your application.
  - ```PDS_BASE_PATH``` The url for the applications Apigee proxy.
  - ```APIGEE_ENVIRONMENT``` The Apigee Environment you are working in.
  - ```KEY_ID``` The identifier for the key in the key store.
​
​
​
## Run
​
* To run the pytest script:
    * ```$ poetry run pytest```