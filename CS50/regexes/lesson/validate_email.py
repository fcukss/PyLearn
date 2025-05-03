email = input("Enter email: ").strip()

if '@' in email and '.' in email:
    print('Valid')
else:
    print('Invalid')
