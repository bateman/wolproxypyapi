"""FastAPI application for the wolproxypy API.

This is the API module of the wolproxypy application.
It is responsible for the routing of the requests.
The root path is '/' redirects to the '/docs'.
The path '/mac' invokes the wakeonlan core module.
"""
import json
import pathlib

import uvicorn
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from starlette.responses import RedirectResponse
from wolproxypycli import wol

from config import api_config, logger
from wolproxypyapi import parent_module

from .info import contact, description, license_info, terms_of_service, title, version
from .models import ApiKey, Host

REDIRECT_CODE = 301


app = FastAPI(
    title=title,
    description=description,
    version=version,
    license_info=license_info,
    terms_of_service=terms_of_service,
    contact=contact,
)


@app.get("/")
async def root() -> RedirectResponse:
    """Root path, termporarily redirected to doc.

    It will display the web app login and main pages.

    Args:
        None

    Returns:
        RedirectResponse: Redirect to the documentation.
    """
    logger.info("Redirecting to doc")
    return RedirectResponse(url="/docs", status_code=REDIRECT_CODE)


@app.post("/wol")
async def send_wol_packet_mac(host: Host, key: ApiKey) -> JSONResponse:
    """Invoke the module to send a Wake-On-Lan packet to a host.

    The key authentication is automatically performed by the Pydantic validator
    within the ApiKey model.

    Args:
        host: the host to send the packet to.
        key: the API key to authenticate the request.

    Returns:
        JSONResponse: The status of the wake-on-lan packet.
    """
    logger.info(f"Received a request to wake up host {host}")
    status = wol(host.mac_address, host.ip_address, host.port, host.interface)
    content = json.dumps({"status": status})
    logger.info(f"Response: {content}")
    return JSONResponse(content=content)


def run():
    """Run the application."""
    logger.info("Starting wolproxypy API module")
    this_file = pathlib.Path(__file__).name.split(".py")[0]
    # must match the name of the FastAPI app defined above
    # as reported in the app_name variable api.config file
    app_name = api_config["general"]["app_name"]
    api = f"{parent_module}.{this_file}:{app_name}"
    uvicorn.run(
        api,
        reload=bool(api_config["general"]["reload"]),
        host=api_config["net"]["host"],
        port=int(api_config["net"]["port"]),
        log_level=api_config["logging"]["level"],
        debug=bool(api_config["logging"]["debug"]),
    )
