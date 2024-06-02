import requests

def test_github_api_status_code():
# Make an API call and check the response.
    url = "https://api.github.com/search/repositories"
    url += "?q=language:javascript+sort:stars+stars:>10000"

    headers = {"Accept": "application/vnd.github.v3+json"}
    r = requests.get(url, headers=headers)

    assert r.status_code == 200

if __name__ == "__main__":
    import pytest
    pytest.main()