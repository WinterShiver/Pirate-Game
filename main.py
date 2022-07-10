import argparse
import math
import random
eps = 1e-6

parser = argparse.ArgumentParser()
parser.add_argument('-m', type=int, default=100, metavar='N',
                    help='The number of coins.')
parser.add_argument('-n', type=int, default=5, metavar='N',
                    help='The number of pirates.')
parser.add_argument('--casting', action='store_true', 
                    help='A distribution plan would be approved when no less than half of pirates agree to it.')
parser.add_argument('--noprint-fail', action='store_true',
                    help='Do not print information when a distribution plan is not approved.')
args = parser.parse_args()

# Initialization: m coins, n pirates; the distribution for pirate #1

m, n = args.m, args.n
assert m >= 1 and n > 1

last_valid_distribution = {
    'id': 1,
    'scheme': [
        {
            'pirates': [1],
            'coin': m,
            'supporters': 1  
            # `supporters`: the number of pirates in the list `pirates` 
            #   that could get `coin` coins and support the scheme.
            #   the rest pirates in `pirates` do not get any coins 
            #   and would not support this scheme.
        }
    ]
}
    
# develop distribution for pirate #i

for i in range(2, n+1):
    # for pirate #1~#i-1, calculate the expected coins they would get 
    # in the last valid distribution; also the variance. 
    # if they would die in the last valid distribution, the expected value is -1
    expected = []
    for item in last_valid_distribution['scheme']:
        p = item['supporters'] / len(item['pirates'])
        exp = item['coin'] * p
        var = item['coin'] ** 2 * p * (1-p)
        expected.append({
            'exp': (exp, var),
            'pirates': item['pirates']
        })
    if last_valid_distribution['id'] < i-1:
        expected.append({
            'exp': (-1, 0),
            'pirates': list(range(last_valid_distribution['id']+1, i))
        })
    # for pirate #1~#i-1, calculate the least coins required if they support the scheme
    required = {}
    for item in expected:
        if item['exp'][1] == 0:
            required_coin = math.ceil(item['exp'][0] + eps)
        else:
            required_coin = math.ceil(item['exp'][0])
        if required_coin in required:
            required[required_coin].extend(item['pirates'])
        else:
            required[required_coin] = item['pirates']
    required = {k: sorted(required[k]) for k in sorted(required.keys())}
    # develop distribution for pirate #i
    # initialization
    distribution = {
        'id': i,
        'scheme': []
    }
    required_supporters = (i-1) // 2 if args.casting else i // 2 # number of supporters required, besides of pirate #i
    curr_supporters = 0
    curr_coins = 0
    # distribute coins to pirates that requires least coins, until we get enough supporters
    pirates_0 = []  # pirates that would not get any coins and would not support this scheme
    for coin, pirates in required.items():
        if curr_supporters < required_supporters: 
            supporters = min(len(pirates), required_supporters - curr_supporters)
            scheme_item = {
                'pirates': pirates,
                'coin': coin,
                'supporters': supporters
            }
            distribution['scheme'].append(scheme_item)
            curr_supporters += supporters
            curr_coins += supporters * coin
        else:
            pirates_0.extend(pirates)
    # the rest pirates (pirates_0) would not get any coins and would not support this scheme
    if len(pirates_0) > 0:
        scheme_item = {
            'pirates': pirates_0,
            'coin': 0,
            'supporters': 0
        }
        distribution['scheme'].append(scheme_item)
    # check if this distribution is valid
    if curr_coins > m: 
        # this distribution is not valid
        # we cannot develop a valid distribution for pirate #i
        if not args.noprint_fail:
            print('*******************************************************************')
            print(
                f"Distribution for pirate #{distribution['id']} with {m} coins would fail")
        continue
    # since this distribution is valid, decide the number of coins for pirate #i
    # and add the item for pirate #i to scheme
    coin_i = m - curr_coins
    for idx, item in enumerate(distribution['scheme']):
        if item['coin'] == coin_i and item['supporters'] == len(item['pirates']):
            distribution['scheme'][idx]['pirates'].append(i)
            distribution['scheme'][idx]['supporters'] += 1
            break
    else:
        distribution['scheme'].append({
            'pirates': [i],
            'coin': coin_i,
            'supporters': 1
        })
    # archive the distribution for pirate #i
    last_valid_distribution = distribution

    # display the result

    # develop a sample distribution for display
    sample_distribution = {}
    supporters = []
    for item in distribution['scheme']:
        supporters_item = random.sample(item['pirates'], item['supporters'])
        if item['coin'] in sample_distribution:
            sample_distribution[item['coin']].extend(supporters_item)
        elif item['coin'] > 0:
            sample_distribution[item['coin']] = supporters_item
        supporters.extend(supporters_item)
    sample_distribution = {
        k: sorted(sample_distribution[k]) for k in sorted(sample_distribution.keys())}
    supporters.sort()
    if args.casting:
        assert len(supporters) >= distribution['id'] / 2
    else:
        assert len(supporters) > distribution['id'] / 2
    # sample distribution as a list
    sample_distribution_list = [0 for i in range(distribution['id'])]
    for coin, pirates in sample_distribution.items():
        for pirate in pirates:
            sample_distribution_list[pirate-1] = coin
    # displays
    print('*******************************************************************')
    print(
        f"A sample distribution for pirate #{distribution['id']} when there are {m} coins")
    print(sample_distribution_list)
    print(f'Supporters: {supporters}')
    print(f"Support rate: {len(supporters)}/{distribution['id']}")
