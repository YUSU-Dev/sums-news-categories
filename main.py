import requests
import csv


def fetchData(session, url, xSiteId, parms):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64)",
        "X-Site-Id": xSiteId,
    }
    response = session.get(url, headers=headers, params=parms)
    return response.json()


def getAllItems(url, xSiteId):
    with requests.Session() as session:
        values = {
            "perPage": 200,
            "page": 1,
        }

        foundAllNews = False

        data = []

        while not foundAllNews:
            jsonData = fetchData(session, url, xSiteId, values)
            data = data + jsonData["data"]
            if jsonData["next_page_url"] is None:
                foundAllNews = True
            else:
                values["page"] += 1
        return data


def searchCategory(categories, id):
    for category in categories:
        if category["id"] == id:
            return [category["id"], category["name"]]
    return None


def main():
    xSiteId = input("Please enter your X-Site-Id: ")
    news = getAllItems(
        "https://pluto.sums.su/api/news",
        xSiteId,
    )
    categories = getAllItems(
        "https://pluto.sums.su/api/news/categories",
        xSiteId,
    )
    with open("data.csv", "w", newline="") as csvfile:
        fieldnames = ["title", "categories"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for item in news:
            newsCategory = []
            for category in item["categories"]:
                category = searchCategory(categories, category)
                newsCategory.append(category)

            writer.writerow({"title": item["title"], "categories": newsCategory})


if __name__ == "__main__":
    main()
