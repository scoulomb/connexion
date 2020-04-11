# To launch unit test

See travis file, it launches tox and prereq
perform prereq
install tox and run tox:
sudo apt install tox
tox

where can reduce python version in tox file

or as done in tox, at project root do
python3 setup.py test

Failed aussi sur master !


Note:
assert not utils.is_json_mimetype("application")
pytestsynthax different from pyunit
https://learning.oreilly.com/library/view/python-testing-with/9781680502848/f_0020.xhtml
and was not managing this case correctly because of /missing

it passed!!

# Running kind of non reg

Switching to this branch
https://github.com/scoulomb/zalando_connexion_sample/compare/buildLocalLib?expand=1


And launching reproduce.sh
Adding eventually rm -rf ./connexion to update folder

And I still have same result as original fix:
Which is the expected new behavior

''''
curl_1    | + curl --request POST --header Content-Type: application/json; charset=utf-8 http://server:8080/api/v1/test/entry --data {"kind" "time"}
curl_1    |   % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
curl_1    |                                  Dload  Upload   Total   Spent    Left  Speed
server_1  | 172.19.0.3 - - [11/Apr/2020 15:46:20] "POST /api/v1/test/entry HTTP/1.1" 400 -
100   110  100    95  100    15  12602   1989 --:--:-- --:--:-- --:--:-- 13571
curl_1    | {"errors":["BadRequestProblem()","Request body is not valid JSON","Bad Request"],"status":400}
''''

Original fix: https://github.com/scoulomb/zalando_connexion_sample/compare/buildLocalLib?expand=1

So we do not raise invalid JSON
but invalid body
https://github.com/zalando/connexion/issues/1202

I can in copied conenxion folder in this branch come back to initial code

'''

def is_json_mimetype(mimetype):
    """
    :type mimetype: str
    :rtype: bool
    """
    maintype, subtype = mimetype.split('/')  # type: str, str
    return maintype == 'application' and (subtype == 'json' or subtype.endswith('+json'))

''''

and do not use script to not overwrite
So do

'''
sudo docker-compose build
sudo docker-compose up
''''

We should come back to old behaviour invalid media type

''''
server_1  | 172.19.0.3 - - [11/Apr/2020 15:59:06] "POST /api/v1/test/entry HTTP/1.1" 415 -
100   231  100   216  100    15  28711   1993 --:--:-- --:--:-- --:--:-- 30857
curl_1    | {"errors":["UnsupportedMediaTypeProblem('Invalid Content-type (application/json; charset=utf-8), expected JSON data')",null,"Invalid Content-type (application/json; charset=utf-8), expected JSON data"],"status":415}
zalando_connexion_sample_curl_1 exited with code 0
^CGracefully stopping... (press Ctrl+C again to force)
''''

Which is the case;
And when we were using karate as it as sending the charset ans we
did not handle 415 invalid media type we had a 500;

Whereas 400 invalid json was handled

OKOK