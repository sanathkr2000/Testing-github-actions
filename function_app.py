import azure.functions as func
import logging

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.route(route="sample")
def sample(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    # Extract the name parameter from the request
    name = req.params.get('name')
    
    if not name:
        try:
            # Try to get name from the JSON body of the request
            req_body = req.get_json()
        except ValueError:
            # Handle exception if the body is not JSON
            pass
        else:
            name = req_body.get('name')

    # Respond based on whether the name was found
    if name:
        # Personalized message if name is provided
        return func.HttpResponse(f"Hello, {name}! Welcome to the Azure Functions platform. We hope you enjoy working with serverless architecture and explore all its capabilities.")
    else:
        # Default message when no name is provided
        return func.HttpResponse(
            "Hi, this is Sanath Kumar Reddy K. Welcome to the world of serverless computing. Azure Functions allow you to run small pieces of code without managing infrastructure, making it easy to scale and handle events in a cost-efficient manner.",
            status_code=200
        )
