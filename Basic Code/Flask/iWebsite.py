from flask import Flask, render_template, url_for, redirect, request
import socket
import ipinfo
import tldextract
import pexpect
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/learn/')
def learn():
    return render_template('learn.html')

@app.route('/measure/')
def measure():
    return render_template('measure.html')

@app.route('/measure/track', methods = ['POST'])
def measure_track():
    if request.method == 'POST':
        error = False

        URL = request.form['URL']

        try:
            def traceroute(url):
                commandStr = 'traceroute -w 1 -q 1 -I ' + url   #Linux / Unix traceroute command
                child = pexpect.spawn(commandStr)               #Creates a child traceroute process

                hopCount = 0
                while 1:                        #runs until process finishes
                    line = child.readline()     #reads each line of stdout
                    if not line: break          #break if reached the end
                    hopCount += 1               #increment

                return hopCount                 #total number of hops
            
            # Gather information about host
            def info(url):
                access_token = '7988f883b8fd54'
                handler = ipinfo.getHandler(access_token)
                ext = tldextract.extract(url)
                domain = ext.registered_domain
                ip_address = socket.gethostbyname(domain)
                details = handler.getDetails(ip_address)
                return details.all

            #Produce the report on your desktop 
            def report(url,address):
                stream = os.popen('lighthouse --quiet --no-update-notifier --no-enable-error-reporting --output=json --output-path=' + address + 'Report.json --chrome-flags="--headless" ' + url)
            path = os.getcwd()
            print(path)
            report(URL,path)
            count = traceroute(URL);
            details = info(URL);

            return render_template('measure_result.html', count=count, details=details)

        except:
            error = True
            return render_template('measure.html',error=error)

@app.route('/measure_result')
def measure_result():
    # Extract datas from the files
    return render_template('measure_result.html')

if __name__ == "__main__":
    app.debug = True
    app.run(port=5000)