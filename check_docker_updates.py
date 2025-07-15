import requests

def check_latest_tag(repo):
    url = f"https://hub.docker.com/v2/repositories/{repo}/tags?page_size=1"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        if data['results']:
            latest_tag = data['results'][0]['name']
            print(f"✅ Latest tag for {repo}: {latest_tag}")
        else:
            print(f"⚠️ No tags found for {repo}")
    else:
        print(f"❌ Failed to fetch tags for {repo} (Status: {response.status_code})")

if __name__ == "__main__":
    check_latest_tag("neima/clms-backend")
    check_latest_tag("neima/clms-frontend")  
