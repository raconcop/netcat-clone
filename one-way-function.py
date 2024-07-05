

# Writing a python function to under the Diffie-Hellman Key Exchange sequence




# Set a common prime modulus and a generator number
primeMod = 17
gen = 3
print("Generator:", gen)
print("Prime Mod:", primeMod)


# Holds the user data in the server
userDB = []


# Server asks for the two user's names
# Currently no information is made publicly available
for i in range(0,2):
    user1 = [input("\nEnter your name: "), int(input("\nEnter your private key: "))]
    userDB.append(user1)
print("We got the user data!\nNow generating the key exchange\n")



# The one way function to generate a public key based on the private key
def oneWayFunction(priv):    
    output = (gen**priv) % primeMod
    return output

# Function to generate the secret based on a public and private key          
def sharedSecret(pub,priv):
    output = (pub**priv)%primeMod
    return output


# Holds all public keys
allPubK = []

# For each of the users, it generates and stores public keys
for i in range (0, len(userDB)):
    userPubK = oneWayFunction(userDB[i][1])
    print(userDB[i][0],"'s public key", userPubK)
    allPubK.append(userPubK)


# Exchanges the public keys over the internet
# Public keys are now available to everyone
temp = []
temp = allPubK[0] 
allPubK[0] = allPubK[1]
allPubK[1] = temp


# Generates a shared secret that no one knows using the private keys    
for i in range (0, len(allPubK)):
    print(sharedSecret(allPubK[i], userDB[i][1]))


# In the end, we only shared public keys and the equation we used, but no one knows our private keys so we always get the shared result
# To try and decrypt the shared key with the information that is public, it would take a long time based on the generator and prime mod


