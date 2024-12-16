import logging
import json
import azure.functions as func
import psutil

def main(req: func.HttpRequest) -> func.HttpResponse:
 logging.info('Python HTTP trigger function processed a request.')

 # Get the number of CPU cores
 cpu_cores = psutil.cpu_count()

 # Add the CPU cores to the JSON response
 response = {
 'method': req.method,
 'url': req.url,
 'headers': dict(req.headers),
 'params': dict(req.params),
 'get_body': req.get_body().decode(),
 'cpu_cores': cpu_cores
 }

 return func.HttpResponse(json.dumps(response))
