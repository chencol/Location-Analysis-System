import jwt

b_token = jwt.encode({"username":"Colin"}, 'secret', algorithm='HS256')
str_b_token = b_token.decode("utf-8")
b_token = str_b_token.encode("utf-8")

print(jwt.decode(b_token,"secret"))



