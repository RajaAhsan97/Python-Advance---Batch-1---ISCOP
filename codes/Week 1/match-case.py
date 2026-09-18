# HTTP status
# 200 --> success
# 400 --> Bad request
# 404 --> Page not found

code = 505

match code:
    case 200:
        print("Success")
    case 400:
        print("Bad Request")
    case 404 | 505:
        print("Not Found")

#if x > 5 or x <5: