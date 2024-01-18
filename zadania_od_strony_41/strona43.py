def delete_all_dashes(text):
    result = text.replace("-", "")
    return result

text = '340-23-245-235'

print(delete_all_dashes(text))