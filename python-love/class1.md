



# Bitwise

x << y Left shift
x >> y Right shift
x & y Bitwise and
x | y Bitwise or
x ^ y Bitwise xor (exclusive or)
~x Bitwise negatio

Detailed Explanation with Security-Focused Examples:

1. Left Shift (x << y)
```python
# Example: 00000101 << 2 = 00010100
x = 5
result = x << 2  # Results in 20

# Security Applications:
# 1. Quick multiplication in cryptographic algorithms
# 2. Generating hash values
# 3. Creating bit masks for permissions

# Permission Flag Example
READ = 1 << 0    # 0001 = 1
WRITE = 1 << 1   # 0010 = 2
EXECUTE = 1 << 2 # 0100 = 4
ADMIN = 1 << 3   # 1000 = 8
```

2. Right Shift (x >> y)
```python
# Example: 00010100 >> 2 = 00000101
x = 20
result = x >> 2  # Results in 5

# Security Applications:
# 1. Extracting specific bits from flags
# 2. Processing binary protocols
# 3. Analyzing network packets

# Network Mask Example
ip_addr = 192 # 11000000
subnet = ip_addr >> 6  # Get first two bits
```

3. Bitwise AND (&)
```python
# Example: 00001111 & 00001100 = 00001100
x = 15  # 1111
y = 12  # 1100
result = x & y  # Results in 12 (1100)

# Security Applications:
# 1. Permission checking
# 2. IP address masking
# 3. Hardware security flags

# Permission Check Example
user_permissions = READ | WRITE  # 0011
if user_permissions & WRITE:     # Check if WRITE permission exists
    print("Write access granted")
```

4. Bitwise OR (|)
```python
# Example: 00001111 | 00001100 = 00001111
x = 15  # 1111
y = 12  # 1100
result = x | y  # Results in 15 (1111)

# Security Applications:
# 1. Setting permission flags
# 2. Combining security attributes
# 3. Protocol header construction

# Setting Multiple Permissions
user_access = READ | WRITE | EXECUTE  # Combine permissions
```

5. Bitwise XOR (^)
```python
# Example: 00001111 ^ 00001100 = 00000011
x = 15  # 1111
y = 12  # 1100
result = x ^ y  # Results in 3 (0011)

# Security Applications:
# 1. Basic encryption
# 2. Generating unique identifiers
# 3. Error detection

# Simple XOR Encryption
def xor_encrypt(data, key):
    return bytes(a ^ b for a, b in zip(data, key))

# Example
message = b"SECRET"
key = b"KEYKEY"
encrypted = xor_encrypt(message, key)
decrypted = xor_encrypt(encrypted, key)  # Original message
```

6. Bitwise NOT (~)
```python
# Example: ~00001111 = 11110000
x = 15  # 00001111
result = ~x  # Results in -16 (11110000)

# Security Applications:
# 1. Creating inverse masks
# 2. Permission revocation
# 3. Network subnet calculations

# Removing Permissions
all_permissions = READ | WRITE | EXECUTE
remove_write = ~WRITE
final_permissions = all_permissions & remove_write
```

Real-World Security Implementation Example:
```python
class SecurityPermissions:
    # Permission flags
    NONE = 0          # 00000000
    READ = 1 << 0     # 00000001
    WRITE = 1 << 1    # 00000010
    EXECUTE = 1 << 2  # 00000100
    ADMIN = 1 << 3    # 00001000

    def __init__(self):
        self.permissions = self.NONE

    def grant_permission(self, permission):
        self.permissions |= permission

    def revoke_permission(self, permission):
        self.permissions &= ~permission

    def has_permission(self, permission):
        return bool(self.permissions & permission)

    def list_permissions(self):
        perms = []
        if self.has_permission(self.READ): perms.append("READ")
        if self.has_permission(self.WRITE): perms.append("WRITE")
        if self.has_permission(self.EXECUTE): perms.append("EXECUTE")
        if self.has_permission(self.ADMIN): perms.append("ADMIN")
        return perms

# Usage Example
security = SecurityPermissions()
security.grant_permission(SecurityPermissions.READ | SecurityPermissions.WRITE)
print(security.list_permissions())  # ['READ', 'WRITE']
security.revoke_permission(SecurityPermissions.WRITE)
print(security.list_permissions())  # ['READ']
```

Important Security Considerations:
1. Always use constants for bit flags to maintain clarity
2. Document bit patterns and their meanings
3. Consider using enums for better type safety
4. Be aware of platform-specific integer sizes
5. Consider endianness in network protocols
6. Use masking to ensure clean operations
7. Implement proper boundary checking

These bitwise operations are fundamental in:
- Access Control Lists (ACL)
- Network Protocol Implementation
- Cryptographic Operations
- Hardware Interface Programming
- Performance Optimization
- Memory Management
- Security Flag Management
