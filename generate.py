import random
import string

def generate_random_redirects(num_redirects):
    redirects = []
    for _ in range(num_redirects):
        source = ''.join(random.choice(string.ascii_lowercase) for _ in range(10))
        target = ''.join(random.choice(string.ascii_lowercase) for _ in range(10))
        redirect = f'RewriteRule ^/{source}$ https://dev.interbau-ag.de/{target} [R=301,L]'
        redirects.append(redirect)
    return redirects

def generate_mywebsite_conf(num_redirects):
    redirects = generate_random_redirects(num_redirects)
    redirects.append('RewriteRule ^(.*)$ https://dev.interbau-ag.de/$1 [R=301,L]')
    conf_content = '\n'.join(redirects)

    with open('mywebsite.conf', 'w') as file:
        file.write(conf_content)

# Specify the number of random redirects you want
num_redirects = 600000

# Generate the mywebsite.conf file
generate_mywebsite_conf(num_redirects)
