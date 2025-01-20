import azure.functions as func
import logging

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.route(route="sample")
def sample(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "Hi This is sanath Kumar Reddy K.
             A YAML file is a simple and easy-to-read file format used to store information like settings or data. It is commonly used to configure applications and tools. YAML files use spaces and indentation to organize data, making them clean and human-friendly.",
             status_code=200
        )
    