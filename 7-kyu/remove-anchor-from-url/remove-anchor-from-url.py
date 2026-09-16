def remove_url_anchor(url):
    end = url.find('#')
    return url[:end] if end != -1 else url