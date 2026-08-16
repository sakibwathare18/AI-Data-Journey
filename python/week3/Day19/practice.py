def profile(name,*skills,**details):
    print(f"Name : {name}")
    print(f"Skills : {','.join(skills)}")
    for key,value in details.items():
            print(f"{key}: {value}")

profile(
      "Sakib",
      "Python",
      "SQL",
      "Pandas",
      experience="Beginner",
      goal="Data Engineering"
)