import requests

DEX_ENDPOINT = ''

def run_query(q):
    request = requests.post(
        f'https://api.thegraph.com/subgraphs/name/{DEX_ENDPOINT}'
        '',
        json={'query': query})
    
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception(f'Query failed; return code is {request.status_code}. {query}')
    

# Add proper pair address below BEFORE running
query = '''{
    swaps(
        where: {
            pair: "",
            timestamp_gte: 1661130000
        }
        orderBy: timestamp,
        orderDirection: desc
    ) {
        amountUSD
        transaction {
            timestamp
        }
    }
}'''

result = run_query(query)
n = 0

for i in result['data']['swaps']:
    n += float(i['amountUSD'])

print(n)