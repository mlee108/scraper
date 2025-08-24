import json
import requests
import time

from product import Product

# settings
base_url = 'https://search.costco.com/api/apps/www_costco_com/query/www_costco_com_search?locale=en-US&start=0&expand=false&userLocation=WA&loc=115-bd%2C8-wh%2C1250-3pl%2C1321-wm%2C1456-3pl%2C283-wm%2C561-wm%2C725-wm%2C731-wm%2C758-wm%2C759-wm%2C847_0-cor%2C847_0-cwt%2C847_0-edi%2C847_0-ehs%2C847_0-membership%2C847_0-mpt%2C847_0-spc%2C847_0-wm%2C847_1-cwt%2C847_1-edi%2C847_d-fis%2C847_lg_n1f-edi%2C847_lux_us01-edi%2C847_NA-cor%2C847_NA-pharmacy%2C847_NA-wm%2C847_ss_u362-edi%2C847_wp_r458-edi%2C951-wm%2C952-wm%2C9847-wcs&whloc=8-wh&q='
request_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
    'x-api-key': '', # insert api key here
}
search_terms = [
    'ramen',
    'switch',
    'lego',
    ]

for term in search_terms:
    url = base_url + term

    # getting product listings from Costco
    try:
        response = requests.get(url, headers=request_headers)
        json_response = response.json()
    except:
        print('Exception occurred while trying to retrieve api response')
        raise

    products = json_response['response']['docs']

    # extracting relevant info from Costco's json response
    result = []
    for p in products:
        name = p['name']
        price = p.get('item_location_pricing_salePrice')
        rating = p.get('item_ratings')

        product = Product(name, price, rating)
        result.append(product)

    with open(f'{term}.json', 'w', encoding='utf-8') as f:
        json.dump(result, f, indent=4, default=lambda o: o.__dict__)

    # wait for 5 seconds just in case to avoid any bans
    print(f'Finished querying {term}, sleeping for 5 seconds')
    time.sleep(5)