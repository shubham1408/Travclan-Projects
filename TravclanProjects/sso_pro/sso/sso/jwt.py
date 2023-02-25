import jwt
from jwt import DecodeError
from jwt.algorithms import RSAAlgorithm

from rest_framework_jwt.settings import api_settings

from django.contrib.auth import authenticate

import json, time, requests, datetime
# from django.contrib.auth.models import User
# from common.services.system import dbg_message
import urllib.request
from jose import jwk, jwt
from jose.utils import base64url_decode
from jose.exceptions import JWTError
from django.conf import settings
from rest_framework import exceptions


def get_username_from_payload_handler(payload):
    username = payload.get('sub')
    authenticate(remote_user=username)
    return username


def cognito_jwt_decode_handler(token):
    """
    To verify the signature of an Amazon Cognito JWT, first search for the public key with a key ID that
    matches the key ID in the header of the token. (c)
    https://aws.amazon.com/premiumsupport/knowledge-center/decode-verify-cognito-json-token/
    Almost the same as default 'rest_framework_jwt.utils.jwt_decode_handler', but 'secret_key' feature is skipped
    """    
    # options = {'verify_exp': api_settings.JWT_VERIFY_EXPIRATION}
    # unverified_header = jwt.get_unverified_header(token)
    # if 'kid' not in unverified_header:
    #     raise DecodeError('Incorrect authentication credentials.')

    # kid = unverified_header['kid']
    # try:
    #     # pick a proper public key according to `kid` from token header
    #     public_key = RSAAlgorithm.from_jwk(api_settings.JWT_PUBLIC_KEY[kid])
    # except KeyError:
    #     # in this place we could refresh cached jwks and try again
    #     raise DecodeError('Can\'t find proper public key in jwks')
    # else:
    #     return jwt.decode(
    #         token,
    #         public_key,
    #         api_settings.JWT_VERIFY,
    #         options=options,
    #         leeway=api_settings.JWT_LEEWAY,
    #         audience=api_settings.JWT_AUDIENCE,
    #         issuer=api_settings.JWT_ISSUER,
    #         algorithms=[api_settings.JWT_ALGORITHM]
    #     )

    with urllib.request.urlopen(settings.AWS_KEYS_URL) as f:
        response = f.read()
    keys = json.loads(response.decode('utf-8'))['keys']
    print(keys)
    # token = 'eyJraWQiOiJTMTVzRWU2ZmdXUjdEbngrMjErNGNoWmJ4cjZSYzBYRnVTS1VHTEpieW9RPSIsImFsZyI6IlJTMjU2In0.eyJhdF9oYXNoIjoiME1adkRKbFFfYnlna0F4aEZlRklUdyIsInN1YiI6IjEyODJlNDg5LTM5ZmUtNGMxNi05ZTg4LWQ3ZWFiN2Q2MTc0MyIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAuYXAtc291dGgtMS5hbWF6b25hd3MuY29tXC9hcC1zb3V0aC0xX3lib3NQekdOOCIsImNvZ25pdG86dXNlcm5hbWUiOiJzaHViaGFtLmR3aXZlZGkiLCJhdWQiOiIzajdudmFvMGpob3RnYWUzcnZsdWpzbGRpNyIsImV2ZW50X2lkIjoiMWU0ODlkMWQtYzYwNC00NDFkLTk3YTctNTUwNDMzMWM0NjQ1IiwidG9rZW5fdXNlIjoiaWQiLCJhdXRoX3RpbWUiOjE2MzczMDUyMTQsImV4cCI6MTYzNzM5MTYxNCwiaWF0IjoxNjM3MzA1MjE0LCJqdGkiOiI5MTU3ZjcwOS01ZTk5LTRhZTQtODA5Zi1hZjk1Njc0MzM5MTIiLCJlbWFpbCI6InNodWJoYW0uZHdpdmVkaUB0cmF2Y2xhbi5jb20ifQ.39-7cz8LNd0ya1FVCSk3JQi1noI1WIK0cvAW5wHnklLz2aP6JDMHnRTglIICeZQQND23K0xPHAkSlelIM_6QNsIFY0aHixkumWQ62OfnG9ZzUQe_VU2p2GsP9SwwZZNHheMiL80n7xGidotTZlj97iMollZ8BmH5gq4WFjGlBv5Jd7Ze2y1z0krwmL_kK-K2bYs9whfmtocHJIL6qGeGFfQ-kQIDUY_MRvlvcJCEartK-_KWMKT16PLiODs7LcqXsI4KwVzIkAPoLVMn9zTdFf1fb8rV0ZFO7cuIQeAHQ0tMPkaR-KkU5E8xixao6QP7KvTtuJRno-Q4neD8Hm69Ew'
    token = 'eyJraWQiOiJTMTVzRWU2ZmdXUjdEbngrMjErNGNoWmJ4cjZSYzBYRnVTS1VHTEpieW9RPSIsImFsZyI6IlJTMjU2In0.eyJhdF9oYXNoIjoicXNJSFdkQThBbmJvUXl0TlpyRk1NZyIsInN1YiI6IjU5N2ZkOWE4LTY4YjQtNDNhMC04ZDdmLWYyOTQxYTAyOTc4ZCIsImNvZ25pdG86Z3JvdXBzIjpbImFwLXNvdXRoLTFfeWJvc1B6R044X0dvb2dsZSJdLCJlbWFpbF92ZXJpZmllZCI6ZmFsc2UsImlzcyI6Imh0dHBzOlwvXC9jb2duaXRvLWlkcC5hcC1zb3V0aC0xLmFtYXpvbmF3cy5jb21cL2FwLXNvdXRoLTFfeWJvc1B6R044IiwiY29nbml0bzp1c2VybmFtZSI6Imdvb2dsZV8xMTc1Mjk3OTQ2ODM5ODAyMzU1NjAiLCJhdWQiOiIzajdudmFvMGpob3RnYWUzcnZsdWpzbGRpNyIsImlkZW50aXRpZXMiOlt7InVzZXJJZCI6IjExNzUyOTc5NDY4Mzk4MDIzNTU2MCIsInByb3ZpZGVyTmFtZSI6Ikdvb2dsZSIsInByb3ZpZGVyVHlwZSI6Ikdvb2dsZSIsImlzc3VlciI6bnVsbCwicHJpbWFyeSI6InRydWUiLCJkYXRlQ3JlYXRlZCI6IjE2MzczMDE5NTA3ODAifV0sInRva2VuX3VzZSI6ImlkIiwiYXV0aF90aW1lIjoxNjM5OTk4NzY4LCJleHAiOjE2NDAwODUxNjgsImlhdCI6MTYzOTk5ODc2OCwianRpIjoiMGM4ZTNmZmQtNzFlMC00ZmI2LThkZGYtMGNhOTljMGI5NDY2IiwiZW1haWwiOiJwdXNocGVuZHJhLmd1cHRhQHRyYXZjbGFuLmNvbSJ9.eCf2WDi0SOECzKu-JRopgy8psbgBpYAWz1LjN7fXjIZn2ibPTWKadLjKTi3cOtpMJVasKUExeiIqTXFvjk99mLzQ_QHki-Cv8CmtL_lyzho2gNeQTEUbzErVi_jv7wawvaumP9MZH2XftR1HjgMJ0LyTRXIkX80o3l2jvnMiIX_xWePvN7Fiz1qFSx4yaqrD0H6feiFYtByXr0XvJmGPSVYUI1GewPFTBCDUfmTfVvrOPwB8B8tKMCTr_NVgb68U9G-CEU-fyvp5Ld6yTl-fv2tey6jrkAyz7O303YkTopVbAY1Wvyh4_oRe0GNFmo6eem0ZQgpGoRp63kq6CVZLwg'
    try:
        headers = jwt.get_unverified_headers(token)
    except JWTError:
        raise exceptions.PermissionDenied()
    kid = headers['kid']
    print(kid)
    key_index = -1
    for i in range(len(keys)):
        if kid == keys[i]['kid']:
            key_index = i
            print("i========>", i)
            break
    if key_index == -1:
        print('Public key not found in jwks.json')
        raise exceptions.PermissionDenied()

    print('keys[key_index]==>', keys[key_index])
    public_key = jwk.construct(keys[key_index])
    print('public_key==>', public_key)
    # get the last two sections of the token,
    # message and signature (encoded in base64)
    message, encoded_signature = str(token).rsplit('.', 1)
    print('message ======>', message)
    print('encoded_signature ======>', encoded_signature)
    # decode the signature
    decoded_signature = base64url_decode(encoded_signature.encode('utf-8'))
    print('decoded_signature========>', decoded_signature)
    print('message.encode("utf8")', message.encode("utf8"))
    status = public_key.verify(message.encode("utf8"), decoded_signature)
    print("status======>", status)
    if not status:
        raise exceptions.PermissionDenied()            
    claims = jwt.get_unverified_claims(token)
    print('claims====>', claims)
    return claims
