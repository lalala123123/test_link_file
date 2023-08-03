import os

from promptflow import tool
from promptflow.connections import CustomConnection

from fetch_text_content_from_url import fetch_text_content_from_url


@tool
def fetch_text_content_from_url_tool(
    url,
    connection: CustomConnection) -> str:

    # set environment variables
    for key, value in connection.items():
        os.environ[key] = value

    # call the entry function
    return fetch_text_content_from_url(
        url=url,
    )