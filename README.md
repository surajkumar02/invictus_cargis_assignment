# invictus_cargis_assignment

For Virtualenv:

    python3/python/py -m pip install --user virtualenv

    python3/python/py -m venv env

Activate env:

    source env/bin/activate (Linux)
    
     .\env\Scripts\activate (Windows)
    
    cd invictus_cargis_assignment
    
    pip install -r requirements.txt

    python migrate

    python app.py runserver 10001 (for port:10001)

    else:

    python app.py runserver (for default port:8000)
    
    
API:

    url:  localhost:10001(or 8000)/api?param(s)
    
    
  The entire list sorted by the item’s price (Ascending and Descending) -
  
      getsorteddata?reverse=True&criteria=price
      
  Any single item by:
  
      Id - getitem?id=AAsm
      Location - getitem?location=AAsm
      
  List of items by:
  
      Status - getitemslist?status=AAsm
      userId - getitemslist?userid=AAsm
      
  An array of items based on radius 
  
      Location specified by coordinate - get_items_in_radius?radius=xy&latitude=xx&longitude=yy
