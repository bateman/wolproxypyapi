"""
Retrieve the path of the parent module to dynamically build the name of FastAPI app.
"""
import pathlib

parent_module = pathlib.Path(__file__).parent.name
