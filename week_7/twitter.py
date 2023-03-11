import re

url = input("URL: ").strip()

# username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)
if matches := re.search(r"^(?:https?://)?(?:www\.)?twitter\.com/(.+)$", url, flags=re.IGNORECASE):
    print(matches.group(1))
