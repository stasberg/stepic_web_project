def app(environ, start_response):
    body = [bytes("\r\n".join(environ["QUERY_STRING"].split("&")), encoding="utf8")]
    status = "200 OK"
    headers = [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(body)))
    ]
    start_response(status, headers)
    return body
