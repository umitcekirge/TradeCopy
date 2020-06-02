TESTNET_URL = "https://testnet.bitmex.com/api/v1/"
MAINNET_URL = "https://www.bitmex.com/api/v1/"

LEADERS = {
    'LEADER_A' : {

        'API_KEY' : '',
        'API_SECRET' : '',
        'ENDPOINT' : TESTNET_URL
    }
}
FOLLOWERS = {
    'FOLLOWER_A' : {

        'API_KEY': '',
        'API_SECRET': '',
        'ENDPOINT': TESTNET_URL,
        'FOLLOWS' : {
            'LEADER_A' : '100%'
        }
    }
}