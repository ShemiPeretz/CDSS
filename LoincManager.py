import requests as requests
from requests.auth import HTTPBasicAuth


class LOINCManager:
    @staticmethod
    def search_test_by_loinc_code(loinc_code):
        base_url = "https://fhir.loinc.org/CodeSystem/$lookup"
        auth = HTTPBasicAuth("shimonperetz", "shimonperetz")
        params = {
            "code": str(loinc_code),
            "system": "http://loinc.org"
        }

        response = requests.get(base_url, params=params, auth=auth)

        if response.status_code == 200:
            data = response.json()
            test_type = LOINCManager.process_loinc_response(data)
            return test_type
        elif response.status_code == 404:
            return "** LOINC Code not found **"
        else:
            return f"Error: {response.status_code}"

    @staticmethod
    def process_loinc_response(data):
        parameters = data['parameter']
        if parameters:
            for param in parameters:
                if param['name'] == 'display':
                    if param['valueString']:
                        return str(param['valueString']).lower()
                    else:
                        print('Error: Could not find display value of the given LOINC_CODE')
        else:
            print('Error: Could not find parameters in loinc.org response')


if __name__ == "__main__":
    # Example usage
    result = LOINCManager.search_loinc_by_code("1474-9")
    print(result)
