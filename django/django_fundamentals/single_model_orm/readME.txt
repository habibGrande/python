
-creating 3 users:

	User.objects.create(first_name ="moutaz",last_name ="jaber",eamil_address = "mutaz@axsos.com",age = 30)
	User.objects.create(first_name ="habib",last_name ="snobar",eamil_address = "mutaz@axsos.com",age =22 )
	User.objects.create(first_name ="shahrazad",last_name ="masalmah",eamil_address = "mutaz@axsos.com",age = 28)

-retriving all users:

	User.objects.all()

-retriving the last user:

	User.objects.last()

-retriving the first user:
	User.objects.first()

-changing the last name for the user who has id = 3:

	changeLastName = User.objects.get(id=3)
	changeLastName.last_name ="pancakes"
	changeLastName.save()


-delete user with id = 2:

	delete_User = User.objects.get(id=2)
 	delete_User.delete()


-sorting users by name:

	User.objects.all().order_by("first_name")


-bonus- sorting names by descending order:

	User.objects.all().order_by("-first_name")