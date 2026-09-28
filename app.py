import urllib.request
import ctypes
import sys

def feed_to_tally():
    # Tally ka address aur port
    tally_url = "http://localhost:9000"
    
    # Tally ki bhasha mein Dummy Transaction (XML)
    xml_data = """<ENVELOPE>
        <HEADER><TALLYREQUEST>Import Data</TALLYREQUEST></HEADER>
        <BODY>
            <IMPORTDATA>
                <REQUESTDESC>
                    <REPORTNAME>Vouchers</REPORTNAME>
                    <STATICVARIABLES><SVCURRENTCOMPANY>Demo Company</SVCURRENTCOMPANY></STATICVARIABLES>
                </REQUESTDESC>
                <REQUESTDATA>
                    <TALLYMESSAGE xmlns:UDF="TallyUDF">
                        <VOUCHER VCHTYPE="Receipt" ACTION="Create" OBJVIEW="Accounting VoucherView">
                            <DATE>20260401</DATE>
                            <VOUCHERNUMBER>DUMMY777</VOUCHERNUMBER>
                            <PARTYLEDGERNAME>Cash</PARTYLEDGERNAME>
                            <PERSISTEDVIEW>Accounting VoucherView</PERSISTEDVIEW>
                            <ALLLEDGERENTRIES.LIST>
                                <LEDGERNAME>Cash</LEDGERNAME>
                                <ISDEEMEDPOSITIVE>YES</ISDEEMEDPOSITIVE>
                                <AMOUNT>-5000.00</AMOUNT>
                            </ALLLEDGERENTRIES.LIST>
                            <ALLLEDGERENTRIES.LIST>
                                <LEDGERNAME>Suspense A/c</LEDGERNAME>
                                <ISDEEMEDPOSITIVE>NO</ISDEEMEDPOSITIVE>
                                <AMOUNT>5000.00</AMOUNT>
                            </ALLLEDGERENTRIES.LIST>
                        </VOUCHER>
                    </TALLYMESSAGE>
                </REQUESTDATA>
            </IMPORTDATA>
        </BODY>
    </ENVELOPE>"""

    try:
        # Tally ko direct data bhejna
        req = urllib.request.Request(tally_url, data=xml_data.encode('utf-8'), headers={'Content-Type': 'text/xml'})
        with urllib.request.urlopen(req, timeout=5) as response:
            res_body = response.read().decode('utf-8')
            
        # Check karna ki Tally ne accept kiya ya nahi
        if "CREATED: 1" in res_body:
            ctypes.windll.user32.MessageBoxW(0, "Success: Dummy Transaction Tally mein feed ho gaya!", "Tally Feeder", 64)
        else:
            ctypes.windll.user32.MessageBoxW(0, "Error: Tally ne data accept nahi kiya. Company Name check karein.", "Tally Feeder", 48)
            
    except Exception as e:
        ctypes.windll.user32.MessageBoxW(0, "Error: Tally se connect nahi ho paye! Kya Tally ON hai?", "Tally Feeder", 16)

if __name__ == "__main__":
    feed_to_tally()
