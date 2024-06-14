import fnctn

url_logs = "https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/apache_logs/apache_logs"
format = r'(?P<host>\S+) (?P<identity>\S+) (?P<user>\S+) \[(?P<time>.+?)\] "(?P<request>.+?)" (?P<status>\d{3}) (?P<size>\S+)'
logs = fnctn.extract_logs(url_logs)
db_name = 'apache_logs.db'
table_name = 'apache_logs'