const { IPinfoWrapper } = require('node-ipinfo');
const dns = require("dns");

let ipinfo = new IPinfoWrapper("7988f883b8fd54");
let url = process.argv[2];
let ip;

async function getIP()
{
    if(process.argv[2])
    {
        dns.resolve4(url, (err, addresses) =>
        {
            if(err)
            {
                console.log(err);
                return;
            }

            ip = addresses[0];
            
            ipinfo.lookupIp(ip).then((response) => 
            {
                console.log(response);
            })
        });
    }
}

getIP();