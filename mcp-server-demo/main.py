# server.py
from mcp.server.fastmcp import FastMCP
import os

# Create an MCP server
app = FastMCP("Demo")
 


# notes_file = "C:\\Users\\DanielWu\\Desktop\\notes.txt"

# def ensure_file_exists(file_path):
#     if not os.path.exists(file_path):
#         with open(file_path, "w") as f:
#             f.write("")


# @app.tool()
# def add_note(note: str) -> str:
#     """
#     Add a note to the notes file
#     Args:
#         note: The note to add to the notes file
#     Returns:
#         A message indicating that the note was added successfully
#     """
#     ensure_file_exists(notes_file)
#     with open(notes_file, "a") as f:
#         f.write(note + "\n")
#     return "Note added successfully"



@app.tool()
def usd_to_gbp(amount: float) -> float:
    """Convert USD(dollars) to GBP(pounds sterling)"""
    exchangeRate = 0.79
    return round(amount * exchangeRate, 2)


# Add an addition tool
@app.tool()
def sum(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# Add a dynamic greeting resource
@app.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"
