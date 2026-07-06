There's an Apache-style access log in the working directory. I need you to produce
a small JSON traffic summary from it.

It must satisfy all of the following:

1. /app/report.json exists and is a single valid JSON object.
2. It contains the key "total_requests": an integer equal to the number of
   non-empty lines in the log.
3. It contains the key "unique_ips": an integer equal to the number of
   distinct client IP addresses, where the client IP is the first
   whitespace-separated field of each line.
4. It contains the key "top_path": a string equal to the single most
   frequently requested path, considering requests with methods GET, POST,
   PUT, DELETE, HEAD, or PATCH.

Write your report to /app/report.json.