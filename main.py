import requests


def distinct_minter(sc_adress, method_name):
    values = set()
    i = 0
    from_value = (i * 10000).__str__()
    size = ((i + 1) * 10000).__str__()
    response = requests.get(
        "https://api.elrond.com/transactions?receiver=" + sc_adress + "&function=" + method_name + "&from=" + from_value + "&size=" + size)
    while response.status_code == 200:
        for data in response.json():
            if data["status"] == "success":
                values.add(data["sender"])
        from_value = (i * 10000).__str__()
        size = ((i + 1) * 10000).__str__()
        i += 1
        response = requests.get(
            "https://api.elrond.com/transactions?receiver=" + sc_adress + "&function=" + method_name + "&from=" + from_value + "&size=" + size)

    return values


if __name__ == '__main__':
    sc_adress = "erd1qqqqqqqqqqqqqpgqup56pfvlh6s3grlrx08jt06ksa35kqxu548sj7cxpt"
    whitelist_mint = distinct_minter(sc_adress, "MintTokens")
    print(len(whitelist_mint))
