import itertools

def generate_typosquats(domain):
    """Generate typosquatting variations of a domain"""
    name, tld = domain.split('.')
    typos = []
    
    # Character substitution (e.g., 'o' to '0')
    subs = {'o': '0', 'i': '1', 'l': '1', 's': '5', 'e': '3', 'a': '4'}
    for char, replacement in subs.items():
        if char in name:
            typos.append(name.replace(char, replacement) + '.' + tld)
    
    # Character swaps
    for i in range(len(name) - 1):
        swapped = name[:i] + name[i+1] + name[i] + name[i+2:]
        typos.append(swapped + '.' + tld)
    
    # Character omission
    for i in range(len(name)):
        typos.append(name[:i] + name[i+1:] + '.' + tld)
    
    # Character duplication
    for i in range(len(name)):
        typos.append(name[:i] + name[i] + name[i:] + '.' + tld)
    
    # Additional TLDs
    common_tlds = ['com', 'net', 'org', 'io', 'co']
    for new_tld in common_tlds:
        if new_tld != tld:
            typos.append(name + '.' + new_tld)
    
    return typos

# Example usage
target_domain = "company.com"
typosquats = generate_typosquats(target_domain)
print(f"Generated {len(typosquats)} typosquatting domains for {target_domain}:")
for domain in typosquats[:10]:  # Show first 10
    print(f" - {domain}")
