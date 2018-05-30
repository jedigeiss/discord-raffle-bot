
# A function that checks if the user has permissions to utilize the bot. 
def permission_check(user, permitted_roles): 
	auth_roles = []
	for x in user.roles:
		auth_roles.append(x.name.lower())

	for x in permitted_roles:
		if x in auth_roles:
			return True
			break
		else:
			return False