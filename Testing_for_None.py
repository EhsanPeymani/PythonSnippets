# taken from talkpython.fm
def find_accounts(search_text):
    db_is_available = False

    if not db_is_available:
        return None

    return 1


accounts = find_accounts('python')

# test for None using 'is' or 'is not'
if accounts is None:
    print('No accounts returned')
else:
    print('{} account(s) returned'.format(accounts))