# Format date
def format_date(date):
  return date.strftime('%m/%d/%y')

# Format URL
def format_url(url):
  return url.replace('http://', '').replace('https://', '').replace('www.', '').split('/')[0].split('?')[0]

# Format word pluralization
def format_plural(amount, word):
  if amount != 1:
    return word + 's'

  return word