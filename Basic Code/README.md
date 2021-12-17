# Flask Explanation
## How To Run Our Prototype
    Use iWebsite.py:
        1.Download the whole Flask directory
        2.Run the python file iWebsite.py
        3.Paste 'http://127.0.0.1:5000/' as URL in browser

    Use iWebsite.ipy:
        1.Download the whole Flask directory
        2.Open Jupyter Notebook to run iWebsite.ipy
        3.Click the link in the output

<br>
<br>
<br>

# IPDemo.js Explanation
## How It Works
- Note: User must have node.js installed as well as the 'node-ipinfo' node module installed in the same directory as ipDemo.js
- Run script by typing 'node .\ipDemo.js [domain name]' into Command Line
- dns package converts domain name into an IP address
- IPInfo API receives this address and provides geolocation data on the address
## Discrepancies
- Comparing the results of location of the same IP sometimes returns slightly different locations
    - The IPInfo API suggests nottingham.ac.uk is located in London
    - https://sitechecker.pro/hosting-checker/ suggests nottingham.ac.uk is located in Ludlow
    - However, comparing against other university websites, such as Cambridge and Derby, the same results are returned, so this potential inaccuracy is not necessarily widespread
- The DNS resolve4() method can return a different IP address to sitechecker.pro
    - resolve4() returns a different IP address to the one returned by sitechecker
    - sitechecker suggests ntu.ac.uk is located in Shoreditch
    - the IPInfo API suggests it is located in Sydney
    - hostingchecker.com also suggests ntu.ac.uk is in Sydney - it provides the same IP as the one resolve4() returns
    - There is a clear discrepancy in locating the nearest server to access
