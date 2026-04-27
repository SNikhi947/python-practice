from passlib.context import CryptContext
p_h=CryptContext(schemes="bcrypt",deprecated="auto")
password="Nikhil@123"
hashed=p_h.hash(password)
print(f"password: {password}\n hased password:{hashed}")
check="Nikhil@123"
print("password is match") if p_h.verify(check,hashed) else print("password is in corrrect")