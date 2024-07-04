from schema import dab_response_validator
from time import sleep
from dab_tester import YesNoQuestion, Default_Validations
import jsons

def image(test_result, durationInMs=0,expectedLatencyMs=0):
    try:
        dab_response_validator.validate_output_image_response_schema(test_result.response)
    except Exception as error:
        print("Schema error:", error)
        return False
    response  = jsons.loads(test_result.response)
    if response['status'] != 200:
        return False

    SCREENSHOT_FILENAME = "screenshot.html"

    with open(SCREENSHOT_FILENAME, "w") as outfile:
        outfile.write('<div><img src="' + response['outputImage'] + '"</div>')
    return YesNoQuestion(test_result, f"Verify if the {SCREENSHOT_FILENAME} file was created and contains the screenshot") and Default_Validations(test_result, durationInMs, expectedLatencyMs)
