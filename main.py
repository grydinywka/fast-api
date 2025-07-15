# This is a sample Python script.

# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/

from fastapi import FastAPI, Request, Query

# Create a FastAPI application
app = FastAPI()

# Define a route at the root web address ("/")
@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

@app.get("/a/")
def read_root(request: Request):
    return {"method": request.method, "url": request.url}


@app.get("/items/")
def read_items(q: str = Query(..., min_length = 3, max_length = 50)):
    print(q, "q")
    results = []
    return results