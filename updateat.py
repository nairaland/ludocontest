import sys
import requests
from datetime import datetime, timedelta, timezone

def format_date(date_str):
    if not date_str:
        return "N/A"
    # GitHub returns dates in ISO 8601 format: 2023-12-18T10:00:00Z
    try:
        dt = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
    except ValueError:
        try:
            # Handle potential variation in ISO format
            dt = datetime.fromisoformat(date_str.replace('Z', '+00:00'))
        except ValueError:
            return date_str

    # Convert to WAT (UTC+1)
    wat_tz = timezone(timedelta(hours=1))
    wat_dt = dt.astimezone(wat_tz)
    
    # Format: Month Day, Hour:Minuteam/pm WAT
    month = wat_dt.strftime("%B")
    day = wat_dt.strftime("%d").lstrip('0')
    time_str = wat_dt.strftime("%I:%M%p").lower()
    
    # Remove leading zero from hour if present (e.g., 01:00am -> 1:00am)
    if time_str.startswith('0'):
        time_str = time_str[1:]
    
    return f"{month} {day}, {time_str} WAT"

def extract_owner_repo(url):
    # Remove .git suffix and trailing slashes
    url = url.strip()
    if url.endswith('.git'):
        url = url[:-4]
    url = url.rstrip('/')
    
    if 'github.com' not in url:
        return None, None
        
    # Handle both https://github.com/owner/repo and git@github.com:owner/repo
    if 'github.com:' in url:
        # git@github.com:owner/repo
        path = url.split('github.com:')[-1]
    elif 'github.com/' in url:
        # https://github.com/owner/repo
        path = url.split('github.com/')[-1]
    else:
        return None, None
        
    parts = path.split('/')
    if len(parts) >= 2:
        return parts[0], parts[1]
    return None, None

def main():
    if len(sys.argv) < 2:
        print("Usage: python updateat.py <github_url>")
        sys.exit(1)

    url = sys.argv[1]
    owner, repo = extract_owner_repo(url)
    
    if not owner or not repo:
        print("Error: Could not extract owner and repo from URL")
        sys.exit(1)
        
    api_url = f"https://api.github.com/repos/{owner}/{repo}"
    headers = {'Accept': 'application/vnd.github.v3+json'}
    
    try:
        response = requests.get(api_url, headers=headers)
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching repo data: {e}")
        sys.exit(1)
    
    # The three variables: pushed_at, updated_at, and created_at
    pushed_at = data.get('pushed_at')
    updated_at = data.get('updated_at')
    created_at = data.get('created_at')
    
    print(f"pushed_at: {format_date(pushed_at)}")
    print(f"updated_at: {format_date(updated_at)}")
    print(f"created_at: {format_date(created_at)}")

if __name__ == "__main__":
    main()

